"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeploymentComponentUpdatePolicyAction``."""

from typing import Literal, TypeAlias, cast

DeploymentComponentUpdatePolicyAction: TypeAlias = Literal[
    "NOTIFY_COMPONENTS",
    "SKIP_NOTIFY_COMPONENTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentComponentUpdatePolicyAction) -> str:
    return value


def deserialize_json(data: str) -> DeploymentComponentUpdatePolicyAction:
    return cast(DeploymentComponentUpdatePolicyAction, data)
