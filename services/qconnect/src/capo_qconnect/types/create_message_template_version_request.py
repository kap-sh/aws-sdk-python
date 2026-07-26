"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateMessageTemplateVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_content_sha256
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier


class CreateMessageTemplateVersionRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>"""
    message_template_content_sha256: NotRequired[
        "capo_qconnect.types.message_template_content_sha256.MessageTemplateContentSha256"
    ]
    """<p>The checksum value of the message template content that is referenced by the <code>$LATEST</code> qualifier. It can be returned in <code>MessageTemplateData</code> or <code>ExtendedMessageTemplateData</code>. It’s calculated by content, language, <code>defaultAttributes</code> and <code>Attachments</code> of the message template. If not supplied, the message template version will be created based on the message template content that is referenced by the <code>$LATEST</code> qualifier by default.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMessageTemplateVersionRequest) -> dict:
    out: dict = {}
    if "message_template_content_sha256" in value:
        out["messageTemplateContentSha256"] = value["message_template_content_sha256"]
    return out


def deserialize_json(data: dict) -> CreateMessageTemplateVersionRequest:
    out: CreateMessageTemplateVersionRequest = {}  # type: ignore[typeddict-item]
    if "messageTemplateContentSha256" in data:
        out["message_template_content_sha256"] = data["messageTemplateContentSha256"]
    return out
