"""Generated from Smithy shape ``com.amazonaws.appconfig#DeploymentState``."""

from typing import Literal, TypeAlias, cast

DeploymentState: TypeAlias = Literal[
    "BAKING",
    "VALIDATING",
    "DEPLOYING",
    "COMPLETE",
    "ROLLING_BACK",
    "ROLLED_BACK",
    "REVERTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentState) -> str:
    return value


def deserialize_json(data: str) -> DeploymentState:
    return cast(DeploymentState, data)
