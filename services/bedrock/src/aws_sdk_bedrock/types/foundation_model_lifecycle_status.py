"""Generated from Smithy shape ``com.amazonaws.bedrock#FoundationModelLifecycleStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

FoundationModelLifecycleStatus: TypeAlias = Literal[
    "ACTIVE",
    "LEGACY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "LEGACY",
    )
)


def serialize_json(value: FoundationModelLifecycleStatus) -> str:
    return value


def deserialize_json(data: str) -> FoundationModelLifecycleStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FoundationModelLifecycleStatus value: {data!r}"
        )
    return cast(FoundationModelLifecycleStatus, data)
