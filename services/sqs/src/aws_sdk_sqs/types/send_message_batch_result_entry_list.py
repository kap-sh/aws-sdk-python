"""Generated from Smithy shape ``com.amazonaws.sqs#SendMessageBatchResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sqs.types.send_message_batch_result_entry

SendMessageBatchResultEntryList: TypeAlias = list[
    "aws_sdk_sqs.types.send_message_batch_result_entry.SendMessageBatchResultEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendMessageBatchResultEntryList) -> list:
    import aws_sdk_sqs.types.send_message_batch_result_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sqs.types.send_message_batch_result_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SendMessageBatchResultEntryList:
    import aws_sdk_sqs.types.send_message_batch_result_entry

    out: SendMessageBatchResultEntryList = []
    for item in data:
        out.append(
            aws_sdk_sqs.types.send_message_batch_result_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
