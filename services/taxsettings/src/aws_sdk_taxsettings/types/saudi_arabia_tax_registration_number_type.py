"""Generated from Smithy shape ``com.amazonaws.taxsettings#SaudiArabiaTaxRegistrationNumberType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_taxsettings.errors import DeserializationError
from aws_sdk_taxsettings._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

SaudiArabiaTaxRegistrationNumberType: TypeAlias = Literal["TaxRegistrationNumber", "TaxIdentificationNumber", "CommercialRegistrationNumber",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TaxRegistrationNumber", "TaxIdentificationNumber", "CommercialRegistrationNumber",))


def serialize_json(value: SaudiArabiaTaxRegistrationNumberType) -> str:
    return value


def deserialize_json(data: str) -> SaudiArabiaTaxRegistrationNumberType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SaudiArabiaTaxRegistrationNumberType value: {data!r}")
    return cast(SaudiArabiaTaxRegistrationNumberType, data)