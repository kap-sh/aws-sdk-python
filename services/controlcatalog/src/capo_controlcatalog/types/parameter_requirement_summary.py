"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ParameterRequirementSummary``."""

from typing import Literal, TypeAlias, cast

ParameterRequirementSummary: TypeAlias = Literal[
    "REQUIRED",
    "OPTIONAL",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ParameterRequirementSummary) -> str:
    return value


def deserialize_json(data: str) -> ParameterRequirementSummary:
    return cast(ParameterRequirementSummary, data)
