"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ProgrammingLanguage``."""

from typing import Literal, TypeAlias, cast

ProgrammingLanguage: TypeAlias = Literal[
    "python",
    "javascript",
    "typescript",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProgrammingLanguage) -> str:
    return value


def deserialize_json(data: str) -> ProgrammingLanguage:
    return cast(ProgrammingLanguage, data)
