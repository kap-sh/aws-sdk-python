"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

DeploymentStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAIL",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStatus:
    return cast(DeploymentStatus, data)
