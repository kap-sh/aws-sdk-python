"""Generated from Smithy shape ``com.amazonaws.sqs#SendMessageBatchRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sqs.types.send_message_batch_request_entry

SendMessageBatchRequestEntryList: TypeAlias = list[
    "capo_sqs.types.send_message_batch_request_entry.SendMessageBatchRequestEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendMessageBatchRequestEntryList) -> list:
    import capo_sqs.types.send_message_batch_request_entry

    out: list = []
    for item in value:
        out.append(
            capo_sqs.types.send_message_batch_request_entry.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SendMessageBatchRequestEntryList:
    import capo_sqs.types.send_message_batch_request_entry

    out: SendMessageBatchRequestEntryList = []
    for item in data:
        out.append(
            capo_sqs.types.send_message_batch_request_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
