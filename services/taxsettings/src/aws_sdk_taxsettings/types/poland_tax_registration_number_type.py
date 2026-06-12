"""Generated from Smithy shape ``com.amazonaws.taxsettings#PolandTaxRegistrationNumberType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_taxsettings.errors import DeserializationError
from aws_sdk_taxsettings._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

PolandTaxRegistrationNumberType: TypeAlias = Literal["EUTaxRegistrationNumber", "LocalTaxRegistrationNumber", "LocalRegistrationNumber",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EUTaxRegistrationNumber", "LocalTaxRegistrationNumber", "LocalRegistrationNumber",))


def serialize_json(value: PolandTaxRegistrationNumberType) -> str:
    return value


def deserialize_json(data: str) -> PolandTaxRegistrationNumberType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolandTaxRegistrationNumberType value: {data!r}")
    return cast(PolandTaxRegistrationNumberType, data)