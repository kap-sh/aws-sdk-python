"""Generated from Smithy shape ``com.amazonaws.datazone#DeploymentMessagesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.deployment_message

DeploymentMessagesList: TypeAlias = list[
    "capo_datazone.types.deployment_message.DeploymentMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentMessagesList) -> list:
    return list(value)


def deserialize_json(data: list) -> DeploymentMessagesList:
    return list(data)
