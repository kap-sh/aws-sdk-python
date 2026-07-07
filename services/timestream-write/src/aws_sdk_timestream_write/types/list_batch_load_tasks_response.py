"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#ListBatchLoadTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.batch_load_task_list
    import aws_sdk_timestream_write.types.string


class ListBatchLoadTasksResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_timestream_write.types.string.String"]
    """<p>A token to specify where to start paginating. Provide the next ListBatchLoadTasksRequest.</p>"""
    batch_load_tasks: NotRequired[
        "aws_sdk_timestream_write.types.batch_load_task_list.BatchLoadTaskList"
    ]
    """<p>A list of batch load task details.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBatchLoadTasksResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "batch_load_tasks" in value:
        import aws_sdk_timestream_write.types.batch_load_task_list

        out["BatchLoadTasks"] = (
            aws_sdk_timestream_write.types.batch_load_task_list.serialize_aws_json_1_0(
                value["batch_load_tasks"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBatchLoadTasksResponse:
    out: ListBatchLoadTasksResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "BatchLoadTasks" in data:
        import aws_sdk_timestream_write.types.batch_load_task_list

        out["batch_load_tasks"] = (
            aws_sdk_timestream_write.types.batch_load_task_list.deserialize_aws_json_1_0(
                data["BatchLoadTasks"]
            )
        )
    return out
