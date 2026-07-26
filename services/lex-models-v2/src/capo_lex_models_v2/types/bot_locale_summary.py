"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_locale_status
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.locale_name
    import capo_lex_models_v2.types.timestamp


class BotLocaleSummary(TypedDict, closed=True):
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The language and locale of the bot locale.</p>"""
    locale_name: NotRequired["capo_lex_models_v2.types.locale_name.LocaleName"]
    """<p>The name of the bot locale.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The description of the bot locale.</p>"""
    bot_locale_status: NotRequired[
        "capo_lex_models_v2.types.bot_locale_status.BotLocaleStatus"
    ]
    """<p>The current status of the bot locale. When the status is <code>Built</code> the locale is ready for use.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the bot locale was last updated.</p>"""
    last_build_submitted_date_time: NotRequired[
        "capo_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>A timestamp of the date and time that the bot locale was last built.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleSummary) -> dict:
    out: dict = {}
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "locale_name" in value:
        out["localeName"] = value["locale_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "bot_locale_status" in value:
        import capo_lex_models_v2.types.bot_locale_status

        out["botLocaleStatus"] = (
            capo_lex_models_v2.types.bot_locale_status.serialize_json(
                value["bot_locale_status"]
            )
        )
    if "last_updated_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["last_updated_date_time"]
        )
    if "last_build_submitted_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastBuildSubmittedDateTime"] = (
            capo_lex_models_v2.types.timestamp.serialize_json(
                value["last_build_submitted_date_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> BotLocaleSummary:
    out: BotLocaleSummary = {}  # type: ignore[typeddict-item]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "localeName" in data:
        out["locale_name"] = data["localeName"]
    if "description" in data:
        out["description"] = data["description"]
    if "botLocaleStatus" in data:
        import capo_lex_models_v2.types.bot_locale_status

        out["bot_locale_status"] = (
            capo_lex_models_v2.types.bot_locale_status.deserialize_json(
                data["botLocaleStatus"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
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
