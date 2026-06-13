"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryUsageRestriction``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GlossaryUsageRestriction: TypeAlias = Literal["ASSET_GOVERNED_TERMS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ASSET_GOVERNED_TERMS",))


def serialize_json(value: GlossaryUsageRestriction) -> str:
    return value


def deserialize_json(data: str) -> GlossaryUsageRestriction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GlossaryUsageRestriction value: {data!r}")
    return cast(GlossaryUsageRestriction, data)
