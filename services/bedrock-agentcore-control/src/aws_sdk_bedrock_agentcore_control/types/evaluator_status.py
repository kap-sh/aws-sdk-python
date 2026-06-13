"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EvaluatorStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

EvaluatorStatus: TypeAlias = Literal["ACTIVE", "CREATING", "CREATE_FAILED", "UPDATING", "UPDATE_FAILED", "DELETING",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ACTIVE", "CREATING", "CREATE_FAILED", "UPDATING", "UPDATE_FAILED", "DELETING",))


def serialize_json(value: EvaluatorStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluatorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluatorStatus value: {data!r}")
    return cast(EvaluatorStatus, data)