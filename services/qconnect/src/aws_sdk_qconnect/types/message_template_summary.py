"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.arn_with_qualifier
    import aws_sdk_qconnect.types.channel
    import aws_sdk_qconnect.types.channel_subtype
    import aws_sdk_qconnect.types.description
    import aws_sdk_qconnect.types.generic_arn
    import aws_sdk_qconnect.types.message_template_source_configuration
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid
    import aws_sdk_qconnect.types.version


class MessageTemplateSummary(TypedDict):
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
    """<p>The channel this message template applies to.</p>"""
    channel_subtype: "aws_sdk_qconnect.types.channel_subtype.ChannelSubtype"
    """<p>The channel subtype this message template applies to.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the message template was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp when the message template data was last modified.</p>"""
    last_modified_by: "aws_sdk_qconnect.types.generic_arn.GenericArn"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the message template data.</p>"""
    source_configuration: NotRequired[
        "aws_sdk_qconnect.types.message_template_source_configuration.MessageTemplateSourceConfiguration"
    ]
    active_version_number: NotRequired["aws_sdk_qconnect.types.version.Version"]
    """<p>The version number of the message template version that is activated.</p>"""
    description: NotRequired["aws_sdk_qconnect.types.description.Description"]
    """<p>The description of the message template.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateSummary) -> dict:
    out: dict = {}
    out["messageTemplateArn"] = value["message_template_arn"]
    out["messageTemplateId"] = value["message_template_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["name"] = value["name"]
    if "channel" in value:
        out["channel"] = value["channel"]
    out["channelSubtype"] = value["channel_subtype"]
    import aws_sdk_qconnect.types._prelude.timestamp

    out["createdTime"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
        value["created_time"]
    )
    import aws_sdk_qconnect.types._prelude.timestamp

    out["lastModifiedTime"] = aws_sdk_qconnect.types._prelude.timestamp.serialize_json(
        value["last_modified_time"]
    )
    out["lastModifiedBy"] = value["last_modified_by"]
    if "source_configuration" in value:
        import aws_sdk_qconnect.types.message_template_source_configuration

        out["sourceConfiguration"] = (
            aws_sdk_qconnect.types.message_template_source_configuration.serialize_json(
                value["source_configuration"]
            )
        )
    if "active_version_number" in value:
        out["activeVersionNumber"] = value["active_version_number"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> MessageTemplateSummary:
    out: MessageTemplateSummary = {}  # type: ignore[typeddict-item]
    if "messageTemplateArn" in data:
        out["message_template_arn"] = data["messageTemplateArn"]
    else:
        raise DeserializationError(
            "MessageTemplateSummary.message_template_arn required"
        )
    if "messageTemplateId" in data:
        out["message_template_id"] = data["messageTemplateId"]
    else:
        raise DeserializationError(
            "MessageTemplateSummary.message_template_id required"
        )
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("MessageTemplateSummary.knowledge_base_arn required")
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("MessageTemplateSummary.knowledge_base_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("MessageTemplateSummary.name required")
    if "channel" in data:
        out["channel"] = data["channel"]
    if "channelSubtype" in data:
        out["channel_subtype"] = data["channelSubtype"]
    else:
        raise DeserializationError("MessageTemplateSummary.channel_subtype required")
    if "createdTime" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["created_time"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        raise DeserializationError("MessageTemplateSummary.created_time required")
    if "lastModifiedTime" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("MessageTemplateSummary.last_modified_time required")
    if "lastModifiedBy" in data:
        out["last_modified_by"] = data["lastModifiedBy"]
    else:
        raise DeserializationError("MessageTemplateSummary.last_modified_by required")
    if "sourceConfiguration" in data:
        import aws_sdk_qconnect.types.message_template_source_configuration

        out["source_configuration"] = (
            aws_sdk_qconnect.types.message_template_source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    if "activeVersionNumber" in data:
        out["active_version_number"] = data["activeVersionNumber"]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    return out
