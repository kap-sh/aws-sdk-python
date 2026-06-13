"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ContentBlockType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ContentBlockType: TypeAlias = Literal["text", "image", "resource", "resource_link",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("text", "image", "resource", "resource_link",))


def serialize_json(value: ContentBlockType) -> str:
    return value


def deserialize_json(data: str) -> ContentBlockType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentBlockType value: {data!r}")
    return cast(ContentBlockType, data)