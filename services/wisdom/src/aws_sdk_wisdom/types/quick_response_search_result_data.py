"""Generated from Smithy shape ``com.amazonaws.wisdom#QuickResponseSearchResultData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_wisdom.types.arn
    import aws_sdk_wisdom.types.channels
    import aws_sdk_wisdom.types.contact_attribute_keys
    import aws_sdk_wisdom.types.generic_arn
    import aws_sdk_wisdom.types.grouping_configuration
    import aws_sdk_wisdom.types.language_code
    import aws_sdk_wisdom.types.quick_response_contents
    import aws_sdk_wisdom.types.quick_response_description
    import aws_sdk_wisdom.types.quick_response_name
    import aws_sdk_wisdom.types.quick_response_status
    import aws_sdk_wisdom.types.quick_response_type
    import aws_sdk_wisdom.types.short_cut_key
    import aws_sdk_wisdom.types.tags
    import aws_sdk_wisdom.types.uuid


class QuickResponseSearchResultData(TypedDict):
    quick_response_arn: "aws_sdk_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the quick response.</p>"""
    quick_response_id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the quick response.</p>"""
    knowledge_base_arn: "aws_sdk_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    name: "aws_sdk_wisdom.types.quick_response_name.QuickResponseName"
    """<p>The name of the quick response.</p>"""
    content_type: "aws_sdk_wisdom.types.quick_response_type.QuickResponseType"
    """<p>The media type of the quick response content.</p> <ul> <li> <p>Use <code>application/x.quickresponse;format=plain</code> for quick response written in plain text.</p> </li> <li> <p>Use <code>application/x.quickresponse;format=markdown</code> for quick response written in richtext.</p> </li> </ul>"""
    status: "aws_sdk_wisdom.types.quick_response_status.QuickResponseStatus"
    """<p>The resource status of the quick response.</p>"""
    contents: "aws_sdk_wisdom.types.quick_response_contents.QuickResponseContents"
    """<p>The contents of the quick response.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the quick response was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp when the quick response search result data was last modified.</p>"""
    is_active: "bool"
    """<p>Whether the quick response is active.</p>"""
    description: NotRequired[
        "aws_sdk_wisdom.types.quick_response_description.QuickResponseDescription"
    ]
    """<p>The description of the quick response.</p>"""
    grouping_configuration: NotRequired[
        "aws_sdk_wisdom.types.grouping_configuration.GroupingConfiguration"
    ]
    """<p>The configuration information of the user groups that the quick response is accessible to.</p>"""
    shortcut_key: NotRequired["aws_sdk_wisdom.types.short_cut_key.ShortCutKey"]
    """<p>The shortcut key of the quick response. The value should be unique across the knowledge base.</p>"""
    last_modified_by: NotRequired["aws_sdk_wisdom.types.generic_arn.GenericArn"]
    """<p>The Amazon Resource Name (ARN) of the user who last updated the quick response search result data.</p>"""
    channels: NotRequired["aws_sdk_wisdom.types.channels.Channels"]
    """<p>The Amazon Connect contact channels this quick response applies to. The supported contact channel types include <code>Chat</code>.</p>"""
    language: NotRequired["aws_sdk_wisdom.types.language_code.LanguageCode"]
    """<p>The language code value for the language in which the quick response is written.</p>"""
    attributes_not_interpolated: NotRequired[
        "aws_sdk_wisdom.types.contact_attribute_keys.ContactAttributeKeys"
    ]
    """<p>The user defined contact attributes that are not resolved when the search result is returned.</p>"""
    attributes_interpolated: NotRequired[
        "aws_sdk_wisdom.types.contact_attribute_keys.ContactAttributeKeys"
    ]
    """<p>The user defined contact attributes that are resolved when the search result is returned.</p>"""
    tags: NotRequired["aws_sdk_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseSearchResultData) -> dict:
    out: dict = {}
    out["quickResponseArn"] = value["quick_response_arn"]
    out["quickResponseId"] = value["quick_response_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["name"] = value["name"]
    out["contentType"] = value["content_type"]
    out["status"] = value["status"]
    import aws_sdk_wisdom.types.quick_response_contents

    out["contents"] = aws_sdk_wisdom.types.quick_response_contents.serialize_json(
        value["contents"]
    )
    import aws_sdk_wisdom.types._prelude.timestamp

    out["createdTime"] = aws_sdk_wisdom.types._prelude.timestamp.serialize_json(
        value["created_time"]
    )
    import aws_sdk_wisdom.types._prelude.timestamp

    out["lastModifiedTime"] = aws_sdk_wisdom.types._prelude.timestamp.serialize_json(
        value["last_modified_time"]
    )
    out["isActive"] = value["is_active"]
    if "description" in value:
        out["description"] = value["description"]
    if "grouping_configuration" in value:
        import aws_sdk_wisdom.types.grouping_configuration

        out["groupingConfiguration"] = (
            aws_sdk_wisdom.types.grouping_configuration.serialize_json(
                value["grouping_configuration"]
            )
        )
    if "shortcut_key" in value:
        out["shortcutKey"] = value["shortcut_key"]
    if "last_modified_by" in value:
        out["lastModifiedBy"] = value["last_modified_by"]
    if "channels" in value:
        import aws_sdk_wisdom.types.channels

        out["channels"] = aws_sdk_wisdom.types.channels.serialize_json(
            value["channels"]
        )
    if "language" in value:
        out["language"] = value["language"]
    if "attributes_not_interpolated" in value:
        import aws_sdk_wisdom.types.contact_attribute_keys

        out["attributesNotInterpolated"] = (
            aws_sdk_wisdom.types.contact_attribute_keys.serialize_json(
                value["attributes_not_interpolated"]
            )
        )
    if "attributes_interpolated" in value:
        import aws_sdk_wisdom.types.contact_attribute_keys

        out["attributesInterpolated"] = (
            aws_sdk_wisdom.types.contact_attribute_keys.serialize_json(
                value["attributes_interpolated"]
            )
        )
    if "tags" in value:
        import aws_sdk_wisdom.types.tags

        out["tags"] = aws_sdk_wisdom.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> QuickResponseSearchResultData:
    out: QuickResponseSearchResultData = {}  # type: ignore[typeddict-item]
    if "quickResponseArn" in data:
        out["quick_response_arn"] = data["quickResponseArn"]
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.quick_response_arn required"
        )
    if "quickResponseId" in data:
        out["quick_response_id"] = data["quickResponseId"]
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.quick_response_id required"
        )
    if "knowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.knowledge_base_arn required"
        )
    if "knowledgeBaseId" in data:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.knowledge_base_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("QuickResponseSearchResultData.name required")
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.content_type required"
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("QuickResponseSearchResultData.status required")
    if "contents" in data:
        import aws_sdk_wisdom.types.quick_response_contents

        out["contents"] = aws_sdk_wisdom.types.quick_response_contents.deserialize_json(
            data["contents"]
        )
    else:
        raise DeserializationError("QuickResponseSearchResultData.contents required")
    if "createdTime" in data:
        import aws_sdk_wisdom.types._prelude.timestamp

        out["created_time"] = aws_sdk_wisdom.types._prelude.timestamp.deserialize_json(
            data["createdTime"]
        )
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.created_time required"
        )
    if "lastModifiedTime" in data:
        import aws_sdk_wisdom.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_wisdom.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError(
            "QuickResponseSearchResultData.last_modified_time required"
        )
    if "isActive" in data:
        out["is_active"] = data["isActive"]
    else:
        raise DeserializationError("QuickResponseSearchResultData.is_active required")
    if "description" in data:
        out["description"] = data["description"]
    if "groupingConfiguration" in data:
        import aws_sdk_wisdom.types.grouping_configuration

        out["grouping_configuration"] = (
            aws_sdk_wisdom.types.grouping_configuration.deserialize_json(
                data["groupingConfiguration"]
            )
        )
    if "shortcutKey" in data:
        out["shortcut_key"] = data["shortcutKey"]
    if "lastModifiedBy" in data:
        out["last_modified_by"] = data["lastModifiedBy"]
    if "channels" in data:
        import aws_sdk_wisdom.types.channels

        out["channels"] = aws_sdk_wisdom.types.channels.deserialize_json(
            data["channels"]
        )
    if "language" in data:
        out["language"] = data["language"]
    if "attributesNotInterpolated" in data:
        import aws_sdk_wisdom.types.contact_attribute_keys

        out["attributes_not_interpolated"] = (
            aws_sdk_wisdom.types.contact_attribute_keys.deserialize_json(
                data["attributesNotInterpolated"]
            )
        )
    if "attributesInterpolated" in data:
        import aws_sdk_wisdom.types.contact_attribute_keys

        out["attributes_interpolated"] = (
            aws_sdk_wisdom.types.contact_attribute_keys.deserialize_json(
                data["attributesInterpolated"]
            )
        )
    if "tags" in data:
        import aws_sdk_wisdom.types.tags

        out["tags"] = aws_sdk_wisdom.types.tags.deserialize_json(data["tags"])
    return out
