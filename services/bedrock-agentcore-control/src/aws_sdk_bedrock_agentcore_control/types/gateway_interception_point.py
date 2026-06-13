"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayInterceptionPoint``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GatewayInterceptionPoint: TypeAlias = Literal["REQUEST", "RESPONSE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("REQUEST", "RESPONSE",))


def serialize_json(value: GatewayInterceptionPoint) -> str:
    return value


def deserialize_json(data: str) -> GatewayInterceptionPoint:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GatewayInterceptionPoint value: {data!r}")
    return cast(GatewayInterceptionPoint, data)