"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceRunStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DataSourceRunStatus: TypeAlias = Literal[
    "REQUESTED",
    "RUNNING",
    "FAILED",
    "PARTIALLY_SUCCEEDED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUESTED",
        "RUNNING",
        "FAILED",
        "PARTIALLY_SUCCEEDED",
        "SUCCESS",
    )
)


def serialize_json(value: DataSourceRunStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceRunStatus value: {data!r}")
    return cast(DataSourceRunStatus, data)
