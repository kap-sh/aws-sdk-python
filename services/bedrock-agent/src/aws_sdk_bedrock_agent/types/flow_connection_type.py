"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowConnectionType``."""

from typing import Literal, TypeAlias, cast

FlowConnectionType: TypeAlias = Literal[
    "Data",
    "Conditional",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowConnectionType) -> str:
    return value


def deserialize_json(data: str) -> FlowConnectionType:
    return cast(FlowConnectionType, data)
