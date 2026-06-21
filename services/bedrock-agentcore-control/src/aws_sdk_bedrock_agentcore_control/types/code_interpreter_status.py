"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeInterpreterStatus``."""

from typing import Literal, TypeAlias, cast

CodeInterpreterStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "READY",
    "DELETING",
    "DELETE_FAILED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterStatus) -> str:
    return value


def deserialize_json(data: str) -> CodeInterpreterStatus:
    return cast(CodeInterpreterStatus, data)
