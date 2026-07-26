"""Generated from Smithy shape ``com.amazonaws.sqs#ListMessageMoveTasksResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sqs.types.list_message_move_tasks_result_entry

ListMessageMoveTasksResultEntryList: TypeAlias = list[
    "capo_sqs.types.list_message_move_tasks_result_entry.ListMessageMoveTasksResultEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMessageMoveTasksResultEntryList) -> list:
    import capo_sqs.types.list_message_move_tasks_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_sqs.types.list_message_move_tasks_result_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListMessageMoveTasksResultEntryList:
    import capo_sqs.types.list_message_move_tasks_result_entry

    out: ListMessageMoveTasksResultEntryList = []
    for item in data:
        out.append(
            capo_sqs.types.list_message_move_tasks_result_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
