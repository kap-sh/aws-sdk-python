"""Generated from Smithy shape ``com.amazonaws.datazone#FilterExpressionType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

FilterExpressionType: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: FilterExpressionType) -> str:
    return value


def deserialize_json(data: str) -> FilterExpressionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterExpressionType value: {data!r}")
    return cast(FilterExpressionType, data)
