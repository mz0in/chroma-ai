# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromadb/proto/chroma.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x63hromadb/proto/chroma.proto\x12\x06\x63hroma\"U\n\x06Vector\x12\x11\n\tdimension\x18\x01 \x01(\x05\x12\x0e\n\x06vector\x18\x02 \x01(\x0c\x12(\n\x08\x65ncoding\x18\x03 \x01(\x0e\x32\x16.chroma.ScalarEncoding\"\xca\x01\n\x07Segment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12#\n\x05scope\x18\x03 \x01(\x0e\x32\x14.chroma.SegmentScope\x12\x12\n\x05topic\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x17\n\ncollection\x18\x05 \x01(\tH\x01\x88\x01\x01\x12-\n\x08metadata\x18\x06 \x01(\x0b\x32\x16.chroma.UpdateMetadataH\x02\x88\x01\x01\x42\x08\n\x06_topicB\r\n\x0b_collectionB\x0b\n\t_metadata\"b\n\x13UpdateMetadataValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x13\n\tint_value\x18\x02 \x01(\x03H\x00\x12\x15\n\x0b\x66loat_value\x18\x03 \x01(\x01H\x00\x42\x07\n\x05value\"\x96\x01\n\x0eUpdateMetadata\x12\x36\n\x08metadata\x18\x01 \x03(\x0b\x32$.chroma.UpdateMetadata.MetadataEntry\x1aL\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.chroma.UpdateMetadataValue:\x02\x38\x01\"\xb5\x01\n\x15SubmitEmbeddingRecord\x12\n\n\x02id\x18\x01 \x01(\t\x12#\n\x06vector\x18\x02 \x01(\x0b\x32\x0e.chroma.VectorH\x00\x88\x01\x01\x12-\n\x08metadata\x18\x03 \x01(\x0b\x32\x16.chroma.UpdateMetadataH\x01\x88\x01\x01\x12$\n\toperation\x18\x04 \x01(\x0e\x32\x11.chroma.OperationB\t\n\x07_vectorB\x0b\n\t_metadata\"S\n\x15VectorEmbeddingRecord\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06seq_id\x18\x02 \x01(\x0c\x12\x1e\n\x06vector\x18\x03 \x01(\x0b\x32\x0e.chroma.Vector\"q\n\x11VectorQueryResult\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06seq_id\x18\x02 \x01(\x0c\x12\x10\n\x08\x64istance\x18\x03 \x01(\x01\x12#\n\x06vector\x18\x04 \x01(\x0b\x32\x0e.chroma.VectorH\x00\x88\x01\x01\x42\t\n\x07_vector\"@\n\x12VectorQueryResults\x12*\n\x07results\x18\x01 \x03(\x0b\x32\x19.chroma.VectorQueryResult\"(\n\x15SegmentServerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"4\n\x11GetVectorsRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\x12\x12\n\nsegment_id\x18\x02 \x01(\t\"D\n\x12GetVectorsResponse\x12.\n\x07records\x18\x01 \x03(\x0b\x32\x1d.chroma.VectorEmbeddingRecord\"\x86\x01\n\x13QueryVectorsRequest\x12\x1f\n\x07vectors\x18\x01 \x03(\x0b\x32\x0e.chroma.Vector\x12\t\n\x01k\x18\x02 \x01(\x05\x12\x13\n\x0b\x61llowed_ids\x18\x03 \x03(\t\x12\x1a\n\x12include_embeddings\x18\x04 \x01(\x08\x12\x12\n\nsegment_id\x18\x05 \x01(\t\"C\n\x14QueryVectorsResponse\x12+\n\x07results\x18\x01 \x03(\x0b\x32\x1a.chroma.VectorQueryResults*8\n\tOperation\x12\x07\n\x03\x41\x44\x44\x10\x00\x12\n\n\x06UPDATE\x10\x01\x12\n\n\x06UPSERT\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03*(\n\x0eScalarEncoding\x12\x0b\n\x07\x46LOAT32\x10\x00\x12\t\n\x05INT32\x10\x01*(\n\x0cSegmentScope\x12\n\n\x06VECTOR\x10\x00\x12\x0c\n\x08METADATA\x10\x01\x32\x94\x01\n\rSegmentServer\x12?\n\x0bLoadSegment\x12\x0f.chroma.Segment\x1a\x1d.chroma.SegmentServerResponse\"\x00\x12\x42\n\x0eReleaseSegment\x12\x0f.chroma.Segment\x1a\x1d.chroma.SegmentServerResponse\"\x00\x32\xa2\x01\n\x0cVectorReader\x12\x45\n\nGetVectors\x12\x19.chroma.GetVectorsRequest\x1a\x1a.chroma.GetVectorsResponse\"\x00\x12K\n\x0cQueryVectors\x12\x1b.chroma.QueryVectorsRequest\x1a\x1c.chroma.QueryVectorsResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromadb.proto.chroma_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _UPDATEMETADATA_METADATAENTRY._options = None
  _UPDATEMETADATA_METADATAENTRY._serialized_options = b'8\001'
  _globals['_OPERATION']._serialized_start=1406
  _globals['_OPERATION']._serialized_end=1462
  _globals['_SCALARENCODING']._serialized_start=1464
  _globals['_SCALARENCODING']._serialized_end=1504
  _globals['_SEGMENTSCOPE']._serialized_start=1506
  _globals['_SEGMENTSCOPE']._serialized_end=1546
  _globals['_VECTOR']._serialized_start=39
  _globals['_VECTOR']._serialized_end=124
  _globals['_SEGMENT']._serialized_start=127
  _globals['_SEGMENT']._serialized_end=329
  _globals['_UPDATEMETADATAVALUE']._serialized_start=331
  _globals['_UPDATEMETADATAVALUE']._serialized_end=429
  _globals['_UPDATEMETADATA']._serialized_start=432
  _globals['_UPDATEMETADATA']._serialized_end=582
  _globals['_UPDATEMETADATA_METADATAENTRY']._serialized_start=506
  _globals['_UPDATEMETADATA_METADATAENTRY']._serialized_end=582
  _globals['_SUBMITEMBEDDINGRECORD']._serialized_start=585
  _globals['_SUBMITEMBEDDINGRECORD']._serialized_end=766
  _globals['_VECTOREMBEDDINGRECORD']._serialized_start=768
  _globals['_VECTOREMBEDDINGRECORD']._serialized_end=851
  _globals['_VECTORQUERYRESULT']._serialized_start=853
  _globals['_VECTORQUERYRESULT']._serialized_end=966
  _globals['_VECTORQUERYRESULTS']._serialized_start=968
  _globals['_VECTORQUERYRESULTS']._serialized_end=1032
  _globals['_SEGMENTSERVERRESPONSE']._serialized_start=1034
  _globals['_SEGMENTSERVERRESPONSE']._serialized_end=1074
  _globals['_GETVECTORSREQUEST']._serialized_start=1076
  _globals['_GETVECTORSREQUEST']._serialized_end=1128
  _globals['_GETVECTORSRESPONSE']._serialized_start=1130
  _globals['_GETVECTORSRESPONSE']._serialized_end=1198
  _globals['_QUERYVECTORSREQUEST']._serialized_start=1201
  _globals['_QUERYVECTORSREQUEST']._serialized_end=1335
  _globals['_QUERYVECTORSRESPONSE']._serialized_start=1337
  _globals['_QUERYVECTORSRESPONSE']._serialized_end=1404
  _globals['_SEGMENTSERVER']._serialized_start=1549
  _globals['_SEGMENTSERVER']._serialized_end=1697
  _globals['_VECTORREADER']._serialized_start=1700
  _globals['_VECTORREADER']._serialized_end=1862
# @@protoc_insertion_point(module_scope)
