"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayRuleStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

GatewayRuleStatus: TypeAlias = Literal["CREATING", "ACTIVE", "UPDATING", "DELETING",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CREATING", "ACTIVE", "UPDATING", "DELETING",))


def serialize_json(value: GatewayRuleStatus) -> str:
    return value


def deserialize_json(data: str) -> GatewayRuleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GatewayRuleStatus value: {data!r}")
    return cast(GatewayRuleStatus, data)