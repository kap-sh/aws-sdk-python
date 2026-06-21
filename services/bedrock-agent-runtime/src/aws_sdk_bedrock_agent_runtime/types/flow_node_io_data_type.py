"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowNodeIODataType``."""

from typing import Literal, TypeAlias, cast

FlowNodeIODataType: TypeAlias = Literal[
    "String",
    "Number",
    "Boolean",
    "Object",
    "Array",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowNodeIODataType) -> str:
    return value


def deserialize_json(data: str) -> FlowNodeIODataType:
    return cast(FlowNodeIODataType, data)
