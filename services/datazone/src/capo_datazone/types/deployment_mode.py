"""Generated from Smithy shape ``com.amazonaws.datazone#DeploymentMode``."""

from typing import Literal, TypeAlias, cast

DeploymentMode: TypeAlias = Literal[
    "ON_CREATE",
    "ON_DEMAND",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentMode) -> str:
    return value


def deserialize_json(data: str) -> DeploymentMode:
    return cast(DeploymentMode, data)
