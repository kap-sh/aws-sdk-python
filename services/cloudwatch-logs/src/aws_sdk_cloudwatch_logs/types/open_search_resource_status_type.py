"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchResourceStatusType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_cloudwatch_logs.errors import DeserializationError
from aws_sdk_cloudwatch_logs._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

OpenSearchResourceStatusType: TypeAlias = Literal[
    "ACTIVE",
    "NOT_FOUND",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "NOT_FOUND",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: OpenSearchResourceStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpenSearchResourceStatusType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OpenSearchResourceStatusType value: {data!r}"
        )
    return cast(OpenSearchResourceStatusType, data)
