"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ParameterType``."""

from typing import Literal, TypeAlias, cast

ParameterType: TypeAlias = Literal[
    "string",
    "number",
    "integer",
    "boolean",
    "array",
]


# --- restJson1 ser/de ---
def serialize_json(value: ParameterType) -> str:
    return value


def deserialize_json(data: str) -> ParameterType:
    return cast(ParameterType, data)
