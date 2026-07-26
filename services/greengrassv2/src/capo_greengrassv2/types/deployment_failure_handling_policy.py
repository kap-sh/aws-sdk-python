"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeploymentFailureHandlingPolicy``."""

from typing import Literal, TypeAlias, cast

DeploymentFailureHandlingPolicy: TypeAlias = Literal[
    "ROLLBACK",
    "DO_NOTHING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentFailureHandlingPolicy) -> str:
    return value


def deserialize_json(data: str) -> DeploymentFailureHandlingPolicy:
    return cast(DeploymentFailureHandlingPolicy, data)
