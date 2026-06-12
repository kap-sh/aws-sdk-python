"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTestRunResult``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AutomatedReasoningPolicyTestRunResult: TypeAlias = Literal[
    "PASSED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSED",
        "FAILED",
    )
)


def serialize_json(value: AutomatedReasoningPolicyTestRunResult) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyTestRunResult:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningPolicyTestRunResult value: {data!r}"
        )
    return cast(AutomatedReasoningPolicyTestRunResult, data)
