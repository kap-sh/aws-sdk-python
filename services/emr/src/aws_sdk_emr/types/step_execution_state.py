"""Generated from Smithy shape ``com.amazonaws.emr#StepExecutionState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

StepExecutionState: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "CONTINUE",
    "COMPLETED",
    "CANCELLED",
    "FAILED",
    "INTERRUPTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "RUNNING",
        "CONTINUE",
        "COMPLETED",
        "CANCELLED",
        "FAILED",
        "INTERRUPTED",
    )
)


def serialize_aws_json_1_1(value: StepExecutionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepExecutionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepExecutionState value: {data!r}")
    return cast(StepExecutionState, data)
