"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateBotAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_alias_id
    import capo_lex_models_v2.types.bot_alias_locale_settings_map
    import capo_lex_models_v2.types.bot_alias_status
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.conversation_log_settings
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.sentiment_analysis_settings
    import capo_lex_models_v2.types.timestamp


class UpdateBotAliasResponse(TypedDict, closed=True):
    bot_alias_id: NotRequired["capo_lex_models_v2.types.bot_alias_id.BotAliasId"]
    """<p>The identifier of the updated bot alias.</p>"""
    bot_alias_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The updated name of the bot alias.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The updated description of the bot alias.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The updated version of the bot that the alias points to.</p>"""
    bot_alias_locale_settings: NotRequired[
        "capo_lex_models_v2.types.bot_alias_locale_settings_map.BotAliasLocaleSettingsMap"
    ]
    """<p>The updated Lambda functions to use in each locale for the bot alias.</p>"""
    conversation_log_settings: NotRequired[
        "capo_lex_models_v2.types.conversation_log_settings.ConversationLogSettings"
    ]
    """<p>The updated settings for storing conversation logs in Amazon CloudWatch Logs and Amazon S3 buckets.</p>"""
    sentiment_analysis_settings: NotRequired[
        "capo_lex_models_v2.types.sentiment_analysis_settings.SentimentAnalysisSettings"
    ]
    bot_alias_status: NotRequired[
        "capo_lex_models_v2.types.bot_alias_status.BotAliasStatus"
    ]
    """<p>The current status of the bot alias. When the status is <code>Available</code> the alias is ready for use.</p>"""
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot with the updated alias.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the bot was created.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the bot was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBotAliasResponse) -> dict:
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
        import capo_lex_models_v2.types.bot_alias_locale_settings_map

        out["botAliasLocaleSettings"] = (
            capo_lex_models_v2.types.bot_alias_locale_settings_map.serialize_json(
                value["bot_alias_locale_settings"]
            )
        )
    if "conversation_log_settings" in value:
        import capo_lex_models_v2.types.conversation_log_settings

        out["conversationLogSettings"] = (
            capo_lex_models_v2.types.conversation_log_settings.serialize_json(
                value["conversation_log_settings"]
            )
        )
    if "sentiment_analysis_settings" in value:
        import capo_lex_models_v2.types.sentiment_analysis_settings

        out["sentimentAnalysisSettings"] = (
            capo_lex_models_v2.types.sentiment_analysis_settings.serialize_json(
                value["sentiment_analysis_settings"]
            )
        )
    if "bot_alias_status" in value:
        import capo_lex_models_v2.types.bot_alias_status

        out["botAliasStatus"] = (
            capo_lex_models_v2.types.bot_alias_status.serialize_json(
                value["bot_alias_status"]
            )
        )
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["last_updated_date_time"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBotAliasResponse:
    out: UpdateBotAliasResponse = {}  # type: ignore[typeddict-item]
    if "botAliasId" in data:
        out["bot_alias_id"] = data["botAliasId"]
    if "botAliasName" in data:
        out["bot_alias_name"] = data["botAliasName"]
    if "description" in data:
        out["description"] = data["description"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "botAliasLocaleSettings" in data:
        import capo_lex_models_v2.types.bot_alias_locale_settings_map

        out["bot_alias_locale_settings"] = (
            capo_lex_models_v2.types.bot_alias_locale_settings_map.deserialize_json(
                data["botAliasLocaleSettings"]
            )
        )
    if "conversationLogSettings" in data:
        import capo_lex_models_v2.types.conversation_log_settings

        out["conversation_log_settings"] = (
            capo_lex_models_v2.types.conversation_log_settings.deserialize_json(
                data["conversationLogSettings"]
            )
        )
    if "sentimentAnalysisSettings" in data:
        import capo_lex_models_v2.types.sentiment_analysis_settings

        out["sentiment_analysis_settings"] = (
            capo_lex_models_v2.types.sentiment_analysis_settings.deserialize_json(
                data["sentimentAnalysisSettings"]
            )
        )
    if "botAliasStatus" in data:
        import capo_lex_models_v2.types.bot_alias_status

        out["bot_alias_status"] = (
            capo_lex_models_v2.types.bot_alias_status.deserialize_json(
                data["botAliasStatus"]
            )
        )
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if "lastUpdatedDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    return out
