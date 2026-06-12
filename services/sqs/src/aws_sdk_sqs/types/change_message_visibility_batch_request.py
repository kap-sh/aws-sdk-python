"""Generated from Smithy shape ``com.amazonaws.sqs#ChangeMessageVisibilityBatchRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.change_message_visibility_batch_request_entry_list
    import aws_sdk_sqs.types.string


class ChangeMessageVisibilityBatchRequest(TypedDict):
    queue_url: "aws_sdk_sqs.types.string.String"
    """<p>The URL of the Amazon SQS queue whose messages' visibility is changed.</p> <p>Queue URLs and names are case-sensitive.</p>"""
    entries: "aws_sdk_sqs.types.change_message_visibility_batch_request_entry_list.ChangeMessageVisibilityBatchRequestEntryList"
    """<p>Lists the receipt handles of the messages for which the visibility timeout must be changed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChangeMessageVisibilityBatchRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    import aws_sdk_sqs.types.change_message_visibility_batch_request_entry_list

    out["Entries"] = (
        aws_sdk_sqs.types.change_message_visibility_batch_request_entry_list.serialize_aws_json_1_0(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ChangeMessageVisibilityBatchRequest:
    out: ChangeMessageVisibilityBatchRequest = {}  # type: ignore[typeddict-item]
    if "QueueUrl" in data:
        out["queue_url"] = data["QueueUrl"]
    else:
        raise DeserializationError(
            "ChangeMessageVisibilityBatchRequest.queue_url required"
        )
    if "Entries" in data:
        import aws_sdk_sqs.types.change_message_visibility_batch_request_entry_list

        out["entries"] = (
            aws_sdk_sqs.types.change_message_visibility_batch_request_entry_list.deserialize_aws_json_1_0(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError(
            "ChangeMessageVisibilityBatchRequest.entries required"
        )
    return out
