"""Generated from Smithy shape ``com.amazonaws.datazone#ResourceTagSource``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ResourceTagSource: TypeAlias = Literal[
    "PROJECT",
    "PROJECT_PROFILE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROJECT",
        "PROJECT_PROFILE",
    )
)


def serialize_json(value: ResourceTagSource) -> str:
    return value


def deserialize_json(data: str) -> ResourceTagSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceTagSource value: {data!r}")
    return cast(ResourceTagSource, data)
