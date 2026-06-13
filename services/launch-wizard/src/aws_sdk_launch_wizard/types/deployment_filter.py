"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_launch_wizard.types.deployment_filter_key
    import aws_sdk_launch_wizard.types.deployment_filter_values


class DeploymentFilter(TypedDict):
    name: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_filter_key.DeploymentFilterKey"
    ]
    """<p>The name of the filter. Filter names are case-sensitive.</p>"""
    values: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_filter_values.DeploymentFilterValues"
    ]
    """<p>The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an <code>OR</code>, and the request returns all results that match any of the specified values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_launch_wizard.types.deployment_filter_key

        out["name"] = aws_sdk_launch_wizard.types.deployment_filter_key.serialize_json(
            value["name"]
        )
    if "values" in value:
        import aws_sdk_launch_wizard.types.deployment_filter_values

        out["values"] = (
            aws_sdk_launch_wizard.types.deployment_filter_values.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeploymentFilter:
    out: DeploymentFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_launch_wizard.types.deployment_filter_key

        out["name"] = (
            aws_sdk_launch_wizard.types.deployment_filter_key.deserialize_json(
                data["name"]
            )
        )
    if "values" in data:
        import aws_sdk_launch_wizard.types.deployment_filter_values

        out["values"] = (
            aws_sdk_launch_wizard.types.deployment_filter_values.deserialize_json(
                data["values"]
            )
        )
    return out
