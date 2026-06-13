"""Generated from Smithy shape ``com.amazonaws.datazone#DataAssetActivityStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DataAssetActivityStatus: TypeAlias = Literal[
    "FAILED",
    "PUBLISHING_FAILED",
    "SUCCEEDED_CREATED",
    "SUCCEEDED_UPDATED",
    "SKIPPED_ALREADY_IMPORTED",
    "SKIPPED_ARCHIVED",
    "SKIPPED_NO_ACCESS",
    "UNCHANGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "PUBLISHING_FAILED",
        "SUCCEEDED_CREATED",
        "SUCCEEDED_UPDATED",
        "SKIPPED_ALREADY_IMPORTED",
        "SKIPPED_ARCHIVED",
        "SKIPPED_NO_ACCESS",
        "UNCHANGED",
    )
)


def serialize_json(value: DataAssetActivityStatus) -> str:
    return value


def deserialize_json(data: str) -> DataAssetActivityStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataAssetActivityStatus value: {data!r}")
    return cast(DataAssetActivityStatus, data)
