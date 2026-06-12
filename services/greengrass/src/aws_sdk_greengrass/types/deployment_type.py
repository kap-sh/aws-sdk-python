"""Generated from Smithy shape ``com.amazonaws.greengrass#DeploymentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

"""The type of deployment. When used for ''CreateDeployment'', only ''NewDeployment'' and ''Redeployment'' are valid."""
DeploymentType: TypeAlias = Literal[
    "NewDeployment",
    "Redeployment",
    "ResetDeployment",
    "ForceResetDeployment",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NewDeployment",
        "Redeployment",
        "ResetDeployment",
        "ForceResetDeployment",
    )
)


def serialize_json(value: DeploymentType) -> str:
    return value


def deserialize_json(data: str) -> DeploymentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentType value: {data!r}")
    return cast(DeploymentType, data)
