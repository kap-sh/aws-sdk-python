"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeInterpreterNetworkMode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CodeInterpreterNetworkMode: TypeAlias = Literal["PUBLIC", "SANDBOX", "VPC",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PUBLIC", "SANDBOX", "VPC",))


def serialize_json(value: CodeInterpreterNetworkMode) -> str:
    return value


def deserialize_json(data: str) -> CodeInterpreterNetworkMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CodeInterpreterNetworkMode value: {data!r}")
    return cast(CodeInterpreterNetworkMode, data)