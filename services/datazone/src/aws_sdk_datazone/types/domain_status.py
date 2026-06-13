"""Generated from Smithy shape ``com.amazonaws.datazone#DomainStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DomainStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "CREATION_FAILED",
    "DELETING",
    "DELETED",
    "DELETION_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "CREATION_FAILED",
        "DELETING",
        "DELETED",
        "DELETION_FAILED",
    )
)


def serialize_json(value: DomainStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainStatus value: {data!r}")
    return cast(DomainStatus, data)
