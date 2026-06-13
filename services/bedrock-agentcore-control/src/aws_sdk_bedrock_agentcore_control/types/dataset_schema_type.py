"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetSchemaType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p> Versioned schema type for dataset examples. Each value identifies both the source format and the version of that format's schema. </p>"""
DatasetSchemaType: TypeAlias = Literal["AGENTCORE_EVALUATION_PREDEFINED_V1", "AGENTCORE_EVALUATION_SIMULATED_V1",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AGENTCORE_EVALUATION_PREDEFINED_V1", "AGENTCORE_EVALUATION_SIMULATED_V1",))


def serialize_json(value: DatasetSchemaType) -> str:
    return value


def deserialize_json(data: str) -> DatasetSchemaType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetSchemaType value: {data!r}")
    return cast(DatasetSchemaType, data)