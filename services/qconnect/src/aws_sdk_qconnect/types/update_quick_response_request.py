"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateQuickResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.channels
    import aws_sdk_qconnect.types.grouping_configuration
    import aws_sdk_qconnect.types.language_code
    import aws_sdk_qconnect.types.quick_response_data_provider
    import aws_sdk_qconnect.types.quick_response_description
    import aws_sdk_qconnect.types.quick_response_name
    import aws_sdk_qconnect.types.quick_response_type
    import aws_sdk_qconnect.types.short_cut_key
    import aws_sdk_qconnect.types.uuid_or_arn


class UpdateQuickResponseRequest(TypedDict, closed=True):
    knowledge_base_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    quick_response_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the quick response.</p>"""
    name: NotRequired["aws_sdk_qconnect.types.quick_response_name.QuickResponseName"]
    """<p>The name of the quick response.</p>"""
    content: NotRequired[
        "aws_sdk_qconnect.types.quick_response_data_provider.QuickResponseDataProvider"
    ]
    """<p>The updated content of the quick response.</p>"""
    content_type: NotRequired[
        "aws_sdk_qconnect.types.quick_response_type.QuickResponseType"
    ]
    """<p>The media type of the quick response content.</p> <ul> <li> <p>Use <code>application/x.quickresponse;format=plain</code> for quick response written in plain text.</p> </li> <li> <p>Use <code>application/x.quickresponse;format=markdown</code> for quick response written in richtext.</p> </li> </ul>"""
    grouping_configuration: NotRequired[
        "aws_sdk_qconnect.types.grouping_configuration.GroupingConfiguration"
    ]
    """<p>The updated grouping configuration of the quick response.</p>"""
    remove_grouping_configuration: NotRequired["bool"]
    """<p>Whether to remove the grouping configuration of the quick response.</p>"""
    description: NotRequired[
        "aws_sdk_qconnect.types.quick_response_description.QuickResponseDescription"
    ]
    """<p>The updated description of the quick response.</p>"""
    remove_description: NotRequired["bool"]
    """<p>Whether to remove the description from the quick response.</p>"""
    shortcut_key: NotRequired["aws_sdk_qconnect.types.short_cut_key.ShortCutKey"]
    """<p>The shortcut key of the quick response. The value should be unique across the knowledge base.</p>"""
    remove_shortcut_key: NotRequired["bool"]
    """<p>Whether to remove the shortcut key of the quick response.</p>"""
    is_active: NotRequired["bool"]
    """<p>Whether the quick response is active. </p>"""
    channels: NotRequired["aws_sdk_qconnect.types.channels.Channels"]
    """<p>The Amazon Connect contact channels this quick response applies to. The supported contact channel types include <code>Chat</code>.</p>"""
    language: NotRequired["aws_sdk_qconnect.types.language_code.LanguageCode"]
    """<p>The language code value for the language in which the quick response is written. The supported language codes include <code>de_DE</code>, <code>en_US</code>, <code>es_ES</code>, <code>fr_FR</code>, <code>id_ID</code>, <code>it_IT</code>, <code>ja_JP</code>, <code>ko_KR</code>, <code>pt_BR</code>, <code>zh_CN</code>, <code>zh_TW</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuickResponseRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "content" in value:
        import aws_sdk_qconnect.types.quick_response_data_provider

        out["content"] = (
            aws_sdk_qconnect.types.quick_response_data_provider.serialize_json(
                value["content"]
            )
        )
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    if "grouping_configuration" in value:
        import aws_sdk_qconnect.types.grouping_configuration

        out["groupingConfiguration"] = (
            aws_sdk_qconnect.types.grouping_configuration.serialize_json(
                value["grouping_configuration"]
            )
        )
    if "remove_grouping_configuration" in value:
        out["removeGroupingConfiguration"] = value["remove_grouping_configuration"]
    if "description" in value:
        out["description"] = value["description"]
    if "remove_description" in value:
        out["removeDescription"] = value["remove_description"]
    if "shortcut_key" in value:
        out["shortcutKey"] = value["shortcut_key"]
    if "remove_shortcut_key" in value:
        out["removeShortcutKey"] = value["remove_shortcut_key"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    if "channels" in value:
        import aws_sdk_qconnect.types.channels

        out["channels"] = aws_sdk_qconnect.types.channels.serialize_json(
            value["channels"]
        )
    if "language" in value:
        out["language"] = value["language"]
    return out


def deserialize_json(data: dict) -> UpdateQuickResponseRequest:
    out: UpdateQuickResponseRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "content" in data:
        import aws_sdk_qconnect.types.quick_response_data_provider

        out["content"] = (
            aws_sdk_qconnect.types.quick_response_data_provider.deserialize_json(
                data["content"]
            )
        )
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    if "groupingConfiguration" in data:
        import aws_sdk_qconnect.types.grouping_configuration

        out["grouping_configuration"] = (
            aws_sdk_qconnect.types.grouping_configuration.deserialize_json(
                data["groupingConfiguration"]
            )
        )
    if "removeGroupingConfiguration" in data:
        out["remove_grouping_configuration"] = data["removeGroupingConfiguration"]
    if "description" in data:
        out["description"] = data["description"]
    if "removeDescription" in data:
        out["remove_description"] = data["removeDescription"]
    if "shortcutKey" in data:
        out["shortcut_key"] = data["shortcutKey"]
    if "removeShortcutKey" in data:
        out["remove_shortcut_key"] = data["removeShortcutKey"]
    if "isActive" in data:
        out["is_active"] = data["isActive"]
    if "channels" in data:
        import aws_sdk_qconnect.types.channels

        out["channels"] = aws_sdk_qconnect.types.channels.deserialize_json(
            data["channels"]
        )
    if "language" in data:
        out["language"] = data["language"]
    return out
