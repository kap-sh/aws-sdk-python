"""Generated from Smithy shape ``com.amazonaws.sqs#BatchResultErrorEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.boolean
    import aws_sdk_sqs.types.string


class BatchResultErrorEntry(TypedDict):
    id: "aws_sdk_sqs.types.string.String"
    """<p>The <code>Id</code> of an entry in a batch request.</p>"""
    sender_fault: "aws_sdk_sqs.types.boolean.Boolean"
    """<p>Specifies whether the error happened due to the caller of the batch API action.</p>"""
    code: "aws_sdk_sqs.types.string.String"
    """<p>An error code representing why the action failed on this entry.</p>"""
    message: NotRequired["aws_sdk_sqs.types.string.String"]
    """<p>A message explaining why the action failed on this entry.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchResultErrorEntry) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["SenderFault"] = value.get("sender_fault", False)
    out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchResultErrorEntry:
    out: BatchResultErrorEntry = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("BatchResultErrorEntry.id required")
    if "SenderFault" in data:
        out["sender_fault"] = data["SenderFault"]
    else:
        out["sender_fault"] = False
    if "Code" in data:
        out["code"] = data["Code"]
    else:
        raise DeserializationError("BatchResultErrorEntry.code required")
    if "Message" in data:
        out["message"] = data["Message"]
    return out
