"""Generated from Smithy shape ``com.amazonaws.datazone#SortKey``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

SortKey: TypeAlias = Literal[
    "CREATED_AT",
    "UPDATED_AT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED_AT",
        "UPDATED_AT",
    )
)


def serialize_json(value: SortKey) -> str:
    return value


def deserialize_json(data: str) -> SortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortKey value: {data!r}")
    return cast(SortKey, data)
