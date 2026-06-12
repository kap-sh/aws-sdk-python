"""Generated from Smithy shape ``com.amazonaws.bedrock#ExternalSourceType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ExternalSourceType: TypeAlias = Literal[
    "S3",
    "BYTE_CONTENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "S3",
        "BYTE_CONTENT",
    )
)


def serialize_json(value: ExternalSourceType) -> str:
    return value


def deserialize_json(data: str) -> ExternalSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExternalSourceType value: {data!r}")
    return cast(ExternalSourceType, data)
