"""Generated from Smithy shape ``com.amazonaws.datasync#ListTasksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.next_token
    import aws_sdk_datasync.types.task_list


class ListTasksResponse(TypedDict):
    tasks: NotRequired["aws_sdk_datasync.types.task_list.TaskList"]
    """<p>A list of all the tasks that are returned.</p>"""
    next_token: NotRequired["aws_sdk_datasync.types.next_token.NextToken"]
    """<p>An opaque string that indicates the position at which to begin returning the next list of tasks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTasksResponse) -> dict:
    out: dict = {}
    if "tasks" in value:
        import aws_sdk_datasync.types.task_list

        out["Tasks"] = aws_sdk_datasync.types.task_list.serialize_aws_json_1_1(
            value["tasks"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTasksResponse:
    out: ListTasksResponse = {}  # type: ignore[typeddict-item]
    if "Tasks" in data:
        import aws_sdk_datasync.types.task_list

        out["tasks"] = aws_sdk_datasync.types.task_list.deserialize_aws_json_1_1(
            data["Tasks"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
