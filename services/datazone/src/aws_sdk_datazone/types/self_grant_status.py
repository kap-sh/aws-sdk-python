"""Generated from Smithy shape ``com.amazonaws.datazone#SelfGrantStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

SelfGrantStatus: TypeAlias = Literal[
    "GRANT_PENDING",
    "REVOKE_PENDING",
    "GRANT_IN_PROGRESS",
    "REVOKE_IN_PROGRESS",
    "GRANTED",
    "GRANT_FAILED",
    "REVOKE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GRANT_PENDING",
        "REVOKE_PENDING",
        "GRANT_IN_PROGRESS",
        "REVOKE_IN_PROGRESS",
        "GRANTED",
        "GRANT_FAILED",
        "REVOKE_FAILED",
    )
)


def serialize_json(value: SelfGrantStatus) -> str:
    return value


def deserialize_json(data: str) -> SelfGrantStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelfGrantStatus value: {data!r}")
    return cast(SelfGrantStatus, data)
