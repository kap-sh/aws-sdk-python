"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailWordAction``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GuardrailWordAction: TypeAlias = Literal[
    "BLOCK",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLOCK",
        "NONE",
    )
)


def serialize_json(value: GuardrailWordAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailWordAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailWordAction value: {data!r}")
    return cast(GuardrailWordAction, data)
