"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AutomatedReasoningPolicyBuildWorkflowStatus: TypeAlias = Literal[
    "SCHEDULED",
    "CANCEL_REQUESTED",
    "PREPROCESSING",
    "BUILDING",
    "TESTING",
    "COMPLETED",
    "FAILED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULED",
        "CANCEL_REQUESTED",
        "PREPROCESSING",
        "BUILDING",
        "TESTING",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
    )
)


def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildWorkflowStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningPolicyBuildWorkflowStatus value: {data!r}"
        )
    return cast(AutomatedReasoningPolicyBuildWorkflowStatus, data)
