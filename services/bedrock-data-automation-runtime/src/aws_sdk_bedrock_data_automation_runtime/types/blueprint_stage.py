"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#BlueprintStage``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError
from aws_sdk_bedrock_data_automation_runtime._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""Blueprint stage enum."""
BlueprintStage: TypeAlias = Literal["DEVELOPMENT", "LIVE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DEVELOPMENT", "LIVE",))


def serialize_aws_json_1_1(value: BlueprintStage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlueprintStage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlueprintStage value: {data!r}")
    return cast(BlueprintStage, data)