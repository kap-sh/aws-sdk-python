"""Generated from Smithy shape ``com.amazonaws.appconfig#DeploymentEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.deployment_event

DeploymentEvents: TypeAlias = list[
    "capo_appconfig.types.deployment_event.DeploymentEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentEvents) -> list:
    import capo_appconfig.types.deployment_event

    out: list = []
    for item in value:
        out.append(capo_appconfig.types.deployment_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeploymentEvents:
    import capo_appconfig.types.deployment_event

    out: DeploymentEvents = []
    for item in data:
        out.append(capo_appconfig.types.deployment_event.deserialize_json(item))
    return out
