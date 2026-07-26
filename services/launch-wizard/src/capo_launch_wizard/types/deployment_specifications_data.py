"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentSpecificationsData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_specifications_field

DeploymentSpecificationsData: TypeAlias = list[
    "capo_launch_wizard.types.deployment_specifications_field.DeploymentSpecificationsField"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentSpecificationsData) -> list:
    import capo_launch_wizard.types.deployment_specifications_field

    out: list = []
    for item in value:
        out.append(
            capo_launch_wizard.types.deployment_specifications_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DeploymentSpecificationsData:
    import capo_launch_wizard.types.deployment_specifications_field

    out: DeploymentSpecificationsData = []
    for item in data:
        out.append(
            capo_launch_wizard.types.deployment_specifications_field.deserialize_json(
                item
            )
        )
    return out
