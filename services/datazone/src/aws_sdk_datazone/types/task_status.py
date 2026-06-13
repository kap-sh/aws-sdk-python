"""Generated from Smithy shape ``com.amazonaws.datazone#TaskStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

TaskStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: TaskStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskStatus value: {data!r}")
    return cast(TaskStatus, data)
