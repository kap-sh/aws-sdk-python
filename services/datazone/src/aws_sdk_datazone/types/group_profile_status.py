"""Generated from Smithy shape ``com.amazonaws.datazone#GroupProfileStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GroupProfileStatus: TypeAlias = Literal[
    "ASSIGNED",
    "NOT_ASSIGNED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSIGNED",
        "NOT_ASSIGNED",
    )
)


def serialize_json(value: GroupProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> GroupProfileStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupProfileStatus value: {data!r}")
    return cast(GroupProfileStatus, data)
