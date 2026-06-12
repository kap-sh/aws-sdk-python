"""Generated from Smithy shape ``com.amazonaws.sqs#ChangeMessageVisibilityBatchRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sqs.types.change_message_visibility_batch_request_entry

ChangeMessageVisibilityBatchRequestEntryList: TypeAlias = list[
    "aws_sdk_sqs.types.change_message_visibility_batch_request_entry.ChangeMessageVisibilityBatchRequestEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChangeMessageVisibilityBatchRequestEntryList) -> list:
    import aws_sdk_sqs.types.change_message_visibility_batch_request_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sqs.types.change_message_visibility_batch_request_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> ChangeMessageVisibilityBatchRequestEntryList:
    import aws_sdk_sqs.types.change_message_visibility_batch_request_entry

    out: ChangeMessageVisibilityBatchRequestEntryList = []
    for item in data:
        out.append(
            aws_sdk_sqs.types.change_message_visibility_batch_request_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
