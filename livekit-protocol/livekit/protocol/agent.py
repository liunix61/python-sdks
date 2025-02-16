# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: livekit_agent.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import models as _models_


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13livekit_agent.proto\x12\x07livekit\x1a\x14livekit_models.proto\"6\n\tAgentInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\"\x92\x01\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1e\n\x04type\x18\x02 \x01(\x0e\x32\x10.livekit.JobType\x12\x1b\n\x04room\x18\x03 \x01(\x0b\x32\r.livekit.Room\x12\x32\n\x0bparticipant\x18\x04 \x01(\x0b\x32\x18.livekit.ParticipantInfoH\x00\x88\x01\x01\x42\x0e\n\x0c_participant\"\xe4\x01\n\rWorkerMessage\x12\x32\n\x08register\x18\x01 \x01(\x0b\x32\x1e.livekit.RegisterWorkerRequestH\x00\x12\x35\n\x0c\x61vailability\x18\x02 \x01(\x0b\x32\x1d.livekit.AvailabilityResponseH\x00\x12-\n\x06status\x18\x03 \x01(\x0b\x32\x1b.livekit.UpdateWorkerStatusH\x00\x12.\n\njob_update\x18\x04 \x01(\x0b\x32\x18.livekit.JobStatusUpdateH\x00\x42\t\n\x07message\"\xb3\x01\n\rServerMessage\x12\x33\n\x08register\x18\x01 \x01(\x0b\x32\x1f.livekit.RegisterWorkerResponseH\x00\x12\x34\n\x0c\x61vailability\x18\x02 \x01(\x0b\x32\x1c.livekit.AvailabilityRequestH\x00\x12,\n\nassignment\x18\x03 \x01(\x0b\x32\x16.livekit.JobAssignmentH\x00\x42\t\n\x07message\"i\n\x15RegisterWorkerRequest\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.livekit.JobType\x12\x11\n\tworker_id\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"C\n\x16RegisterWorkerResponse\x12\x11\n\tworker_id\x18\x01 \x01(\t\x12\x16\n\x0eserver_version\x18\x02 \x01(\t\"0\n\x13\x41vailabilityRequest\x12\x19\n\x03job\x18\x01 \x01(\x0b\x32\x0c.livekit.Job\"9\n\x14\x41vailabilityResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x11\n\tavailable\x18\x02 \x01(\x08\"g\n\x0fJobStatusUpdate\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\"\n\x06status\x18\x02 \x01(\x0e\x32\x12.livekit.JobStatus\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x11\n\tuser_data\x18\x04 \x01(\t\"*\n\rJobAssignment\x12\x19\n\x03job\x18\x01 \x01(\x0b\x32\x0c.livekit.Job\";\n\x12UpdateWorkerStatus\x12%\n\x06status\x18\x01 \x01(\x0e\x32\x15.livekit.WorkerStatus*(\n\x07JobType\x12\x0b\n\x07JT_ROOM\x10\x00\x12\x10\n\x0cJT_PUBLISHER\x10\x01*-\n\x0cWorkerStatus\x12\x10\n\x0cWS_AVAILABLE\x10\x00\x12\x0b\n\x07WS_FULL\x10\x01*:\n\tJobStatus\x12\x0e\n\nJS_UNKNOWN\x10\x00\x12\x0e\n\nJS_SUCCESS\x10\x01\x12\r\n\tJS_FAILED\x10\x02\x42\x46Z#github.com/livekit/protocol/livekit\xaa\x02\rLiveKit.Proto\xea\x02\x0eLiveKit::Protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'agent', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z#github.com/livekit/protocol/livekit\252\002\rLiveKit.Proto\352\002\016LiveKit::Proto'
  _globals['_JOBTYPE']._serialized_start=1167
  _globals['_JOBTYPE']._serialized_end=1207
  _globals['_WORKERSTATUS']._serialized_start=1209
  _globals['_WORKERSTATUS']._serialized_end=1254
  _globals['_JOBSTATUS']._serialized_start=1256
  _globals['_JOBSTATUS']._serialized_end=1314
  _globals['_AGENTINFO']._serialized_start=54
  _globals['_AGENTINFO']._serialized_end=108
  _globals['_JOB']._serialized_start=111
  _globals['_JOB']._serialized_end=257
  _globals['_WORKERMESSAGE']._serialized_start=260
  _globals['_WORKERMESSAGE']._serialized_end=488
  _globals['_SERVERMESSAGE']._serialized_start=491
  _globals['_SERVERMESSAGE']._serialized_end=670
  _globals['_REGISTERWORKERREQUEST']._serialized_start=672
  _globals['_REGISTERWORKERREQUEST']._serialized_end=777
  _globals['_REGISTERWORKERRESPONSE']._serialized_start=779
  _globals['_REGISTERWORKERRESPONSE']._serialized_end=846
  _globals['_AVAILABILITYREQUEST']._serialized_start=848
  _globals['_AVAILABILITYREQUEST']._serialized_end=896
  _globals['_AVAILABILITYRESPONSE']._serialized_start=898
  _globals['_AVAILABILITYRESPONSE']._serialized_end=955
  _globals['_JOBSTATUSUPDATE']._serialized_start=957
  _globals['_JOBSTATUSUPDATE']._serialized_end=1060
  _globals['_JOBASSIGNMENT']._serialized_start=1062
  _globals['_JOBASSIGNMENT']._serialized_end=1104
  _globals['_UPDATEWORKERSTATUS']._serialized_start=1106
  _globals['_UPDATEWORKERSTATUS']._serialized_end=1165
# @@protoc_insertion_point(module_scope)
