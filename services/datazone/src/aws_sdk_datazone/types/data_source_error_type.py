"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceErrorType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DataSourceErrorType: TypeAlias = Literal[
    "ACCESS_DENIED_EXCEPTION",
    "CONFLICT_EXCEPTION",
    "INTERNAL_SERVER_EXCEPTION",
    "RESOURCE_NOT_FOUND_EXCEPTION",
    "SERVICE_QUOTA_EXCEEDED_EXCEPTION",
    "THROTTLING_EXCEPTION",
    "VALIDATION_EXCEPTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCESS_DENIED_EXCEPTION",
        "CONFLICT_EXCEPTION",
        "INTERNAL_SERVER_EXCEPTION",
        "RESOURCE_NOT_FOUND_EXCEPTION",
        "SERVICE_QUOTA_EXCEEDED_EXCEPTION",
        "THROTTLING_EXCEPTION",
        "VALIDATION_EXCEPTION",
    )
)


def serialize_json(value: DataSourceErrorType) -> str:
    return value


def deserialize_json(data: str) -> DataSourceErrorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceErrorType value: {data!r}")
    return cast(DataSourceErrorType, data)
