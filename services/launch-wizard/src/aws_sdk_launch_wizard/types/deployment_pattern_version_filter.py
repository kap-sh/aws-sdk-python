"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentPatternVersionFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_launch_wizard.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_pattern_version_filter_key
    import aws_sdk_launch_wizard.types.deployment_pattern_version_filter_values


class DeploymentPatternVersionFilter(TypedDict):
    name: "aws_sdk_launch_wizard.types.deployment_pattern_version_filter_key.DeploymentPatternVersionFilterKey"
    """<p>The name of the filter attribute. Specifies which attribute to filter on when querying deployment pattern versions.</p>"""
    values: "aws_sdk_launch_wizard.types.deployment_pattern_version_filter_values.DeploymentPatternVersionFilterValues"
    """<p>The values to filter by. Contains the specific values to match against when filtering deployment pattern versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentPatternVersionFilter) -> dict:
    out: dict = {}
    import aws_sdk_launch_wizard.types.deployment_pattern_version_filter_key

    out["name"] = (
        aws_sdk_launch_wizard.types.deployment_pattern_version_filter_key.serialize_json(
            value["name"]
        )
    )
    import aws_sdk_launch_wizard.types.deployment_pattern_version_filter_values

    out["values"] = (
        aws_sdk_launch_wizard.types.deployment_pattern_version_filter_values.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeploymentPatternVersionFilter:
    out: DeploymentPatternVersionFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_launch_wizard.types.deployment_pattern_version_filter_key

        out["name"] = (
            aws_sdk_launch_wizard.types.deployment_pattern_version_filter_key.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("DeploymentPatternVersionFilter.name required")
    if "values" in data:
        import aws_sdk_launch_wizard.types.deployment_pattern_version_filter_values

        out["values"] = (
            aws_sdk_launch_wizard.types.deployment_pattern_version_filter_values.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError("DeploymentPatternVersionFilter.values required")
    return out
