"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

CustomModelDeploymentStatus: TypeAlias = Literal[
    "Creating",
    "Active",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelDeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> CustomModelDeploymentStatus:
    return cast(CustomModelDeploymentStatus, data)
