"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DataSourceStatus: TypeAlias = Literal[
    "CREATING",
    "FAILED_CREATION",
    "READY",
    "UPDATING",
    "FAILED_UPDATE",
    "RUNNING",
    "DELETING",
    "FAILED_DELETION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "FAILED_CREATION",
        "READY",
        "UPDATING",
        "FAILED_UPDATE",
        "RUNNING",
        "DELETING",
        "FAILED_DELETION",
    )
)


def serialize_json(value: DataSourceStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceStatus value: {data!r}")
    return cast(DataSourceStatus, data)
