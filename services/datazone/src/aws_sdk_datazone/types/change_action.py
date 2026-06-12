"""Generated from Smithy shape ``com.amazonaws.datazone#ChangeAction``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ChangeAction: TypeAlias = Literal["PUBLISH", "UNPUBLISH",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PUBLISH", "UNPUBLISH",))


def serialize_json(value: ChangeAction) -> str:
    return value


def deserialize_json(data: str) -> ChangeAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeAction value: {data!r}")
    return cast(ChangeAction, data)