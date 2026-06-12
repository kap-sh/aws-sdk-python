"""Generated from Smithy shape ``com.amazonaws.sqs#DeleteMessageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.string


class DeleteMessageRequest(TypedDict):
    queue_url: "aws_sdk_sqs.types.string.String"
    """<p>The URL of the Amazon SQS queue from which messages are deleted.</p> <p>Queue URLs and names are case-sensitive.</p>"""
    receipt_handle: "aws_sdk_sqs.types.string.String"
    """<p>The receipt handle associated with the message to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteMessageRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    out["ReceiptHandle"] = value["receipt_handle"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteMessageRequest:
    out: DeleteMessageRequest = {}  # type: ignore[typeddict-item]
    if "QueueUrl" in data:
        out["queue_url"] = data["QueueUrl"]
    else:
        raise DeserializationError("DeleteMessageRequest.queue_url required")
    if "ReceiptHandle" in data:
        out["receipt_handle"] = data["ReceiptHandle"]
    else:
        raise DeserializationError("DeleteMessageRequest.receipt_handle required")
    return out
