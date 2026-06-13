"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentPatternVersionFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_pattern_version_filter_value

DeploymentPatternVersionFilterValues: TypeAlias = list[
    "aws_sdk_launch_wizard.types.deployment_pattern_version_filter_value.DeploymentPatternVersionFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentPatternVersionFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> DeploymentPatternVersionFilterValues:
    return list(data)
