"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ApplicationStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_gameliftstreams.errors import DeserializationError
from aws_sdk_gameliftstreams._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ApplicationStatus: TypeAlias = Literal["INITIALIZED", "PROCESSING", "READY", "DELETING", "ERROR",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INITIALIZED", "PROCESSING", "READY", "DELETING", "ERROR",))


def serialize_json(value: ApplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ApplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationStatus value: {data!r}")
    return cast(ApplicationStatus, data)