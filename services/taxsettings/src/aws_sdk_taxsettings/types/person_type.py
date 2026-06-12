"""Generated from Smithy shape ``com.amazonaws.taxsettings#PersonType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_taxsettings.errors import DeserializationError
from aws_sdk_taxsettings._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

PersonType: TypeAlias = Literal["Legal Person", "Physical Person", "Business",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Legal Person", "Physical Person", "Business",))


def serialize_json(value: PersonType) -> str:
    return value


def deserialize_json(data: str) -> PersonType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PersonType value: {data!r}")
    return cast(PersonType, data)