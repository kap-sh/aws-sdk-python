"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#PutBotAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.alias_name
    import aws_sdk_lex_model_building_service.types.bot_name
    import aws_sdk_lex_model_building_service.types.conversation_logs_response
    import aws_sdk_lex_model_building_service.types.description
    import aws_sdk_lex_model_building_service.types.string
    import aws_sdk_lex_model_building_service.types.tag_list
    import aws_sdk_lex_model_building_service.types.timestamp
    import aws_sdk_lex_model_building_service.types.version


class PutBotAliasResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_lex_model_building_service.types.alias_name.AliasName"]
    """<p>The name of the alias.</p>"""
    description: NotRequired[
        "aws_sdk_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the alias.</p>"""
    bot_version: NotRequired["aws_sdk_lex_model_building_service.types.version.Version"]
    """<p>The version of the bot that the alias points to.</p>"""
    bot_name: NotRequired["aws_sdk_lex_model_building_service.types.bot_name.BotName"]
    """<p>The name of the bot that the alias points to.</p>"""
    last_updated_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the bot alias was updated. When you create a resource, the creation date and the last updated date are the same.</p>"""
    created_date: NotRequired[
        "aws_sdk_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the bot alias was created.</p>"""
    checksum: NotRequired["aws_sdk_lex_model_building_service.types.string.String"]
    """<p>The checksum for the current version of the alias.</p>"""
    conversation_logs: NotRequired[
        "aws_sdk_lex_model_building_service.types.conversation_logs_response.ConversationLogsResponse"
    ]
    """<p>The settings that determine how Amazon Lex uses conversation logs for the alias.</p>"""
    tags: NotRequired["aws_sdk_lex_model_building_service.types.tag_list.TagList"]
    """<p>A list of tags associated with a bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutBotAliasResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "bot_name" in value:
        out["botName"] = value["bot_name"]
    if "last_updated_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["lastUpdatedDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "created_date" in value:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["createdDate"] = (
            aws_sdk_lex_model_building_service.types.timestamp.serialize_json(
                value["created_date"]
            )
        )
    if "checksum" in value:
        out["checksum"] = value["checksum"]
    if "conversation_logs" in value:
        import aws_sdk_lex_model_building_service.types.conversation_logs_response

        out["conversationLogs"] = (
            aws_sdk_lex_model_building_service.types.conversation_logs_response.serialize_json(
                value["conversation_logs"]
            )
        )
    if "tags" in value:
        import aws_sdk_lex_model_building_service.types.tag_list

        out["tags"] = aws_sdk_lex_model_building_service.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> PutBotAliasResponse:
    out: PutBotAliasResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "botName" in data:
        out["bot_name"] = data["botName"]
    if "lastUpdatedDate" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["last_updated_date"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if "createdDate" in data:
        import aws_sdk_lex_model_building_service.types.timestamp

        out["created_date"] = (
            aws_sdk_lex_model_building_service.types.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if "checksum" in data:
        out["checksum"] = data["checksum"]
    if "conversationLogs" in data:
        import aws_sdk_lex_model_building_service.types.conversation_logs_response

        out["conversation_logs"] = (
            aws_sdk_lex_model_building_service.types.conversation_logs_response.deserialize_json(
                data["conversationLogs"]
            )
        )
    if "tags" in data:
        import aws_sdk_lex_model_building_service.types.tag_list

        out["tags"] = (
            aws_sdk_lex_model_building_service.types.tag_list.deserialize_json(
                data["tags"]
            )
        )
    return out
