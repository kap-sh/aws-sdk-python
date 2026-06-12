"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_qbusiness.errors import DeserializationError
from aws_sdk_qbusiness._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AttachmentStatus: TypeAlias = Literal["FAILED", "SUCCESS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FAILED", "SUCCESS",))


def serialize_json(value: AttachmentStatus) -> str:
    return value


def deserialize_json(data: str) -> AttachmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttachmentStatus value: {data!r}")
    return cast(AttachmentStatus, data)