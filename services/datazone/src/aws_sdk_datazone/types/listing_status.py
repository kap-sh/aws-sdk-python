"""Generated from Smithy shape ``com.amazonaws.datazone#ListingStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ListingStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: ListingStatus) -> str:
    return value


def deserialize_json(data: str) -> ListingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListingStatus value: {data!r}")
    return cast(ListingStatus, data)
