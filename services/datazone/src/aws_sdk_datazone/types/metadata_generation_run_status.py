"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataGenerationRunStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

MetadataGenerationRunStatus: TypeAlias = Literal[
    "SUBMITTED",
    "IN_PROGRESS",
    "CANCELED",
    "SUCCEEDED",
    "FAILED",
    "PARTIALLY_SUCCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "IN_PROGRESS",
        "CANCELED",
        "SUCCEEDED",
        "FAILED",
        "PARTIALLY_SUCCEEDED",
    )
)


def serialize_json(value: MetadataGenerationRunStatus) -> str:
    return value


def deserialize_json(data: str) -> MetadataGenerationRunStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MetadataGenerationRunStatus value: {data!r}"
        )
    return cast(MetadataGenerationRunStatus, data)
