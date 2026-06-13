"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateVersionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.arn_with_qualifier
    import aws_sdk_qconnect.types.channel
    import aws_sdk_qconnect.types.channel_subtype
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.uuid
    import aws_sdk_qconnect.types.version


class MessageTemplateVersionSummary(TypedDict):
    message_template_arn: "aws_sdk_qconnect.types.arn_with_qualifier.ArnWithQualifier"
    """<p>The Amazon Resource Name (ARN) of the message template.</p>"""
    message_template_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the message template.</p>"""
    knowledge_base_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the knowledge base.</p>"""
    name: "aws_sdk_qconnect.types.name.Name"
    """<p>The name of the message template.</p>"""
    channel: NotRequired["aws_sdk_qconnect.types.channel.Channel"]
    """<p>The channel of the message template.</p>"""
    channel_subtype: "aws_sdk_qconnect.types.channel_subtype.ChannelSubtype"
    """<p>The channel subtype this message template applies to.</p>"""
    is_active: "bool"
    """<p>Whether the version of the message template is activated.</p>"""
    version_number: "aws_sdk_qconnect.types.version.Version"
    """<p>The version number of the message template version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateVersionSummary) -> dict:
    out: dict = {}
    out["messageTemplateArn"] = value["message_template_arn"]
    out["messageTemplateId"] = value["message_template_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["name"] = value["name"]
    if "channel" in value:
        out["channel"] = value["channel"]
    out["channelSubtype"] = value["channel_subtype"]
    out["isActive"] = value["is_active"]
    out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> MessageTemplateVersionSummary:
    out: MessageTemplateVersionSummary = {}  # type: ignore[typeddict-item]
    if "messageTemplateArn" in data:
        out["message_template_arn"] = data["messageTemplateArn"]
    else:
        raise DeserializationError(
            "MessageTemplateVersionSummary.message_template_arn required"
        )
    if "messageTemplateId" in data:
        out["message_template_id"] = data["messageTemplateId"]
    else:
        raise DeserializationError(
            "MessageTemplateVersionSummary.message_template_id required"
        )
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError(
            "MessageTemplateVersionSummary.knowledge_base_arn required"
        )
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError(
            "MessageTemplateVersionSummary.knowledge_base_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("MessageTemplateVersionSummary.name required")
    if "channel" in data:
        out["channel"] = data["channel"]
    if "channelSubtype" in data:
        out["channel_subtype"] = data["channelSubtype"]
    else:
        raise DeserializationError(
            "MessageTemplateVersionSummary.channel_subtype required"
        )
    if "isActive" in data:
        out["is_active"] = data["isActive"]
    else:
        raise DeserializationError("MessageTemplateVersionSummary.is_active required")
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    else:
        raise DeserializationError(
            "MessageTemplateVersionSummary.version_number required"
        )
    return out
