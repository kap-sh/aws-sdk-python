"""Generated from Smithy shape ``com.amazonaws.dlm#PolicyLanguageValues``."""

from typing import Literal, TypeAlias, cast

PolicyLanguageValues: TypeAlias = Literal[
    "SIMPLIFIED",
    "STANDARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyLanguageValues) -> str:
    return value


def deserialize_json(data: str) -> PolicyLanguageValues:
    return cast(PolicyLanguageValues, data)
