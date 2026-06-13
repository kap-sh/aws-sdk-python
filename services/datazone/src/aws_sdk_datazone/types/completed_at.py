"""Generated from Smithy shape ``com.amazonaws.datazone#CompletedAt``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CompletedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CompletedAt) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> CompletedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
