"""Generated from Smithy shape ``com.amazonaws.bedrock#AttributeType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AttributeType: TypeAlias = Literal[
    "STRING",
    "NUMBER",
    "BOOLEAN",
    "STRING_LIST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "NUMBER",
        "BOOLEAN",
        "STRING_LIST",
    )
)


def serialize_json(value: AttributeType) -> str:
    return value


def deserialize_json(data: str) -> AttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeType value: {data!r}")
    return cast(AttributeType, data)
