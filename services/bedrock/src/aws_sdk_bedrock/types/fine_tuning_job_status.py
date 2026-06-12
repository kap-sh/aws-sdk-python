"""Generated from Smithy shape ``com.amazonaws.bedrock#FineTuningJobStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

FineTuningJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
    )
)


def serialize_json(value: FineTuningJobStatus) -> str:
    return value


def deserialize_json(data: str) -> FineTuningJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FineTuningJobStatus value: {data!r}")
    return cast(FineTuningJobStatus, data)
