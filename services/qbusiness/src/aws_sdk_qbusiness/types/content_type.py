"""Generated from Smithy shape ``com.amazonaws.qbusiness#ContentType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_qbusiness.errors import DeserializationError
from aws_sdk_qbusiness._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ContentType: TypeAlias = Literal["PDF", "HTML", "MS_WORD", "PLAIN_TEXT", "PPT", "RTF", "XML", "XSLT", "MS_EXCEL", "CSV", "JSON", "MD",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PDF", "HTML", "MS_WORD", "PLAIN_TEXT", "PPT", "RTF", "XML", "XSLT", "MS_EXCEL", "CSV", "JSON", "MD",))


def serialize_json(value: ContentType) -> str:
    return value


def deserialize_json(data: str) -> ContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentType value: {data!r}")
    return cast(ContentType, data)