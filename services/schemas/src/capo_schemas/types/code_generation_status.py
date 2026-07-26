"""Generated from Smithy shape ``com.amazonaws.schemas#CodeGenerationStatus``."""

from typing import Literal, TypeAlias, cast

CodeGenerationStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeGenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> CodeGenerationStatus:
    return cast(CodeGenerationStatus, data)
