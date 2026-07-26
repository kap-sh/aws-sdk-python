"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeScanStatus``."""

from typing import Literal, TypeAlias, cast

CodeScanStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
    "SKIPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeScanStatus) -> str:
    return value


def deserialize_json(data: str) -> CodeScanStatus:
    return cast(CodeScanStatus, data)
