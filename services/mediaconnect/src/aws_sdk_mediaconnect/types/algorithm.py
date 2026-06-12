"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Algorithm``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_mediaconnect.errors import DeserializationError
from aws_sdk_mediaconnect._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Algorithm: TypeAlias = Literal["aes128", "aes192", "aes256",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("aes128", "aes192", "aes256",))


def serialize_json(value: Algorithm) -> str:
    return value


def deserialize_json(data: str) -> Algorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Algorithm value: {data!r}")
    return cast(Algorithm, data)