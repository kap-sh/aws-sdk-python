"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlParameterRequirement``."""

from typing import Literal, TypeAlias, cast

ControlParameterRequirement: TypeAlias = Literal[
    "REQUIRED",
    "OPTIONAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlParameterRequirement) -> str:
    return value


def deserialize_json(data: str) -> ControlParameterRequirement:
    return cast(ControlParameterRequirement, data)
