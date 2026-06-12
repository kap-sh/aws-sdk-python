"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#CustomOutputStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError
from aws_sdk_bedrock_data_automation_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""Custom output status enum"""
CustomOutputStatus: TypeAlias = Literal["MATCH", "NO_MATCH",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MATCH", "NO_MATCH",))


def serialize_aws_json_1_1(value: CustomOutputStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomOutputStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomOutputStatus value: {data!r}")
    return cast(CustomOutputStatus, data)