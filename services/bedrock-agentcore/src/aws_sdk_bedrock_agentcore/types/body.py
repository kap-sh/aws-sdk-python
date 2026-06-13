"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Body``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Body: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: Body) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> Body:
    return base64.b64decode(data)