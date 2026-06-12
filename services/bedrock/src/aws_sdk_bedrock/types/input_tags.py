"""Generated from Smithy shape ``com.amazonaws.bedrock#InputTags``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

InputTags: TypeAlias = Literal[
    "HONOR",
    "IGNORE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HONOR",
        "IGNORE",
    )
)


def serialize_json(value: InputTags) -> str:
    return value


def deserialize_json(data: str) -> InputTags:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputTags value: {data!r}")
    return cast(InputTags, data)
