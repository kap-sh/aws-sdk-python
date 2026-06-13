"""Generated from Smithy shape ``com.amazonaws.datazone#JobRunStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

JobRunStatus: TypeAlias = Literal[
    "SCHEDULED",
    "IN_PROGRESS",
    "SUCCESS",
    "PARTIALLY_SUCCEEDED",
    "FAILED",
    "ABORTED",
    "TIMED_OUT",
    "CANCELED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULED",
        "IN_PROGRESS",
        "SUCCESS",
        "PARTIALLY_SUCCEEDED",
        "FAILED",
        "ABORTED",
        "TIMED_OUT",
        "CANCELED",
    )
)


def serialize_json(value: JobRunStatus) -> str:
    return value


def deserialize_json(data: str) -> JobRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobRunStatus value: {data!r}")
    return cast(JobRunStatus, data)
