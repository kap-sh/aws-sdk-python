"""Generated from Smithy shape ``com.amazonaws.taxsettings#Industries``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_taxsettings.errors import DeserializationError
from aws_sdk_taxsettings._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Industries: TypeAlias = Literal["CirculatingOrg", "ProfessionalOrg", "Banks", "Insurance", "PensionAndBenefitFunds", "DevelopmentAgencies",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CirculatingOrg", "ProfessionalOrg", "Banks", "Insurance", "PensionAndBenefitFunds", "DevelopmentAgencies",))


def serialize_json(value: Industries) -> str:
    return value


def deserialize_json(data: str) -> Industries:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Industries value: {data!r}")
    return cast(Industries, data)