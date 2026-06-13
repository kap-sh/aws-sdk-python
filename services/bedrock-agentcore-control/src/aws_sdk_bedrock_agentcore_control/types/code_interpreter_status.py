"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeInterpreterStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CodeInterpreterStatus: TypeAlias = Literal["CREATING", "CREATE_FAILED", "READY", "DELETING", "DELETE_FAILED", "DELETED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CREATING", "CREATE_FAILED", "READY", "DELETING", "DELETE_FAILED", "DELETED",))


def serialize_json(value: CodeInterpreterStatus) -> str:
    return value


def deserialize_json(data: str) -> CodeInterpreterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CodeInterpreterStatus value: {data!r}")
    return cast(CodeInterpreterStatus, data)