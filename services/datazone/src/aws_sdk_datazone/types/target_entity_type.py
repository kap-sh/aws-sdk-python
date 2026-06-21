"""Generated from Smithy shape ``com.amazonaws.datazone#TargetEntityType``."""

from typing import Literal, TypeAlias, cast

TargetEntityType: TypeAlias = Literal[
    "DOMAIN_UNIT",
    "ENVIRONMENT_BLUEPRINT_CONFIGURATION",
    "ENVIRONMENT_PROFILE",
    "ASSET_TYPE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetEntityType) -> str:
    return value


def deserialize_json(data: str) -> TargetEntityType:
    return cast(TargetEntityType, data)
