"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentFilterKey``."""

from typing import Literal, TypeAlias, cast

DeploymentFilterKey: TypeAlias = Literal[
    "WORKLOAD_NAME",
    "DEPLOYMENT_STATUS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentFilterKey) -> str:
    return value


def deserialize_json(data: str) -> DeploymentFilterKey:
    return cast(DeploymentFilterKey, data)
