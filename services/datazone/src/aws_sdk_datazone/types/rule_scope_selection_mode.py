"""Generated from Smithy shape ``com.amazonaws.datazone#RuleScopeSelectionMode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

RuleScopeSelectionMode: TypeAlias = Literal[
    "ALL",
    "SPECIFIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "SPECIFIC",
    )
)


def serialize_json(value: RuleScopeSelectionMode) -> str:
    return value


def deserialize_json(data: str) -> RuleScopeSelectionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleScopeSelectionMode value: {data!r}")
    return cast(RuleScopeSelectionMode, data)
