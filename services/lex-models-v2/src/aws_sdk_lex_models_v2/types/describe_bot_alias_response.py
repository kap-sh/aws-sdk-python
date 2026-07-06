"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_history_events_list
    import aws_sdk_lex_models_v2.types.bot_alias_id
    import aws_sdk_lex_models_v2.types.bot_alias_locale_settings_map
    import aws_sdk_lex_models_v2.types.bot_alias_status
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.conversation_log_settings
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.parent_bot_networks
    import aws_sdk_lex_models_v2.types.sentiment_analysis_settings
    import aws_sdk_lex_models_v2.types.timestamp


class DescribeBotAliasResponse(TypedDict, closed=True):
    bot_alias_id: NotRequired["aws_sdk_lex_models_v2.types.bot_alias_id.BotAliasId"]
    """<p>The identifier of the bot alias.</p>"""
    bot_alias_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name of the bot alias.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The description of the bot alias.</p>"""
    bot_version: NotRequired["aws_sdk_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot associated with the bot alias.</p>"""
    bot_alias_locale_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_alias_locale_settings_map.BotAliasLocaleSettingsMap"
    ]
    """<p>The locale settings that are unique to the alias.</p>"""
    conversation_log_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.conversation_log_settings.ConversationLogSettings"
    ]
    """<p>Specifics of how Amazon Lex logs text and audio conversations with the bot associated with the alias.</p>"""
    sentiment_analysis_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.sentiment_analysis_settings.SentimentAnalysisSettings"
    ]
    bot_alias_history_events: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_alias_history_events_list.BotAliasHistoryEventsList"
    ]
    """<p>A list of events that affect a bot alias. For example, an event is recorded when the version that the alias points to changes.</p>"""
    bot_alias_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_alias_status.BotAliasStatus"
    ]
    """<p>The current status of the alias. When the alias is <code>Available</code>, the alias is ready for use with your bot.</p>"""
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot associated with the bot alias.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the alias was created.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>A timestamp of the date and time that the alias was last updated.</p>"""
    parent_bot_networks: NotRequired[
        "aws_sdk_lex_models_v2.types.parent_bot_networks.ParentBotNetworks"
    ]
    """<p>A list of the networks to which the bot alias you described belongs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotAliasResponse) -> dict:
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
    if "bot_alias_history_events" in value:
        import aws_sdk_lex_models_v2.types.bot_alias_history_events_list

        out["botAliasHistoryEvents"] = (
            aws_sdk_lex_models_v2.types.bot_alias_history_events_list.serialize_json(
                value["bot_alias_history_events"]
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
    if "last_updated_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_date_time"]
            )
        )
    if "parent_bot_networks" in value:
        import aws_sdk_lex_models_v2.types.parent_bot_networks

        out["parentBotNetworks"] = (
            aws_sdk_lex_models_v2.types.parent_bot_networks.serialize_json(
                value["parent_bot_networks"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeBotAliasResponse:
    out: DescribeBotAliasResponse = {}  # type: ignore[typeddict-item]
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
    if "botAliasHistoryEvents" in data:
        import aws_sdk_lex_models_v2.types.bot_alias_history_events_list

        out["bot_alias_history_events"] = (
            aws_sdk_lex_models_v2.types.bot_alias_history_events_list.deserialize_json(
                data["botAliasHistoryEvents"]
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
    if "lastUpdatedDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    if "parentBotNetworks" in data:
        import aws_sdk_lex_models_v2.types.parent_bot_networks

        out["parent_bot_networks"] = (
            aws_sdk_lex_models_v2.types.parent_bot_networks.deserialize_json(
                data["parentBotNetworks"]
            )
        )
    return out
