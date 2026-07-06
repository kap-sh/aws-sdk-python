"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateBotAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_alias_id
    import aws_sdk_lex_models_v2.types.bot_alias_locale_settings_map
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.conversation_log_settings
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.sentiment_analysis_settings


class UpdateBotAliasRequest(TypedDict, closed=True):
    bot_alias_id: "aws_sdk_lex_models_v2.types.bot_alias_id.BotAliasId"
    """<p>The unique identifier of the bot alias.</p>"""
    bot_alias_name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The new name to assign to the bot alias.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The new description to assign to the bot alias.</p>"""
    bot_version: NotRequired["aws_sdk_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The new bot version to assign to the bot alias.</p>"""
    bot_alias_locale_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_alias_locale_settings_map.BotAliasLocaleSettingsMap"
    ]
    """<p>The new Lambda functions to use in each locale for the bot alias.</p>"""
    conversation_log_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.conversation_log_settings.ConversationLogSettings"
    ]
    """<p>The new settings for storing conversation logs in Amazon CloudWatch Logs and Amazon S3 buckets.</p>"""
    sentiment_analysis_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.sentiment_analysis_settings.SentimentAnalysisSettings"
    ]
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot with the updated alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBotAliasRequest) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> UpdateBotAliasRequest:
    out: UpdateBotAliasRequest = {}  # type: ignore[typeddict-item]
    if "botAliasName" in data:
        out["bot_alias_name"] = data["botAliasName"]
    else:
        raise DeserializationError("UpdateBotAliasRequest.bot_alias_name required")
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
    return out
