"""Generated from Smithy shape ``com.amazonaws.bedrock#PromptRouterType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

PromptRouterType: TypeAlias = Literal[
    "custom",
    "default",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "custom",
        "default",
    )
)


def serialize_json(value: PromptRouterType) -> str:
    return value


def deserialize_json(data: str) -> PromptRouterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PromptRouterType value: {data!r}")
    return cast(PromptRouterType, data)
