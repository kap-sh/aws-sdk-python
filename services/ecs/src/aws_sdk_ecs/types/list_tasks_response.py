"""Generated from Smithy shape ``com.amazonaws.ecs#ListTasksResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class ListTasksResponse(TypedDict):
    task_arns: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The list of task ARN entries for the <code>ListTasks</code> request.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListTasks</code> request. When the results of a <code>ListTasks</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTasksResponse) -> dict:
    out: dict = {}
    if "task_arns" in value:
        import aws_sdk_ecs.types.string_list

        out["taskArns"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["task_arns"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTasksResponse:
    out: ListTasksResponse = {}  # type: ignore[typeddict-item]
    if "taskArns" in data:
        import aws_sdk_ecs.types.string_list

        out["task_arns"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["taskArns"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
