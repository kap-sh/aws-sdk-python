"""Generated from Smithy shape ``com.amazonaws.opensearch#ActionSeverity``."""

from typing import Literal, TypeAlias, cast

ActionSeverity: TypeAlias = Literal[
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionSeverity) -> str:
    return value


def deserialize_json(data: str) -> ActionSeverity:
    return cast(ActionSeverity, data)
