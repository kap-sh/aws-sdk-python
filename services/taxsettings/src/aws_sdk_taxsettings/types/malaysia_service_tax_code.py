"""Generated from Smithy shape ``com.amazonaws.taxsettings#MalaysiaServiceTaxCode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_taxsettings.errors import DeserializationError
from aws_sdk_taxsettings._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

MalaysiaServiceTaxCode: TypeAlias = Literal["Consultancy", "Digital Service And Electronic Medium", "IT Services", "Training Or Coaching",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Consultancy", "Digital Service And Electronic Medium", "IT Services", "Training Or Coaching",))


def serialize_json(value: MalaysiaServiceTaxCode) -> str:
    return value


def deserialize_json(data: str) -> MalaysiaServiceTaxCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MalaysiaServiceTaxCode value: {data!r}")
    return cast(MalaysiaServiceTaxCode, data)