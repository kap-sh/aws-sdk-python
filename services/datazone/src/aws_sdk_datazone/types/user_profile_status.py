"""Generated from Smithy shape ``com.amazonaws.datazone#UserProfileStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

UserProfileStatus: TypeAlias = Literal[
    "ASSIGNED",
    "NOT_ASSIGNED",
    "ACTIVATED",
    "DEACTIVATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSIGNED",
        "NOT_ASSIGNED",
        "ACTIVATED",
        "DEACTIVATED",
    )
)


def serialize_json(value: UserProfileStatus) -> str:
    return value


def deserialize_json(data: str) -> UserProfileStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserProfileStatus value: {data!r}")
    return cast(UserProfileStatus, data)
