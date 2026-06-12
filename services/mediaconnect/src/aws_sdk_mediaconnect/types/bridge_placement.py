"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BridgePlacement``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_mediaconnect.errors import DeserializationError
from aws_sdk_mediaconnect._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

BridgePlacement: TypeAlias = Literal["AVAILABLE", "LOCKED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AVAILABLE", "LOCKED",))


def serialize_json(value: BridgePlacement) -> str:
    return value


def deserialize_json(data: str) -> BridgePlacement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BridgePlacement value: {data!r}")
    return cast(BridgePlacement, data)