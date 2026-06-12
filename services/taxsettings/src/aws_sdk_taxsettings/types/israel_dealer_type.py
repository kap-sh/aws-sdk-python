"""Generated from Smithy shape ``com.amazonaws.taxsettings#IsraelDealerType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_taxsettings.errors import DeserializationError
from aws_sdk_taxsettings._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

IsraelDealerType: TypeAlias = Literal["Authorized", "Non-authorized",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Authorized", "Non-authorized",))


def serialize_json(value: IsraelDealerType) -> str:
    return value


def deserialize_json(data: str) -> IsraelDealerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IsraelDealerType value: {data!r}")
    return cast(IsraelDealerType, data)