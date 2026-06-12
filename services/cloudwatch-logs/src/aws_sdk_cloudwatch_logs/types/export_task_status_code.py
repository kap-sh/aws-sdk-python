"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ExportTaskStatusCode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_cloudwatch_logs.errors import DeserializationError
from aws_sdk_cloudwatch_logs._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ExportTaskStatusCode: TypeAlias = Literal[
    "CANCELLED",
    "COMPLETED",
    "FAILED",
    "PENDING",
    "PENDING_CANCEL",
    "RUNNING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CANCELLED",
        "COMPLETED",
        "FAILED",
        "PENDING",
        "PENDING_CANCEL",
        "RUNNING",
    )
)


def serialize_aws_json_1_1(value: ExportTaskStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportTaskStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportTaskStatusCode value: {data!r}")
    return cast(ExportTaskStatusCode, data)
