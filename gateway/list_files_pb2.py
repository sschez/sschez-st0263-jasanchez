# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list_files.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10list_files.proto\"\x12\n\x10ListFilesRequest\")\n\x11ListFilesResponse\x12\x14\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x05.File\"&\n\x04\x46ile\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0c\n\x04\x66ile\x18\x02 \x01(\x0c\x32\x44\n\tListFiles\x12\x37\n\x0cGetFilesList\x12\x11.ListFilesRequest\x1a\x12.ListFilesResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'list_files_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LISTFILESREQUEST._serialized_start=20
  _LISTFILESREQUEST._serialized_end=38
  _LISTFILESRESPONSE._serialized_start=40
  _LISTFILESRESPONSE._serialized_end=81
  _FILE._serialized_start=83
  _FILE._serialized_end=121
  _LISTFILES._serialized_start=123
  _LISTFILES._serialized_end=191
# @@protoc_insertion_point(module_scope)
