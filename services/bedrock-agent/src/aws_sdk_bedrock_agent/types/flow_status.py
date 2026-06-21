"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowStatus``."""

from typing import Literal, TypeAlias, cast

FlowStatus: TypeAlias = Literal[
    "Failed",
    "Prepared",
    "Preparing",
    "NotPrepared",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowStatus) -> str:
    return value


def deserialize_json(data: str) -> FlowStatus:
    return cast(FlowStatus, data)
