"""Generated from Smithy shape ``com.amazonaws.datazone#DateTime``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DateTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> DateTime:
    return datetime.datetime.fromisoformat(data)
