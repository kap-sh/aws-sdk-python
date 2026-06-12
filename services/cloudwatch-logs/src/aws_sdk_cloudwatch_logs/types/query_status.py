"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_cloudwatch_logs.errors import DeserializationError
from aws_sdk_cloudwatch_logs._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

QueryStatus: TypeAlias = Literal[
    "Scheduled",
    "Running",
    "Complete",
    "Failed",
    "Cancelled",
    "Timeout",
    "Unknown",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Scheduled",
        "Running",
        "Complete",
        "Failed",
        "Cancelled",
        "Timeout",
        "Unknown",
    )
)


def serialize_aws_json_1_1(value: QueryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryStatus value: {data!r}")
    return cast(QueryStatus, data)
