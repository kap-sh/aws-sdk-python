"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EventFilterCondition``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The condition to use for filtering sessions by events.</p>"""
EventFilterCondition: TypeAlias = Literal["HAS_EVENTS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("HAS_EVENTS",))


def serialize_json(value: EventFilterCondition) -> str:
    return value


def deserialize_json(data: str) -> EventFilterCondition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventFilterCondition value: {data!r}")
    return cast(EventFilterCondition, data)