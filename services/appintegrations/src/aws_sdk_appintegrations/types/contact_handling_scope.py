"""Generated from Smithy shape ``com.amazonaws.appintegrations#ContactHandlingScope``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_appintegrations.errors import DeserializationError
from aws_sdk_appintegrations._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ContactHandlingScope: TypeAlias = Literal["CROSS_CONTACTS", "PER_CONTACT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CROSS_CONTACTS", "PER_CONTACT",))


def serialize_json(value: ContactHandlingScope) -> str:
    return value


def deserialize_json(data: str) -> ContactHandlingScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContactHandlingScope value: {data!r}")
    return cast(ContactHandlingScope, data)