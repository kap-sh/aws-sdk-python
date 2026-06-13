"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AutomationStreamStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AutomationStreamStatus: TypeAlias = Literal["ENABLED", "DISABLED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ENABLED", "DISABLED",))


def serialize_json(value: AutomationStreamStatus) -> str:
    return value


def deserialize_json(data: str) -> AutomationStreamStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutomationStreamStatus value: {data!r}")
    return cast(AutomationStreamStatus, data)