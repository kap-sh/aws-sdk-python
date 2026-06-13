"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ClaimMatchOperatorType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ClaimMatchOperatorType: TypeAlias = Literal["EQUALS", "CONTAINS", "CONTAINS_ANY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EQUALS", "CONTAINS", "CONTAINS_ANY",))


def serialize_json(value: ClaimMatchOperatorType) -> str:
    return value


def deserialize_json(data: str) -> ClaimMatchOperatorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClaimMatchOperatorType value: {data!r}")
    return cast(ClaimMatchOperatorType, data)