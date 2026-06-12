"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ModelInvocationJobStatus: TypeAlias = Literal[
    "Submitted",
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
    "PartiallyCompleted",
    "Expired",
    "Validating",
    "Scheduled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Submitted",
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
        "PartiallyCompleted",
        "Expired",
        "Validating",
        "Scheduled",
    )
)


def serialize_json(value: ModelInvocationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelInvocationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelInvocationJobStatus value: {data!r}")
    return cast(ModelInvocationJobStatus, data)
