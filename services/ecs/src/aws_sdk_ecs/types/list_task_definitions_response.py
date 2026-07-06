"""Generated from Smithy shape ``com.amazonaws.ecs#ListTaskDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class ListTaskDefinitionsResponse(TypedDict, closed=True):
    task_definition_arns: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The list of task definition Amazon Resource Name (ARN) entries for the <code>ListTaskDefinitions</code> request.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListTaskDefinitions</code> request. When the results of a <code>ListTaskDefinitions</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTaskDefinitionsResponse) -> dict:
    out: dict = {}
    if "task_definition_arns" in value:
        import aws_sdk_ecs.types.string_list

        out["taskDefinitionArns"] = (
            aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
                value["task_definition_arns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTaskDefinitionsResponse:
    out: ListTaskDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "taskDefinitionArns" in data:
        import aws_sdk_ecs.types.string_list

        out["task_definition_arns"] = (
            aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
                data["taskDefinitionArns"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
