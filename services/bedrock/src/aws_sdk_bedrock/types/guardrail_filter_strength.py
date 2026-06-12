"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailFilterStrength``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GuardrailFilterStrength: TypeAlias = Literal[
    "NONE",
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_json(value: GuardrailFilterStrength) -> str:
    return value


def deserialize_json(data: str) -> GuardrailFilterStrength:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailFilterStrength value: {data!r}")
    return cast(GuardrailFilterStrength, data)
