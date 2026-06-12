"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ApplicationStatusReason``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_gameliftstreams.errors import DeserializationError
from aws_sdk_gameliftstreams._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ApplicationStatusReason: TypeAlias = Literal["internalError", "accessDenied", "sourceModified",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("internalError", "accessDenied", "sourceModified",))


def serialize_json(value: ApplicationStatusReason) -> str:
    return value


def deserialize_json(data: str) -> ApplicationStatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationStatusReason value: {data!r}")
    return cast(ApplicationStatusReason, data)