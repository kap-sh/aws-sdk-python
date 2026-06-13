"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserNetworkMode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

BrowserNetworkMode: TypeAlias = Literal["PUBLIC", "VPC",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PUBLIC", "VPC",))


def serialize_json(value: BrowserNetworkMode) -> str:
    return value


def deserialize_json(data: str) -> BrowserNetworkMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrowserNetworkMode value: {data!r}")
    return cast(BrowserNetworkMode, data)