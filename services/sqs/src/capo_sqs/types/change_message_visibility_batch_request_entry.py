"""Generated from Smithy shape ``com.amazonaws.sqs#ChangeMessageVisibilityBatchRequestEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sqs.types.nullable_integer
    import capo_sqs.types.string


class ChangeMessageVisibilityBatchRequestEntry(TypedDict, closed=True):
    id: "capo_sqs.types.string.String"
    """<p>An identifier for this particular receipt handle used to communicate the result.</p> <note> <p>The <code>Id</code>s of a batch request need to be unique within a request.</p> <p>This identifier can have up to 80 characters. The following characters are accepted: alphanumeric characters, hyphens(-), and underscores (_).</p> </note>"""
    receipt_handle: "capo_sqs.types.string.String"
    """<p>A receipt handle.</p>"""
    visibility_timeout: NotRequired["capo_sqs.types.nullable_integer.NullableInteger"]
    """<p>The new value (in seconds) for the message's visibility timeout.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChangeMessageVisibilityBatchRequestEntry) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["ReceiptHandle"] = value["receipt_handle"]
    if "visibility_timeout" in value:
        out["VisibilityTimeout"] = value["visibility_timeout"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ChangeMessageVisibilityBatchRequestEntry:
    out: ChangeMessageVisibilityBatchRequestEntry = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError(
            "ChangeMessageVisibilityBatchRequestEntry.id required"
        )
    if "ReceiptHandle" in data:
        out["receipt_handle"] = data["ReceiptHandle"]
    else:
        raise DeserializationError(
            "ChangeMessageVisibilityBatchRequestEntry.receipt_handle required"
        )
    if "VisibilityTimeout" in data:
        out["visibility_timeout"] = data["VisibilityTimeout"]
    return out
