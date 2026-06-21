"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowValidationSeverity``."""

from typing import Literal, TypeAlias, cast

FlowValidationSeverity: TypeAlias = Literal[
    "Warning",
    "Error",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowValidationSeverity) -> str:
    return value


def deserialize_json(data: str) -> FlowValidationSeverity:
    return cast(FlowValidationSeverity, data)
