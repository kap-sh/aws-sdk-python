"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

SubscriptionStatus: TypeAlias = Literal[
    "APPROVED",
    "REVOKED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPROVED",
        "REVOKED",
        "CANCELLED",
    )
)


def serialize_json(value: SubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionStatus value: {data!r}")
    return cast(SubscriptionStatus, data)
