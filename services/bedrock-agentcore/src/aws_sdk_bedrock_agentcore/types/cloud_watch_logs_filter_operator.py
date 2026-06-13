"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CloudWatchLogsFilterOperator``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The comparison operator used to filter CloudWatch Logs entries.</p>"""
CloudWatchLogsFilterOperator: TypeAlias = Literal["Equals", "NotEquals", "GreaterThan", "LessThan", "GreaterThanOrEqual", "LessThanOrEqual", "Contains", "NotContains",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Equals", "NotEquals", "GreaterThan", "LessThan", "GreaterThanOrEqual", "LessThanOrEqual", "Contains", "NotContains",))


def serialize_json(value: CloudWatchLogsFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> CloudWatchLogsFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CloudWatchLogsFilterOperator value: {data!r}")
    return cast(CloudWatchLogsFilterOperator, data)