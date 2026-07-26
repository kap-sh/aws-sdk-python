"""Generated from Smithy shape ``com.amazonaws.sqs#ChangeMessageVisibilityBatchResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sqs.types.change_message_visibility_batch_result_entry

ChangeMessageVisibilityBatchResultEntryList: TypeAlias = list[
    "capo_sqs.types.change_message_visibility_batch_result_entry.ChangeMessageVisibilityBatchResultEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChangeMessageVisibilityBatchResultEntryList) -> list:
    import capo_sqs.types.change_message_visibility_batch_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_sqs.types.change_message_visibility_batch_result_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ChangeMessageVisibilityBatchResultEntryList:
    import capo_sqs.types.change_message_visibility_batch_result_entry

    out: ChangeMessageVisibilityBatchResultEntryList = []
    for item in data:
        out.append(
            capo_sqs.types.change_message_visibility_batch_result_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
