"""Generated from Smithy shape ``com.amazonaws.support#DescribeAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.attachment_id


class DescribeAttachmentRequest(TypedDict, closed=True):
    attachment_id: "aws_sdk_support.types.attachment_id.AttachmentId"
    """<p>The ID of the attachment to return. Attachment IDs are returned by the <a>DescribeCommunications</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAttachmentRequest) -> dict:
    out: dict = {}
    out["attachmentId"] = value["attachment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAttachmentRequest:
    out: DescribeAttachmentRequest = {}  # type: ignore[typeddict-item]
    if "attachmentId" in data:
        out["attachment_id"] = data["attachmentId"]
    else:
        raise DeserializationError("DescribeAttachmentRequest.attachment_id required")
    return out
