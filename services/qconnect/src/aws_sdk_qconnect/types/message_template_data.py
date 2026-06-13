"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateData``."""

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
    import aws_sdk_qconnect.types.grouping_configuration
    import aws_sdk_qconnect.types.language_code
    import aws_sdk_qconnect.types.message_template_attribute_type_list
    import aws_sdk_qconnect.types.message_template_attributes
    import aws_sdk_qconnect.types.message_template_content_provider
    import aws_sdk_qconnect.types.message_template_content_sha256
    import aws_sdk_qconnect.types.message_template_source_configuration_summary
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid


class MessageTemplateData(TypedDict):
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
    created_time: "datetime.datetime"
    """<p>The timestamp when the message template was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp when the message template data was last modified.</p>"""
    last_modified_by: "aws_sdk_qconnect.types.generic_arn.GenericArn"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the message template data.</p>"""
    content: NotRequired[
        "aws_sdk_qconnect.types.message_template_content_provider.MessageTemplateContentProvider"
    ]
    """<p>The content of the message template.</p>"""
    description: NotRequired["aws_sdk_qconnect.types.description.Description"]
    """<p>The description of the message template.</p>"""
    language: NotRequired["aws_sdk_qconnect.types.language_code.LanguageCode"]
    """<p>The language code value for the language in which the quick response is written. The supported language codes include <code>de_DE</code>, <code>en_US</code>, <code>es_ES</code>, <code>fr_FR</code>, <code>id_ID</code>, <code>it_IT</code>, <code>ja_JP</code>, <code>ko_KR</code>, <code>pt_BR</code>, <code>zh_CN</code>, <code>zh_TW</code> </p>"""
    source_configuration_summary: NotRequired[
        "aws_sdk_qconnect.types.message_template_source_configuration_summary.MessageTemplateSourceConfigurationSummary"
    ]
    """<p>The source configuration summary of the message template.</p>"""
    grouping_configuration: NotRequired[
        "aws_sdk_qconnect.types.grouping_configuration.GroupingConfiguration"
    ]
    default_attributes: NotRequired[
        "aws_sdk_qconnect.types.message_template_attributes.MessageTemplateAttributes"
    ]
    """<p>An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.</p>"""
    attribute_types: NotRequired[
        "aws_sdk_qconnect.types.message_template_attribute_type_list.MessageTemplateAttributeTypeList"
    ]
    """<p>The types of attributes that the message template contains.</p>"""
    message_template_content_sha256: "aws_sdk_qconnect.types.message_template_content_sha256.MessageTemplateContentSha256"
    """<p>The checksum value of the message template content that is referenced by the <code>$LATEST</code> qualifier. It can be returned in <code>MessageTemplateData</code> or <code>ExtendedMessageTemplateData</code>. It’s calculated by content, language, <code>defaultAttributes</code> and <code>Attachments</code> of the message template.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateData) -> dict:
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
    if "content" in value:
        import aws_sdk_qconnect.types.message_template_content_provider

        out["content"] = (
            aws_sdk_qconnect.types.message_template_content_provider.serialize_json(
                value["content"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "language" in value:
        out["language"] = value["language"]
    if "source_configuration_summary" in value:
        import aws_sdk_qconnect.types.message_template_source_configuration_summary

        out["sourceConfigurationSummary"] = (
            aws_sdk_qconnect.types.message_template_source_configuration_summary.serialize_json(
                value["source_configuration_summary"]
            )
        )
    if "grouping_configuration" in value:
        import aws_sdk_qconnect.types.grouping_configuration

        out["groupingConfiguration"] = (
            aws_sdk_qconnect.types.grouping_configuration.serialize_json(
                value["grouping_configuration"]
            )
        )
    if "default_attributes" in value:
        import aws_sdk_qconnect.types.message_template_attributes

        out["defaultAttributes"] = (
            aws_sdk_qconnect.types.message_template_attributes.serialize_json(
                value["default_attributes"]
            )
        )
    if "attribute_types" in value:
        import aws_sdk_qconnect.types.message_template_attribute_type_list

        out["attributeTypes"] = (
            aws_sdk_qconnect.types.message_template_attribute_type_list.serialize_json(
                value["attribute_types"]
            )
        )
    out["messageTemplateContentSha256"] = value["message_template_content_sha256"]
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> MessageTemplateData:
    out: MessageTemplateData = {}  # type: ignore[typeddict-item]
    if "messageTemplateArn" in data:
        out["message_template_arn"] = data["messageTemplateArn"]
    else:
        raise DeserializationError("MessageTemplateData.message_template_arn required")
    if "messageTemplateId" in data:
        out["message_template_id"] = data["messageTemplateId"]
    else:
        raise DeserializationError("MessageTemplateData.message_template_id required")
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError("MessageTemplateData.knowledge_base_arn required")
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError("MessageTemplateData.knowledge_base_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("MessageTemplateData.name required")
    if "channel" in data:
        out["channel"] = data["channel"]
    if "channelSubtype" in data:
        out["channel_subtype"] = data["channelSubtype"]
    else:
        raise DeserializationError("MessageTemplateData.channel_subtype required")
    if "createdTime" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["created_time"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["createdTime"]
            )
        )
    else:
        raise DeserializationError("MessageTemplateData.created_time required")
    if "lastModifiedTime" in data:
        import aws_sdk_qconnect.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_qconnect.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("MessageTemplateData.last_modified_time required")
    if "lastModifiedBy" in data:
        out["last_modified_by"] = data["lastModifiedBy"]
    else:
        raise DeserializationError("MessageTemplateData.last_modified_by required")
    if "content" in data:
        import aws_sdk_qconnect.types.message_template_content_provider

        out["content"] = (
            aws_sdk_qconnect.types.message_template_content_provider.deserialize_json(
                data["content"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "language" in data:
        out["language"] = data["language"]
    if "sourceConfigurationSummary" in data:
        import aws_sdk_qconnect.types.message_template_source_configuration_summary

        out["source_configuration_summary"] = (
            aws_sdk_qconnect.types.message_template_source_configuration_summary.deserialize_json(
                data["sourceConfigurationSummary"]
            )
        )
    if "groupingConfiguration" in data:
        import aws_sdk_qconnect.types.grouping_configuration

        out["grouping_configuration"] = (
            aws_sdk_qconnect.types.grouping_configuration.deserialize_json(
                data["groupingConfiguration"]
            )
        )
    if "defaultAttributes" in data:
        import aws_sdk_qconnect.types.message_template_attributes

        out["default_attributes"] = (
            aws_sdk_qconnect.types.message_template_attributes.deserialize_json(
                data["defaultAttributes"]
            )
        )
    if "attributeTypes" in data:
        import aws_sdk_qconnect.types.message_template_attribute_type_list

        out["attribute_types"] = (
            aws_sdk_qconnect.types.message_template_attribute_type_list.deserialize_json(
                data["attributeTypes"]
            )
        )
    if "messageTemplateContentSha256" in data:
        out["message_template_content_sha256"] = data["messageTemplateContentSha256"]
    else:
        raise DeserializationError(
            "MessageTemplateData.message_template_content_sha256 required"
        )
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    return out
