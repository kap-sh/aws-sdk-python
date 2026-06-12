"""Generated from Smithy shape ``com.amazonaws.s3vectors#DataType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_s3vectors.errors import DeserializationError
from aws_sdk_s3vectors._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DataType: TypeAlias = Literal["float32",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("float32",))


def serialize_json(value: DataType) -> str:
    return value


def deserialize_json(data: str) -> DataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataType value: {data!r}")
    return cast(DataType, data)