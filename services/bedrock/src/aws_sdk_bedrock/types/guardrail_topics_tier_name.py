"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopicsTierName``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GuardrailTopicsTierName: TypeAlias = Literal[
    "CLASSIC",
    "STANDARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLASSIC",
        "STANDARD",
    )
)


def serialize_json(value: GuardrailTopicsTierName) -> str:
    return value


def deserialize_json(data: str) -> GuardrailTopicsTierName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailTopicsTierName value: {data!r}")
    return cast(GuardrailTopicsTierName, data)
