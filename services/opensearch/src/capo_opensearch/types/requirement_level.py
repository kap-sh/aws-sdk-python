"""Generated from Smithy shape ``com.amazonaws.opensearch#RequirementLevel``."""

from typing import Literal, TypeAlias, cast

RequirementLevel: TypeAlias = Literal[
    "REQUIRED",
    "OPTIONAL",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RequirementLevel) -> str:
    return value


def deserialize_json(data: str) -> RequirementLevel:
    return cast(RequirementLevel, data)
