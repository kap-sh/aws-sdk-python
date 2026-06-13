"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_filter_value

DeploymentFilterValues: TypeAlias = list[
    "aws_sdk_launch_wizard.types.deployment_filter_value.DeploymentFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> DeploymentFilterValues:
    return list(data)
