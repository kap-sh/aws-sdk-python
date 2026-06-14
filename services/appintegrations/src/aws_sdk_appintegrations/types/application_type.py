"""Generated from Smithy shape ``com.amazonaws.appintegrations#ApplicationType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_appintegrations.errors import DeserializationError
from aws_sdk_appintegrations._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<value>The type of application</value>"""
ApplicationType: TypeAlias = Literal["STANDARD", "SERVICE", "MCP_SERVER",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("STANDARD", "SERVICE", "MCP_SERVER",))


def serialize_json(value: ApplicationType) -> str:
    return value


def deserialize_json(data: str) -> ApplicationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationType value: {data!r}")
    return cast(ApplicationType, data)