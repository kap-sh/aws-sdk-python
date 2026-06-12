"""Generated from Smithy shape ``com.amazonaws.taxsettings#Sector``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_taxsettings.errors import DeserializationError
from aws_sdk_taxsettings._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Sector: TypeAlias = Literal["Business", "Individual", "Government",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Business", "Individual", "Government",))


def serialize_json(value: Sector) -> str:
    return value


def deserialize_json(data: str) -> Sector:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Sector value: {data!r}")
    return cast(Sector, data)