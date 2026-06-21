"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelDeploymentUpdateStatus``."""

from typing import Literal, TypeAlias, cast

CustomModelDeploymentUpdateStatus: TypeAlias = Literal[
    "Updating",
    "UpdateCompleted",
    "UpdateFailed",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelDeploymentUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> CustomModelDeploymentUpdateStatus:
    return cast(CustomModelDeploymentUpdateStatus, data)
