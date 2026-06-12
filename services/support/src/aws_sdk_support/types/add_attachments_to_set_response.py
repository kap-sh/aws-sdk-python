"""Generated from Smithy shape ``com.amazonaws.support#AddAttachmentsToSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_support.types.attachment_set_id
    import aws_sdk_support.types.expiry_time


class AddAttachmentsToSetResponse(TypedDict):
    attachment_set_id: NotRequired[
        "aws_sdk_support.types.attachment_set_id.AttachmentSetId"
    ]
    """<p>The ID of the attachment set. If an <code>attachmentSetId</code> was not specified, a new attachment set is created, and the ID of the set is returned in the response. If an <code>attachmentSetId</code> was specified, the attachments are added to the specified set, if it exists.</p>"""
    expiry_time: NotRequired["aws_sdk_support.types.expiry_time.ExpiryTime"]
    """<p>The time and date when the attachment set expires.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddAttachmentsToSetResponse) -> dict:
    out: dict = {}
    if "attachment_set_id" in value:
        out["attachmentSetId"] = value["attachment_set_id"]
    if "expiry_time" in value:
        out["expiryTime"] = value["expiry_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddAttachmentsToSetResponse:
    out: AddAttachmentsToSetResponse = {}  # type: ignore[typeddict-item]
    if "attachmentSetId" in data:
        out["attachment_set_id"] = data["attachmentSetId"]
    if "expiryTime" in data:
        out["expiry_time"] = data["expiryTime"]
    return out
