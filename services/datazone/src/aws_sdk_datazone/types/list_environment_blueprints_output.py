"""Generated from Smithy shape ``com.amazonaws.datazone#ListEnvironmentBlueprintsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.environment_blueprint_summaries
    import aws_sdk_datazone.types.pagination_token


class ListEnvironmentBlueprintsOutput(TypedDict, closed=True):
    items: "aws_sdk_datazone.types.environment_blueprint_summaries.EnvironmentBlueprintSummaries"
    """<p>The results of the <code>ListEnvironmentBlueprints</code> action.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of blueprints in the environment is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of blueprints in the environment, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentBlueprints</code>to list the next set of blueprints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentBlueprintsOutput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.environment_blueprint_summaries

    out["items"] = (
        aws_sdk_datazone.types.environment_blueprint_summaries.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnvironmentBlueprintsOutput:
    out: ListEnvironmentBlueprintsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_datazone.types.environment_blueprint_summaries

        out["items"] = (
            aws_sdk_datazone.types.environment_blueprint_summaries.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError("ListEnvironmentBlueprintsOutput.items required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
