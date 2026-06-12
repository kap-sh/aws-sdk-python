"""Generated from Smithy shape ``com.amazonaws.qbusiness#APISchemaType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_qbusiness.errors import DeserializationError
from aws_sdk_qbusiness._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

APISchemaType: TypeAlias = Literal["OPEN_API_V3",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OPEN_API_V3",))


def serialize_json(value: APISchemaType) -> str:
    return value


def deserialize_json(data: str) -> APISchemaType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown APISchemaType value: {data!r}")
    return cast(APISchemaType, data)