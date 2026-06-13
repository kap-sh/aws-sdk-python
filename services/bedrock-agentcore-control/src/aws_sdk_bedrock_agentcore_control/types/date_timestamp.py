"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DateTimestamp``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DateTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DateTimestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> DateTimestamp:
    return datetime.datetime.fromisoformat(data)