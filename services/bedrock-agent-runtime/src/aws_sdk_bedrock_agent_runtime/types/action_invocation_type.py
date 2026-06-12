"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ActionInvocationType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError
from aws_sdk_bedrock_agent_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ActionInvocationType: TypeAlias = Literal["RESULT", "USER_CONFIRMATION", "USER_CONFIRMATION_AND_RESULT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RESULT", "USER_CONFIRMATION", "USER_CONFIRMATION_AND_RESULT",))


def serialize_json(value: ActionInvocationType) -> str:
    return value


def deserialize_json(data: str) -> ActionInvocationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionInvocationType value: {data!r}")
    return cast(ActionInvocationType, data)