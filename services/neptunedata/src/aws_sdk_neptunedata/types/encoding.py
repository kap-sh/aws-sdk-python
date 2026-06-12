"""Generated from Smithy shape ``com.amazonaws.neptunedata#Encoding``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_neptunedata.errors import DeserializationError
from aws_sdk_neptunedata._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Encoding: TypeAlias = Literal["gzip",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("gzip",))


def serialize_json(value: Encoding) -> str:
    return value


def deserialize_json(data: str) -> Encoding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Encoding value: {data!r}")
    return cast(Encoding, data)