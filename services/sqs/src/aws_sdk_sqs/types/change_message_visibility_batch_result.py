"""Generated from Smithy shape ``com.amazonaws.sqs#ChangeMessageVisibilityBatchResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.batch_result_error_entry_list
    import aws_sdk_sqs.types.change_message_visibility_batch_result_entry_list


class ChangeMessageVisibilityBatchResult(TypedDict, closed=True):
    successful: "aws_sdk_sqs.types.change_message_visibility_batch_result_entry_list.ChangeMessageVisibilityBatchResultEntryList"
    """<p>A list of <code> <a>ChangeMessageVisibilityBatchResultEntry</a> </code> items.</p>"""
    failed: "aws_sdk_sqs.types.batch_result_error_entry_list.BatchResultErrorEntryList"
    """<p>A list of <code> <a>BatchResultErrorEntry</a> </code> items.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChangeMessageVisibilityBatchResult) -> dict:
    out: dict = {}
    import aws_sdk_sqs.types.change_message_visibility_batch_result_entry_list

    out["Successful"] = (
        aws_sdk_sqs.types.change_message_visibility_batch_result_entry_list.serialize_aws_json_1_0(
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


def deserialize_aws_json_1_0(data: dict) -> ChangeMessageVisibilityBatchResult:
    out: ChangeMessageVisibilityBatchResult = {}  # type: ignore[typeddict-item]
    if "Successful" in data:
        import aws_sdk_sqs.types.change_message_visibility_batch_result_entry_list

        out["successful"] = (
            aws_sdk_sqs.types.change_message_visibility_batch_result_entry_list.deserialize_aws_json_1_0(
                data["Successful"]
            )
        )
    else:
        raise DeserializationError(
            "ChangeMessageVisibilityBatchResult.successful required"
        )
    if "Failed" in data:
        import aws_sdk_sqs.types.batch_result_error_entry_list

        out["failed"] = (
            aws_sdk_sqs.types.batch_result_error_entry_list.deserialize_aws_json_1_0(
                data["Failed"]
            )
        )
    else:
        raise DeserializationError("ChangeMessageVisibilityBatchResult.failed required")
    return out
