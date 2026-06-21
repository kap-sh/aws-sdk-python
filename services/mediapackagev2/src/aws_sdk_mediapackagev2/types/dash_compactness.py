"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashCompactness``."""

from typing import Literal, TypeAlias, cast

DashCompactness: TypeAlias = Literal[
    "STANDARD",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashCompactness) -> str:
    return value


def deserialize_json(data: str) -> DashCompactness:
    return cast(DashCompactness, data)
