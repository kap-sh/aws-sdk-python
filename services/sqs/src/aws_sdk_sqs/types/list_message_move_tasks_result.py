"""Generated from Smithy shape ``com.amazonaws.sqs#ListMessageMoveTasksResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sqs.types.list_message_move_tasks_result_entry_list


class ListMessageMoveTasksResult(TypedDict):
    results: NotRequired[
        "aws_sdk_sqs.types.list_message_move_tasks_result_entry_list.ListMessageMoveTasksResultEntryList"
    ]
    """<p>A list of message movement tasks and their attributes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMessageMoveTasksResult) -> dict:
    out: dict = {}
    if "results" in value:
        import aws_sdk_sqs.types.list_message_move_tasks_result_entry_list

        out["Results"] = (
            aws_sdk_sqs.types.list_message_move_tasks_result_entry_list.serialize_aws_json_1_0(
                value["results"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMessageMoveTasksResult:
    out: ListMessageMoveTasksResult = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_sqs.types.list_message_move_tasks_result_entry_list

        out["results"] = (
            aws_sdk_sqs.types.list_message_move_tasks_result_entry_list.deserialize_aws_json_1_0(
                data["Results"]
            )
        )
    return out
