"""Generated from Smithy shape ``com.amazonaws.mq#__listOfDeploymentMode``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mq.types.deployment_mode

__listOfDeploymentMode: TypeAlias = list["capo_mq.types.deployment_mode.DeploymentMode"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDeploymentMode) -> list:
    import capo_mq.types.deployment_mode

    out: list = []
    for item in value:
        out.append(capo_mq.types.deployment_mode.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDeploymentMode:
    import capo_mq.types.deployment_mode

    out: __listOfDeploymentMode = []
    for item in data:
        out.append(capo_mq.types.deployment_mode.deserialize_json(item))
    return out
