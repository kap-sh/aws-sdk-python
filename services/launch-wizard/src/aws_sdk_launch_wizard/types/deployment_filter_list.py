"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_filter

DeploymentFilterList: TypeAlias = list[
    "aws_sdk_launch_wizard.types.deployment_filter.DeploymentFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentFilterList) -> list:
    import aws_sdk_launch_wizard.types.deployment_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_launch_wizard.types.deployment_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeploymentFilterList:
    import aws_sdk_launch_wizard.types.deployment_filter

    out: DeploymentFilterList = []
    for item in data:
        out.append(aws_sdk_launch_wizard.types.deployment_filter.deserialize_json(item))
    return out
