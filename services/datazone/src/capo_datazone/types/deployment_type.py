"""Generated from Smithy shape ``com.amazonaws.datazone#DeploymentType``."""

from typing import Literal, TypeAlias, cast

DeploymentType: TypeAlias = Literal[
    "CREATE",
    "UPDATE",
    "DELETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentType) -> str:
    return value


def deserialize_json(data: str) -> DeploymentType:
    return cast(DeploymentType, data)
