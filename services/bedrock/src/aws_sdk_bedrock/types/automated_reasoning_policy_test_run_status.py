"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTestRunStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AutomatedReasoningPolicyTestRunStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "SCHEDULED",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_STARTED",
        "SCHEDULED",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: AutomatedReasoningPolicyTestRunStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyTestRunStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningPolicyTestRunStatus value: {data!r}"
        )
    return cast(AutomatedReasoningPolicyTestRunStatus, data)
