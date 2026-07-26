"""Generated from Smithy shape ``com.amazonaws.sqs#DeleteMessageBatchRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sqs.types.delete_message_batch_request_entry

DeleteMessageBatchRequestEntryList: TypeAlias = list[
    "capo_sqs.types.delete_message_batch_request_entry.DeleteMessageBatchRequestEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteMessageBatchRequestEntryList) -> list:
    import capo_sqs.types.delete_message_batch_request_entry

    out: list = []
    for item in value:
        out.append(
            capo_sqs.types.delete_message_batch_request_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DeleteMessageBatchRequestEntryList:
    import capo_sqs.types.delete_message_batch_request_entry

    out: DeleteMessageBatchRequestEntryList = []
    for item in data:
        out.append(
            capo_sqs.types.delete_message_batch_request_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
