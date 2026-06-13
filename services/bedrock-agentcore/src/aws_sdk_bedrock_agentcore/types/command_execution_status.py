"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CommandExecutionStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CommandExecutionStatus: TypeAlias = Literal["COMPLETED", "TIMED_OUT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("COMPLETED", "TIMED_OUT",))


def serialize_json(value: CommandExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> CommandExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommandExecutionStatus value: {data!r}")
    return cast(CommandExecutionStatus, data)