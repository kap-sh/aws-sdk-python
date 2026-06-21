"""Generated from Smithy shape ``com.amazonaws.greengrass#DeploymentType``."""

from typing import Literal, TypeAlias, cast

"""The type of deployment. When used for ''CreateDeployment'', only ''NewDeployment'' and ''Redeployment'' are valid."""
DeploymentType: TypeAlias = Literal[
    "NewDeployment",
    "Redeployment",
    "ResetDeployment",
    "ForceResetDeployment",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentType) -> str:
    return value


def deserialize_json(data: str) -> DeploymentType:
    return cast(DeploymentType, data)
