"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgentCollaboration``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AgentCollaboration: TypeAlias = Literal["SUPERVISOR", "SUPERVISOR_ROUTER", "DISABLED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SUPERVISOR", "SUPERVISOR_ROUTER", "DISABLED",))


def serialize_json(value: AgentCollaboration) -> str:
    return value


def deserialize_json(data: str) -> AgentCollaboration:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentCollaboration value: {data!r}")
    return cast(AgentCollaboration, data)