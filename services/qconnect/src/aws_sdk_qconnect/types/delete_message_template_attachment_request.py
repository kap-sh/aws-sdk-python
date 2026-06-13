"""Generated from Smithy shape ``com.amazonaws.qconnect#DeleteMessageTemplateAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.uuid
    import aws_sdk_qconnect.types.uuid_or_arn
    import aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier


class DeleteMessageTemplateAttachmentRequest(TypedDict):
    knowledge_base_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    message_template_id: "aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>"""
    attachment_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the attachment file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMessageTemplateAttachmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMessageTemplateAttachmentRequest:
    out: DeleteMessageTemplateAttachmentRequest = {}  # type: ignore[typeddict-item]
    return out
