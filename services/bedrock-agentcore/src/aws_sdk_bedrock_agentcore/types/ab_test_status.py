"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ABTestStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ABTestStatus: TypeAlias = Literal["CREATING", "ACTIVE", "CREATE_FAILED", "UPDATING", "UPDATE_FAILED", "DELETING", "DELETE_FAILED", "FAILED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CREATING", "ACTIVE", "CREATE_FAILED", "UPDATING", "UPDATE_FAILED", "DELETING", "DELETE_FAILED", "FAILED",))


def serialize_json(value: ABTestStatus) -> str:
    return value


def deserialize_json(data: str) -> ABTestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ABTestStatus value: {data!r}")
    return cast(ABTestStatus, data)