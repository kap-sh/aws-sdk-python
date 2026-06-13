"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayProtocolType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GatewayProtocolType: TypeAlias = Literal["MCP",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MCP",))


def serialize_json(value: GatewayProtocolType) -> str:
    return value


def deserialize_json(data: str) -> GatewayProtocolType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GatewayProtocolType value: {data!r}")
    return cast(GatewayProtocolType, data)