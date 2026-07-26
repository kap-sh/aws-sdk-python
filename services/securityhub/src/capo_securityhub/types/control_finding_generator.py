"""Generated from Smithy shape ``com.amazonaws.securityhub#ControlFindingGenerator``."""

from typing import Literal, TypeAlias, cast

ControlFindingGenerator: TypeAlias = Literal[
    "STANDARD_CONTROL",
    "SECURITY_CONTROL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlFindingGenerator) -> str:
    return value


def deserialize_json(data: str) -> ControlFindingGenerator:
    return cast(ControlFindingGenerator, data)
