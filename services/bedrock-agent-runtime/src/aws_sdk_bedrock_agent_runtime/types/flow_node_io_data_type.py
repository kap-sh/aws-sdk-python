"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowNodeIODataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

FlowNodeIODataType: TypeAlias = Literal[
    "String",
    "Number",
    "Boolean",
    "Object",
    "Array",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "String",
        "Number",
        "Boolean",
        "Object",
        "Array",
    )
)


def serialize_json(value: FlowNodeIODataType) -> str:
    return value


def deserialize_json(data: str) -> FlowNodeIODataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowNodeIODataType value: {data!r}")
    return cast(FlowNodeIODataType, data)
