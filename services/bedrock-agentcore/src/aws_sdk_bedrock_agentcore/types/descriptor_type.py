"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DescriptorType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p> The type of descriptor associated with a registry record.</p>"""
DescriptorType: TypeAlias = Literal["MCP", "A2A", "CUSTOM", "AGENT_SKILLS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MCP", "A2A", "CUSTOM", "AGENT_SKILLS",))


def serialize_json(value: DescriptorType) -> str:
    return value


def deserialize_json(data: str) -> DescriptorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DescriptorType value: {data!r}")
    return cast(DescriptorType, data)