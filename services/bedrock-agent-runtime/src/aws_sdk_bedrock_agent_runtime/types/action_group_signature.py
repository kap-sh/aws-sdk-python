"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ActionGroupSignature``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ActionGroupSignature: TypeAlias = Literal["AMAZON.UserInput", "AMAZON.CodeInterpreter", "ANTHROPIC.Computer", "ANTHROPIC.Bash", "ANTHROPIC.TextEditor",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AMAZON.UserInput", "AMAZON.CodeInterpreter", "ANTHROPIC.Computer", "ANTHROPIC.Bash", "ANTHROPIC.TextEditor",))


def serialize_json(value: ActionGroupSignature) -> str:
    return value


def deserialize_json(data: str) -> ActionGroupSignature:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionGroupSignature value: {data!r}")
    return cast(ActionGroupSignature, data)