"""Generated from Smithy shape ``com.amazonaws.notifications#AccessStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_notifications.errors import DeserializationError
from aws_sdk_notifications._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AccessStatus: TypeAlias = Literal["ENABLED", "DISABLED", "PENDING", "FAILED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ENABLED", "DISABLED", "PENDING", "FAILED",))


def serialize_json(value: AccessStatus) -> str:
    return value


def deserialize_json(data: str) -> AccessStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessStatus value: {data!r}")
    return cast(AccessStatus, data)