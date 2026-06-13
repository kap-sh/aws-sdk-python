"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptRuleBehavior``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AcceptRuleBehavior: TypeAlias = Literal[
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


def serialize_json(value: AcceptRuleBehavior) -> str:
    return value


def deserialize_json(data: str) -> AcceptRuleBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceptRuleBehavior value: {data!r}")
    return cast(AcceptRuleBehavior, data)
