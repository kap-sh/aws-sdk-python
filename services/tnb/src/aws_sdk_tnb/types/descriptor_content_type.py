"""Generated from Smithy shape ``com.amazonaws.tnb#DescriptorContentType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_tnb.errors import DeserializationError
from aws_sdk_tnb._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DescriptorContentType: TypeAlias = Literal["text/plain",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("text/plain",))


def serialize_json(value: DescriptorContentType) -> str:
    return value


def deserialize_json(data: str) -> DescriptorContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DescriptorContentType value: {data!r}")
    return cast(DescriptorContentType, data)