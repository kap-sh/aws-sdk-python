"""Generated from Smithy shape ``com.amazonaws.securitylake#AccessType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_securitylake.errors import DeserializationError
from aws_sdk_securitylake._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AccessType: TypeAlias = Literal["LAKEFORMATION", "S3",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LAKEFORMATION", "S3",))


def serialize_json(value: AccessType) -> str:
    return value


def deserialize_json(data: str) -> AccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessType value: {data!r}")
    return cast(AccessType, data)