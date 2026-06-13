"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserActionStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The status of a browser action execution.</p>"""
BrowserActionStatus: TypeAlias = Literal["SUCCESS", "FAILED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SUCCESS", "FAILED",))


def serialize_json(value: BrowserActionStatus) -> str:
    return value


def deserialize_json(data: str) -> BrowserActionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrowserActionStatus value: {data!r}")
    return cast(BrowserActionStatus, data)