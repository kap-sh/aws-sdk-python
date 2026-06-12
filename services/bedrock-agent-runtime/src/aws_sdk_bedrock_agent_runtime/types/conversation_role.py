"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ConversationRole``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ConversationRole: TypeAlias = Literal["user", "assistant",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("user", "assistant",))


def serialize_json(value: ConversationRole) -> str:
    return value


def deserialize_json(data: str) -> ConversationRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConversationRole value: {data!r}")
    return cast(ConversationRole, data)