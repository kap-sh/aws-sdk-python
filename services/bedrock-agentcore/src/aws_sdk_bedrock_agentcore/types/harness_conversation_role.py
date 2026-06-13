"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessConversationRole``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

HarnessConversationRole: TypeAlias = Literal["user", "assistant",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("user", "assistant",))


def serialize_json(value: HarnessConversationRole) -> str:
    return value


def deserialize_json(data: str) -> HarnessConversationRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HarnessConversationRole value: {data!r}")
    return cast(HarnessConversationRole, data)