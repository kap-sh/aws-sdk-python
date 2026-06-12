"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckLogicWarningType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AutomatedReasoningCheckLogicWarningType: TypeAlias = Literal[
    "ALWAYS_TRUE",
    "ALWAYS_FALSE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALWAYS_TRUE",
        "ALWAYS_FALSE",
    )
)


def serialize_json(value: AutomatedReasoningCheckLogicWarningType) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningCheckLogicWarningType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningCheckLogicWarningType value: {data!r}"
        )
    return cast(AutomatedReasoningCheckLogicWarningType, data)
