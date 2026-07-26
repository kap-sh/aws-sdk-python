"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BuildBotLocaleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_locale_status
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.timestamp


class BuildBotLocaleResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the specified bot.</p>"""
    bot_version: NotRequired[
        "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot that was built. This is only the draft version of the bot.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The language and locale specified of where the bot can be used.</p>"""
    bot_locale_status: NotRequired[
        "capo_lex_models_v2.types.bot_locale_status.BotLocaleStatus"
    ]
    """<p>The bot's build status. When the status is <code>ReadyExpressTesting</code> you can test the bot using the utterances defined for the intents and slot types. When the status is <code>Built</code>, the bot is ready for use and can be tested using any utterance.</p>"""
    last_build_submitted_date_time: NotRequired[
        "capo_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>A timestamp indicating the date and time that the bot was last built for this locale.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BuildBotLocaleResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "bot_locale_status" in value:
        import capo_lex_models_v2.types.bot_locale_status

        out["botLocaleStatus"] = (
            capo_lex_models_v2.types.bot_locale_status.serialize_json(
                value["bot_locale_status"]
            )
        )
    if "last_build_submitted_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastBuildSubmittedDateTime"] = (
            capo_lex_models_v2.types.timestamp.serialize_json(
                value["last_build_submitted_date_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> BuildBotLocaleResponse:
    out: BuildBotLocaleResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "botLocaleStatus" in data:
        import capo_lex_models_v2.types.bot_locale_status

        out["bot_locale_status"] = (
            capo_lex_models_v2.types.bot_locale_status.deserialize_json(
                data["botLocaleStatus"]
            )
        )
    if "lastBuildSubmittedDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["last_build_submitted_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastBuildSubmittedDateTime"]
            )
        )
    return out
