"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimeStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AgentRuntimeStatus: TypeAlias = Literal["CREATING", "CREATE_FAILED", "UPDATING", "UPDATE_FAILED", "READY", "DELETING",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CREATING", "CREATE_FAILED", "UPDATING", "UPDATE_FAILED", "READY", "DELETING",))


def serialize_json(value: AgentRuntimeStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentRuntimeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentRuntimeStatus value: {data!r}")
    return cast(AgentRuntimeStatus, data)