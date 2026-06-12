"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ABTestExecutionStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ABTestExecutionStatus: TypeAlias = Literal["PAUSED", "RUNNING", "STOPPED", "NOT_STARTED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PAUSED", "RUNNING", "STOPPED", "NOT_STARTED",))


def serialize_json(value: ABTestExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ABTestExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ABTestExecutionStatus value: {data!r}")
    return cast(ABTestExecutionStatus, data)