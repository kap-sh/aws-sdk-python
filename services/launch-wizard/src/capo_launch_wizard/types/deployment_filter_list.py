"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_filter

DeploymentFilterList: TypeAlias = list[
    "capo_launch_wizard.types.deployment_filter.DeploymentFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentFilterList) -> list:
    import capo_launch_wizard.types.deployment_filter

    out: list = []
    for item in value:
        out.append(capo_launch_wizard.types.deployment_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeploymentFilterList:
    import capo_launch_wizard.types.deployment_filter

    out: DeploymentFilterList = []
    for item in data:
        out.append(capo_launch_wizard.types.deployment_filter.deserialize_json(item))
    return out
