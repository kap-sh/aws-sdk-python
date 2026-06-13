"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionRequestStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

SubscriptionRequestStatus: TypeAlias = Literal[
    "PENDING",
    "ACCEPTED",
    "REJECTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACCEPTED",
        "REJECTED",
    )
)


def serialize_json(value: SubscriptionRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionRequestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionRequestStatus value: {data!r}")
    return cast(SubscriptionRequestStatus, data)
