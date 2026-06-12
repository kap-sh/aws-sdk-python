"""Generated from Smithy shape ``com.amazonaws.taxsettings#AddressRoleType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_taxsettings.errors import DeserializationError
from aws_sdk_taxsettings._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AddressRoleType: TypeAlias = Literal["TaxAddress", "BillingAddress", "ContactAddress",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TaxAddress", "BillingAddress", "ContactAddress",))


def serialize_json(value: AddressRoleType) -> str:
    return value


def deserialize_json(data: str) -> AddressRoleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AddressRoleType value: {data!r}")
    return cast(AddressRoleType, data)