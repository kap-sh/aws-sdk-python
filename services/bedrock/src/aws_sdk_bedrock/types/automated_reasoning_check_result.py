"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckResult``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AutomatedReasoningCheckResult: TypeAlias = Literal[
    "VALID",
    "INVALID",
    "SATISFIABLE",
    "IMPOSSIBLE",
    "TRANSLATION_AMBIGUOUS",
    "TOO_COMPLEX",
    "NO_TRANSLATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALID",
        "INVALID",
        "SATISFIABLE",
        "IMPOSSIBLE",
        "TRANSLATION_AMBIGUOUS",
        "TOO_COMPLEX",
        "NO_TRANSLATION",
    )
)


def serialize_json(value: AutomatedReasoningCheckResult) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningCheckResult:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningCheckResult value: {data!r}"
        )
    return cast(AutomatedReasoningCheckResult, data)
