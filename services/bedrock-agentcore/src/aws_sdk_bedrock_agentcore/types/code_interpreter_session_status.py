"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CodeInterpreterSessionStatus``."""

from typing import Literal, TypeAlias, cast

CodeInterpreterSessionStatus: TypeAlias = Literal[
    "READY",
    "TERMINATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterSessionStatus) -> str:
    return value


def deserialize_json(data: str) -> CodeInterpreterSessionStatus:
    return cast(CodeInterpreterSessionStatus, data)
