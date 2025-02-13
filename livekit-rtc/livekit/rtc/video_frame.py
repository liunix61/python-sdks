# Copyright 2023 LiveKit, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import ctypes
from typing import Union
from ._proto import video_frame_pb2 as proto_video
from ._proto import ffi_pb2 as proto
from typing import List, Optional
from ._ffi_client import FfiClient, FfiHandle
from ._utils import get_address


class VideoFrame:
    def __init__(
        self,
        width: int,
        height: int,
        type: proto_video.VideoBufferType.ValueType,
        data: Union[bytes, bytearray, memoryview],
    ) -> None:
        self._width = width
        self._height = height
        self._type = type
        self._data = bytearray(data)

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def type(self) -> proto_video.VideoBufferType.ValueType:
        return self._type

    @property
    def data(self) -> memoryview:
        return memoryview(self._data)

    @staticmethod
    def _from_owned_info(owned_info: proto_video.OwnedVideoBuffer) -> "VideoFrame":
        info = owned_info.info
        cdata = (ctypes.c_uint8 * info.data_len).from_address(info.data_ptr)
        data = bytearray(cdata)
        frame = VideoFrame(
            width=info.width,
            height=info.height,
            type=info.type,
            data=data,
        )
        FfiHandle(owned_info.handle.id)
        return frame

    def _proto_info(self) -> proto_video.VideoBufferInfo:
        info = proto_video.VideoBufferInfo()
        info.components.extend(_get_plane_infos(self.type, self.width, self.height))
        info.width = self.width
        info.height = self.height
        info.type = self.type
        info.data_ptr = get_address(self.data)
        info.data_len = len(self.data)

        if self.type in [
            proto_video.VideoBufferType.ARGB,
            proto_video.VideoBufferType.ABGR,
            proto_video.VideoBufferType.RGBA,
            proto_video.VideoBufferType.BGRA,
        ]:
            info.stride = self.width * 4
        elif self.type == proto_video.VideoBufferType.RGB24:
            info.stride = self.width * 3

        return info

    def get_plane(self, plane_nth: int) -> Optional[memoryview]:
        plane_infos = _get_plane_infos(self.type, self.width, self.height)
        if plane_nth >= len(plane_infos):
            return None

        plane_info = plane_infos[plane_nth]
        return memoryview(self.data)[
            plane_info.offset : plane_info.offset + plane_info.size
        ]

    def convert(
        self, type: proto_video.VideoBufferType.ValueType, *, flip_y: bool = False
    ) -> "VideoFrame":
        req = proto.FfiRequest()
        req.video_convert.flip_y = flip_y
        req.video_convert.dst_type = type
        req.video_convert.buffer.CopyFrom(self._proto_info())
        resp = FfiClient.instance.request(req)
        if resp.video_convert.error:
            raise Exception(resp.video_convert.error)

        return VideoFrame._from_owned_info(resp.video_convert.buffer)


def _component_info(
    offset: int, stride: int, size: int
) -> proto_video.VideoBufferInfo.ComponentInfo:
    cmpt = proto_video.VideoBufferInfo.ComponentInfo()
    cmpt.offset = offset
    cmpt.stride = stride
    cmpt.size = size
    return cmpt


def _get_plane_infos(
    type: proto_video.VideoBufferType.ValueType, width: int, height: int
) -> List[proto_video.VideoBufferInfo.ComponentInfo]:
    if type == proto_video.VideoBufferType.I420:
        chroma_width = (width + 1) // 2
        chroma_height = (height + 1) // 2
        y = _component_info(0, width, width * height)
        u = _component_info(y.size, chroma_width, chroma_width * chroma_height)
        v = _component_info(
            u.offset + u.size, chroma_width, chroma_width * chroma_height
        )
        return [y, u, v]
    elif type == proto_video.VideoBufferType.I420A:
        chroma_width = (width + 1) // 2
        chroma_height = (height + 1) // 2
        y = _component_info(0, width, width * height)
        u = _component_info(y.size, chroma_width, chroma_width * chroma_height)
        v = _component_info(
            u.offset + u.size, chroma_width, chroma_width * chroma_height
        )
        a = _component_info(v.offset + v.size, width, width * height)
        return [y, u, v, a]
    elif type == proto_video.VideoBufferType.I422:
        chroma_width = (width + 1) // 2
        y = _component_info(0, width, width * height)
        u = _component_info(y.size, chroma_width, chroma_width * height)
        v = _component_info(u.offset + u.size, chroma_width, chroma_width * height)
        return [y, u, v]
    elif type == proto_video.VideoBufferType.I444:
        y = _component_info(0, width, width * height)
        u = _component_info(y.size, width, width * height)
        v = _component_info(u.offset + u.size, width, width * height)
        return [y, u, v]
    elif type == proto_video.VideoBufferType.I010:
        chroma_width = (width + 1) // 2
        chroma_height = (height + 1) // 2
        y = _component_info(0, width * 2, width * height * 2)
        u = _component_info(y.size, chroma_width * 2, chroma_width * chroma_height * 2)
        v = _component_info(
            u.offset + u.size, chroma_width * 2, chroma_width * chroma_height * 2
        )
        return [y, u, v]
    elif type == proto_video.VideoBufferType.NV12:
        chroma_width = (width + 1) // 2
        chroma_height = (height + 1) // 2
        y = _component_info(0, width, width * height)
        uv = _component_info(
            y.stride * height, chroma_width * 2, chroma_width * chroma_height * 2
        )
        return [y, uv]

    return []
