"""Generated from Smithy shape ``com.amazonaws.sqs#ListMessageMoveTasksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.list_message_move_tasks_result_entry_list


class ListMessageMoveTasksResult(TypedDict, closed=True):
    results: NotRequired[
        "capo_sqs.types.list_message_move_tasks_result_entry_list.ListMessageMoveTasksResultEntryList"
    ]
    """<p>A list of message movement tasks and their attributes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMessageMoveTasksResult) -> dict:
    out: dict = {}
    if "results" in value:
        import capo_sqs.types.list_message_move_tasks_result_entry_list

        out["Results"] = (
            capo_sqs.types.list_message_move_tasks_result_entry_list.serialize_aws_json_1_0(
                value["results"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMessageMoveTasksResult:
    out: ListMessageMoveTasksResult = {}  # type: ignore[typeddict-item]
    if data.get("Results") is not None:
        import capo_sqs.types.list_message_move_tasks_result_entry_list

        out["results"] = (
            capo_sqs.types.list_message_move_tasks_result_entry_list.deserialize_aws_json_1_0(
                data["Results"]
            )
        )
    return out
