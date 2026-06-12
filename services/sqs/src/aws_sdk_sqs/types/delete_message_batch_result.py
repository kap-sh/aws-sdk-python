"""Generated from Smithy shape ``com.amazonaws.sqs#DeleteMessageBatchResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.batch_result_error_entry_list
    import aws_sdk_sqs.types.delete_message_batch_result_entry_list


class DeleteMessageBatchResult(TypedDict):
    successful: "aws_sdk_sqs.types.delete_message_batch_result_entry_list.DeleteMessageBatchResultEntryList"
    """<p>A list of <code> <a>DeleteMessageBatchResultEntry</a> </code> items.</p>"""
    failed: "aws_sdk_sqs.types.batch_result_error_entry_list.BatchResultErrorEntryList"
    """<p>A list of <code> <a>BatchResultErrorEntry</a> </code> items.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteMessageBatchResult) -> dict:
    out: dict = {}
    import aws_sdk_sqs.types.delete_message_batch_result_entry_list

    out["Successful"] = (
        aws_sdk_sqs.types.delete_message_batch_result_entry_list.serialize_aws_json_1_0(
            value["successful"]
        )
    )
    import aws_sdk_sqs.types.batch_result_error_entry_list

    out["Failed"] = (
        aws_sdk_sqs.types.batch_result_error_entry_list.serialize_aws_json_1_0(
            value["failed"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteMessageBatchResult:
    out: DeleteMessageBatchResult = {}  # type: ignore[typeddict-item]
    if "Successful" in data:
        import aws_sdk_sqs.types.delete_message_batch_result_entry_list

        out["successful"] = (
            aws_sdk_sqs.types.delete_message_batch_result_entry_list.deserialize_aws_json_1_0(
                data["Successful"]
            )
        )
    else:
        raise DeserializationError("DeleteMessageBatchResult.successful required")
    if "Failed" in data:
        import aws_sdk_sqs.types.batch_result_error_entry_list

        out["failed"] = (
            aws_sdk_sqs.types.batch_result_error_entry_list.deserialize_aws_json_1_0(
                data["Failed"]
            )
        )
    else:
        raise DeserializationError("DeleteMessageBatchResult.failed required")
    return out
