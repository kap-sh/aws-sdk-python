"""Generated from Smithy shape ``com.amazonaws.taxsettings#HeritageStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_taxsettings.errors import DeserializationError
from aws_sdk_taxsettings._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

HeritageStatus: TypeAlias = Literal["OptIn", "OptOut",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OptIn", "OptOut",))


def serialize_json(value: HeritageStatus) -> str:
    return value


def deserialize_json(data: str) -> HeritageStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HeritageStatus value: {data!r}")
    return cast(HeritageStatus, data)