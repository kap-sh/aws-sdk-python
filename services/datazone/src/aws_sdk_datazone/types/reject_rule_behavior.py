"""Generated from Smithy shape ``com.amazonaws.datazone#RejectRuleBehavior``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

RejectRuleBehavior: TypeAlias = Literal[
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "NONE",
    )
)


def serialize_json(value: RejectRuleBehavior) -> str:
    return value


def deserialize_json(data: str) -> RejectRuleBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RejectRuleBehavior value: {data!r}")
    return cast(RejectRuleBehavior, data)
