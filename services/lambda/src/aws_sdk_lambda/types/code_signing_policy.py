"""Generated from Smithy shape ``com.amazonaws.lambda#CodeSigningPolicy``."""

from typing import Literal, TypeAlias, cast

CodeSigningPolicy: TypeAlias = Literal[
    "Warn",
    "Enforce",
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeSigningPolicy) -> str:
    return value


def deserialize_json(data: str) -> CodeSigningPolicy:
    return cast(CodeSigningPolicy, data)
