"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateBotAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_id
    import aws_sdk_lex_models_v2.types.bot_alias_locale_settings_map
    import aws_sdk_lex_models_v2.types.bot_alias_status
    import aws_sdk_lex_models_v2.types.conversation_log_settings
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.numerical_bot_version
    import aws_sdk_lex_models_v2.types.sentiment_analysis_settings
    import aws_sdk_lex_models_v2.types.tag_map
    import aws_sdk_lex_models_v2.types.timestamp


class CreateBotAliasResponse(TypedDict, closed=True):
    bot_alias_id: NotRequired["aws_sdk_lex_models_v2.types.bot_alias_id.BotAliasId"]
    """<p>The unique identifier of the bot alias.</p>"""
    bot_alias_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name specified for the bot alias.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The description specified for the bot alias.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.numerical_bot_version.NumericalBotVersion"
    ]
    """<p>The version of the bot associated with this alias.</p>"""
    bot_alias_locale_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_alias_locale_settings_map.BotAliasLocaleSettingsMap"
    ]
    """<p>Configuration information for a specific locale.</p>"""
    conversation_log_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.conversation_log_settings.ConversationLogSettings"
    ]
    """<p>The conversation log settings specified for the alias.</p>"""
    sentiment_analysis_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.sentiment_analysis_settings.SentimentAnalysisSettings"
    ]
    bot_alias_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_alias_status.BotAliasStatus"
    ]
    """<p>The current status of the alias. The alias is first put into the <code>Creating</code> state. When the alias is ready to be used, it is put into the <code>Available</code> state. You can use the <code>DescribeBotAlias</code> operation to get the current state of an alias.</p>"""
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot that this alias applies to.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A Unix timestamp indicating the date and time that the bot alias was created.</p>"""
    tags: NotRequired["aws_sdk_lex_models_v2.types.tag_map.TagMap"]
    """<p>A list of tags associated with the bot alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotAliasResponse) -> dict:
    out: dict = {}
    if "bot_alias_id" in value:
        out["botAliasId"] = value["bot_alias_id"]
    if "bot_alias_name" in value:
        out["botAliasName"] = value["bot_alias_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "bot_alias_locale_settings" in value:
        import aws_sdk_lex_models_v2.types.bot_alias_locale_settings_map

        out["botAliasLocaleSettings"] = (
            aws_sdk_lex_models_v2.types.bot_alias_locale_settings_map.serialize_json(
                value["bot_alias_locale_settings"]
            )
        )
    if "conversation_log_settings" in value:
        import aws_sdk_lex_models_v2.types.conversation_log_settings

        out["conversationLogSettings"] = (
            aws_sdk_lex_models_v2.types.conversation_log_settings.serialize_json(
                value["conversation_log_settings"]
            )
        )
    if "sentiment_analysis_settings" in value:
        import aws_sdk_lex_models_v2.types.sentiment_analysis_settings

        out["sentimentAnalysisSettings"] = (
            aws_sdk_lex_models_v2.types.sentiment_analysis_settings.serialize_json(
                value["sentiment_analysis_settings"]
            )
        )
    if "bot_alias_status" in value:
        import aws_sdk_lex_models_v2.types.bot_alias_status

        out["botAliasStatus"] = (
            aws_sdk_lex_models_v2.types.bot_alias_status.serialize_json(
                value["bot_alias_status"]
            )
        )
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "tags" in value:
        import aws_sdk_lex_models_v2.types.tag_map

        out["tags"] = aws_sdk_lex_models_v2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateBotAliasResponse:
    out: CreateBotAliasResponse = {}  # type: ignore[typeddict-item]
    if "botAliasId" in data:
        out["bot_alias_id"] = data["botAliasId"]
    if "botAliasName" in data:
        out["bot_alias_name"] = data["botAliasName"]
    if "description" in data:
        out["description"] = data["description"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "botAliasLocaleSettings" in data:
        import aws_sdk_lex_models_v2.types.bot_alias_locale_settings_map

        out["bot_alias_locale_settings"] = (
            aws_sdk_lex_models_v2.types.bot_alias_locale_settings_map.deserialize_json(
                data["botAliasLocaleSettings"]
            )
        )
    if "conversationLogSettings" in data:
        import aws_sdk_lex_models_v2.types.conversation_log_settings

        out["conversation_log_settings"] = (
            aws_sdk_lex_models_v2.types.conversation_log_settings.deserialize_json(
                data["conversationLogSettings"]
            )
        )
    if "sentimentAnalysisSettings" in data:
        import aws_sdk_lex_models_v2.types.sentiment_analysis_settings

        out["sentiment_analysis_settings"] = (
            aws_sdk_lex_models_v2.types.sentiment_analysis_settings.deserialize_json(
                data["sentimentAnalysisSettings"]
            )
        )
    if "botAliasStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_alias_status

        out["bot_alias_status"] = (
            aws_sdk_lex_models_v2.types.bot_alias_status.deserialize_json(
                data["botAliasStatus"]
            )
        )
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "tags" in data:
        import aws_sdk_lex_models_v2.types.tag_map

        out["tags"] = aws_sdk_lex_models_v2.types.tag_map.deserialize_json(data["tags"])
    return out
