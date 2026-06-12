"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatResponseConfigurationStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_qbusiness.errors import DeserializationError
from aws_sdk_qbusiness._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ChatResponseConfigurationStatus: TypeAlias = Literal["CREATING", "UPDATING", "FAILED", "ACTIVE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CREATING", "UPDATING", "FAILED", "ACTIVE",))


def serialize_json(value: ChatResponseConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> ChatResponseConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChatResponseConfigurationStatus value: {data!r}")
    return cast(ChatResponseConfigurationStatus, data)