"""Generated from Smithy shape ``com.amazonaws.taxsettings#ChileDocumentType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_taxsettings.errors import DeserializationError
from aws_sdk_taxsettings._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p> The type of tax document for Chile.</p>"""
ChileDocumentType: TypeAlias = Literal["Invoice", "Receipt",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Invoice", "Receipt",))


def serialize_json(value: ChileDocumentType) -> str:
    return value


def deserialize_json(data: str) -> ChileDocumentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChileDocumentType value: {data!r}")
    return cast(ChileDocumentType, data)