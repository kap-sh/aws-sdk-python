"""Generated from Smithy shape ``com.amazonaws.datazone#ListEnvironmentBlueprintConfigurationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.environment_blueprint_configurations
    import aws_sdk_datazone.types.pagination_token


class ListEnvironmentBlueprintConfigurationsOutput(TypedDict):
    items: NotRequired[
        "aws_sdk_datazone.types.environment_blueprint_configurations.EnvironmentBlueprintConfigurations"
    ]
    """<p>The results of the <code>ListEnvironmentBlueprintConfigurations</code> action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of blueprint configurations is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of configurations, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentBlueprintConfigurations</code> to list the next set of configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentBlueprintConfigurationsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_datazone.types.environment_blueprint_configurations

        out["items"] = (
            aws_sdk_datazone.types.environment_blueprint_configurations.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnvironmentBlueprintConfigurationsOutput:
    out: ListEnvironmentBlueprintConfigurationsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.environment_blueprint_configurations

        out["items"] = (
            aws_sdk_datazone.types.environment_blueprint_configurations.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
