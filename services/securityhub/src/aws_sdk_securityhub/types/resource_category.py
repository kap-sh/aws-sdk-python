"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceCategory``."""

from typing import Literal, TypeAlias, cast

ResourceCategory: TypeAlias = Literal[
    "Compute",
    "Database",
    "Storage",
    "Code",
    "AI/ML",
    "Identity",
    "Network",
    "Other",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceCategory) -> str:
    return value


def deserialize_json(data: str) -> ResourceCategory:
    return cast(ResourceCategory, data)
