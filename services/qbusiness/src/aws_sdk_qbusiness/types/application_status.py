"""Generated from Smithy shape ``com.amazonaws.qbusiness#ApplicationStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_qbusiness.errors import DeserializationError
from aws_sdk_qbusiness._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ApplicationStatus: TypeAlias = Literal["CREATING", "ACTIVE", "DELETING", "FAILED", "UPDATING",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CREATING", "ACTIVE", "DELETING", "FAILED", "UPDATING",))


def serialize_json(value: ApplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ApplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationStatus value: {data!r}")
    return cast(ApplicationStatus, data)