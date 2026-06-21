"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJobStatus``."""

from typing import Literal, TypeAlias, cast

CodegenJobStatus: TypeAlias = Literal[
    "in_progress",
    "failed",
    "succeeded",
]


# --- restJson1 ser/de ---
def serialize_json(value: CodegenJobStatus) -> str:
    return value


def deserialize_json(data: str) -> CodegenJobStatus:
    return cast(CodegenJobStatus, data)
