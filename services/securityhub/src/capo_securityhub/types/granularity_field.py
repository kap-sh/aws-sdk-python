"""Generated from Smithy shape ``com.amazonaws.securityhub#GranularityField``."""

from typing import Literal, TypeAlias, cast

GranularityField: TypeAlias = Literal[
    "Daily",
    "Weekly",
    "Monthly",
]


# --- restJson1 ser/de ---
def serialize_json(value: GranularityField) -> str:
    return value


def deserialize_json(data: str) -> GranularityField:
    return cast(GranularityField, data)
