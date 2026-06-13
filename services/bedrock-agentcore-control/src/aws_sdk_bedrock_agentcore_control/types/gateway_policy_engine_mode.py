"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayPolicyEngineMode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GatewayPolicyEngineMode: TypeAlias = Literal["LOG_ONLY", "ENFORCE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LOG_ONLY", "ENFORCE",))


def serialize_json(value: GatewayPolicyEngineMode) -> str:
    return value


def deserialize_json(data: str) -> GatewayPolicyEngineMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GatewayPolicyEngineMode value: {data!r}")
    return cast(GatewayPolicyEngineMode, data)