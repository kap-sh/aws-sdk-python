"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ExecutionType``."""

from typing import Literal, TypeAlias, cast

ExecutionType: TypeAlias = Literal[
    "LAMBDA",
    "RETURN_CONTROL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionType) -> str:
    return value


def deserialize_json(data: str) -> ExecutionType:
    return cast(ExecutionType, data)
