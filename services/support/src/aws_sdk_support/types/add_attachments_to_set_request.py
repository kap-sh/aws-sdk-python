"""Generated from Smithy shape ``com.amazonaws.support#AddAttachmentsToSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.attachment_set_id
    import aws_sdk_support.types.attachments


class AddAttachmentsToSetRequest(TypedDict):
    attachment_set_id: NotRequired[
        "aws_sdk_support.types.attachment_set_id.AttachmentSetId"
    ]
    """<p>The ID of the attachment set. If an <code>attachmentSetId</code> is not specified, a new attachment set is created, and the ID of the set is returned in the response. If an <code>attachmentSetId</code> is specified, the attachments are added to the specified set, if it exists.</p>"""
    attachments: "aws_sdk_support.types.attachments.Attachments"
    """<p>One or more attachments to add to the set. You can add up to three attachments per set. The size limit is 5 MB per attachment.</p> <p>In the <code>Attachment</code> object, use the <code>data</code> parameter to specify the contents of the attachment file. In the previous request syntax, the value for <code>data</code> appear as <code>blob</code>, which is represented as a base64-encoded string. The value for <code>fileName</code> is the name of the attachment, such as <code>troubleshoot-screenshot.png</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddAttachmentsToSetRequest) -> dict:
    out: dict = {}
    if "attachment_set_id" in value:
        out["attachmentSetId"] = value["attachment_set_id"]
    import aws_sdk_support.types.attachments

    out["attachments"] = aws_sdk_support.types.attachments.serialize_aws_json_1_1(
        value["attachments"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddAttachmentsToSetRequest:
    out: AddAttachmentsToSetRequest = {}  # type: ignore[typeddict-item]
    if "attachmentSetId" in data:
        out["attachment_set_id"] = data["attachmentSetId"]
    if "attachments" in data:
        import aws_sdk_support.types.attachments

        out["attachments"] = aws_sdk_support.types.attachments.deserialize_aws_json_1_1(
            data["attachments"]
        )
    else:
        raise DeserializationError("AddAttachmentsToSetRequest.attachments required")
    return out
