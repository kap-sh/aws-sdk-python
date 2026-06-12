"""Generated from Smithy shape ``com.amazonaws.neptunedata#Action``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_neptunedata.errors import DeserializationError
from aws_sdk_neptunedata._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Action: TypeAlias = Literal["initiateDatabaseReset", "performDatabaseReset",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("initiateDatabaseReset", "performDatabaseReset",))


def serialize_json(value: Action) -> str:
    return value


def deserialize_json(data: str) -> Action:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Action value: {data!r}")
    return cast(Action, data)