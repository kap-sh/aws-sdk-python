"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GuardrailStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "VERSIONING",
    "READY",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "VERSIONING",
        "READY",
        "FAILED",
        "DELETING",
    )
)


def serialize_json(value: GuardrailStatus) -> str:
    return value


def deserialize_json(data: str) -> GuardrailStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailStatus value: {data!r}")
    return cast(GuardrailStatus, data)
