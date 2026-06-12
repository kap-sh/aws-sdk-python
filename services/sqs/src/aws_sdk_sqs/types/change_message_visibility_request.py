"""Generated from Smithy shape ``com.amazonaws.sqs#ChangeMessageVisibilityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.nullable_integer
    import aws_sdk_sqs.types.string


class ChangeMessageVisibilityRequest(TypedDict):
    queue_url: "aws_sdk_sqs.types.string.String"
    """<p>The URL of the Amazon SQS queue whose message's visibility is changed.</p> <p>Queue URLs and names are case-sensitive.</p>"""
    receipt_handle: "aws_sdk_sqs.types.string.String"
    """<p>The receipt handle associated with the message, whose visibility timeout is changed. This parameter is returned by the <code> <a>ReceiveMessage</a> </code> action.</p>"""
    visibility_timeout: "aws_sdk_sqs.types.nullable_integer.NullableInteger"
    """<p>The new value for the message's visibility timeout (in seconds). Values range: <code>0</code> to <code>43200</code>. Maximum: 12 hours.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChangeMessageVisibilityRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    out["ReceiptHandle"] = value["receipt_handle"]
    out["VisibilityTimeout"] = value["visibility_timeout"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ChangeMessageVisibilityRequest:
    out: ChangeMessageVisibilityRequest = {}  # type: ignore[typeddict-item]
    if "QueueUrl" in data:
        out["queue_url"] = data["QueueUrl"]
    else:
        raise DeserializationError("ChangeMessageVisibilityRequest.queue_url required")
    if "ReceiptHandle" in data:
        out["receipt_handle"] = data["ReceiptHandle"]
    else:
        raise DeserializationError(
            "ChangeMessageVisibilityRequest.receipt_handle required"
        )
    if "VisibilityTimeout" in data:
        out["visibility_timeout"] = data["VisibilityTimeout"]
    else:
        raise DeserializationError(
            "ChangeMessageVisibilityRequest.visibility_timeout required"
        )
    return out
