"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Day``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_mediaconnect.errors import DeserializationError
from aws_sdk_mediaconnect._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Day: TypeAlias = Literal["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY",))


def serialize_json(value: Day) -> str:
    return value


def deserialize_json(data: str) -> Day:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Day value: {data!r}")
    return cast(Day, data)