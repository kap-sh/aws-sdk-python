"""Generated from Smithy shape ``com.amazonaws.datazone#S3Permission``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

S3Permission: TypeAlias = Literal[
    "READ",
    "WRITE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ",
        "WRITE",
    )
)


def serialize_json(value: S3Permission) -> str:
    return value


def deserialize_json(data: str) -> S3Permission:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3Permission value: {data!r}")
    return cast(S3Permission, data)
