"""Generated from Smithy shape ``com.amazonaws.bedrock#AdvancedPromptOptimizationJobStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The status of an advanced prompt optimization job.</p>"""
AdvancedPromptOptimizationJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "PartiallyCompleted",
    "Stopping",
    "Stopped",
    "Deleting",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
        "PartiallyCompleted",
        "Stopping",
        "Stopped",
        "Deleting",
    )
)


def serialize_json(value: AdvancedPromptOptimizationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> AdvancedPromptOptimizationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AdvancedPromptOptimizationJobStatus value: {data!r}"
        )
    return cast(AdvancedPromptOptimizationJobStatus, data)
