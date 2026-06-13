"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionGrantOverallStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

SubscriptionGrantOverallStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "GRANT_FAILED",
    "REVOKE_FAILED",
    "GRANT_AND_REVOKE_FAILED",
    "COMPLETED",
    "INACCESSIBLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "GRANT_FAILED",
        "REVOKE_FAILED",
        "GRANT_AND_REVOKE_FAILED",
        "COMPLETED",
        "INACCESSIBLE",
    )
)


def serialize_json(value: SubscriptionGrantOverallStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionGrantOverallStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SubscriptionGrantOverallStatus value: {data!r}"
        )
    return cast(SubscriptionGrantOverallStatus, data)
