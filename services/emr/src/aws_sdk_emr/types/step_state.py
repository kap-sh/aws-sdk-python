"""Generated from Smithy shape ``com.amazonaws.emr#StepState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_emr.errors import DeserializationError
from aws_sdk_emr._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

StepState: TypeAlias = Literal[
    "PENDING",
    "CANCEL_PENDING",
    "RUNNING",
    "COMPLETED",
    "CANCELLED",
    "FAILED",
    "INTERRUPTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "CANCEL_PENDING",
        "RUNNING",
        "COMPLETED",
        "CANCELLED",
        "FAILED",
        "INTERRUPTED",
    )
)


def serialize_aws_json_1_1(value: StepState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepState value: {data!r}")
    return cast(StepState, data)
