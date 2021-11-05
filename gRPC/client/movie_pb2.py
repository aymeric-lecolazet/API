# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: movie.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='movie.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bmovie.proto\"\x15\n\x07MovieID\x12\n\n\x02id\x18\x01 \x01(\t\"\x1b\n\nMovieTitle\x12\r\n\x05title\x18\x01 \x01(\t\"H\n\tMovieData\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0e\n\x06rating\x18\x02 \x01(\x02\x12\x10\n\x08\x64irector\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\"\x07\n\x05\x45mpty2\xf6\x01\n\x05Movie\x12&\n\x0cGetMovieByID\x12\x08.MovieID\x1a\n.MovieData\"\x00\x12,\n\x0fGetMovieByTitle\x12\x0b.MovieTitle\x1a\n.MovieData\"\x00\x12\'\n\rGetListMovies\x12\x06.Empty\x1a\n.MovieData\"\x00\x30\x01\x12%\n\x0f\x44\x65leteMovieByID\x12\x08.MovieID\x1a\x06.Empty\"\x00\x12!\n\tPostMovie\x12\n.MovieData\x1a\x06.Empty\"\x00\x12$\n\x0cPutMovieByID\x12\n.MovieData\x1a\x06.Empty\"\x00\x62\x06proto3'
)




_MOVIEID = _descriptor.Descriptor(
  name='MovieID',
  full_name='MovieID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MovieID.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=36,
)


_MOVIETITLE = _descriptor.Descriptor(
  name='MovieTitle',
  full_name='MovieTitle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='MovieTitle.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=65,
)


_MOVIEDATA = _descriptor.Descriptor(
  name='MovieData',
  full_name='MovieData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='MovieData.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rating', full_name='MovieData.rating', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='director', full_name='MovieData.director', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='MovieData.id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=139,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['MovieID'] = _MOVIEID
DESCRIPTOR.message_types_by_name['MovieTitle'] = _MOVIETITLE
DESCRIPTOR.message_types_by_name['MovieData'] = _MOVIEDATA
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MovieID = _reflection.GeneratedProtocolMessageType('MovieID', (_message.Message,), {
  'DESCRIPTOR' : _MOVIEID,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:MovieID)
  })
_sym_db.RegisterMessage(MovieID)

MovieTitle = _reflection.GeneratedProtocolMessageType('MovieTitle', (_message.Message,), {
  'DESCRIPTOR' : _MOVIETITLE,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:MovieTitle)
  })
_sym_db.RegisterMessage(MovieTitle)

MovieData = _reflection.GeneratedProtocolMessageType('MovieData', (_message.Message,), {
  'DESCRIPTOR' : _MOVIEDATA,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:MovieData)
  })
_sym_db.RegisterMessage(MovieData)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'movie_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)



_MOVIE = _descriptor.ServiceDescriptor(
  name='Movie',
  full_name='Movie',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=151,
  serialized_end=397,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMovieByID',
    full_name='Movie.GetMovieByID',
    index=0,
    containing_service=None,
    input_type=_MOVIEID,
    output_type=_MOVIEDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMovieByTitle',
    full_name='Movie.GetMovieByTitle',
    index=1,
    containing_service=None,
    input_type=_MOVIETITLE,
    output_type=_MOVIEDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetListMovies',
    full_name='Movie.GetListMovies',
    index=2,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_MOVIEDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteMovieByID',
    full_name='Movie.DeleteMovieByID',
    index=3,
    containing_service=None,
    input_type=_MOVIEID,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PostMovie',
    full_name='Movie.PostMovie',
    index=4,
    containing_service=None,
    input_type=_MOVIEDATA,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PutMovieByID',
    full_name='Movie.PutMovieByID',
    index=5,
    containing_service=None,
    input_type=_MOVIEDATA,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MOVIE)

DESCRIPTOR.services_by_name['Movie'] = _MOVIE

# @@protoc_insertion_point(module_scope)
