"""Generated from Smithy shape ``com.amazonaws.bedrock#EntitlementAvailability``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

EntitlementAvailability: TypeAlias = Literal[
    "AVAILABLE",
    "NOT_AVAILABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "NOT_AVAILABLE",
    )
)


def serialize_json(value: EntitlementAvailability) -> str:
    return value


def deserialize_json(data: str) -> EntitlementAvailability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntitlementAvailability value: {data!r}")
    return cast(EntitlementAvailability, data)
