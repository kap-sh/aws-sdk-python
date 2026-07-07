"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteBotLocaleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_locale_status
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class DeleteBotLocaleResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot that contained the deleted locale.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot that contained the deleted locale.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The language and locale of the deleted locale.</p>"""
    bot_locale_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_locale_status.BotLocaleStatus"
    ]
    """<p>The status of deleting the bot locale. The locale first enters the <code>Deleting</code> status. Once the locale is deleted it no longer appears in the list of locales for the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotLocaleResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "bot_locale_status" in value:
        import aws_sdk_lex_models_v2.types.bot_locale_status

        out["botLocaleStatus"] = (
            aws_sdk_lex_models_v2.types.bot_locale_status.serialize_json(
                value["bot_locale_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteBotLocaleResponse:
    out: DeleteBotLocaleResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "botLocaleStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_locale_status

        out["bot_locale_status"] = (
            aws_sdk_lex_models_v2.types.bot_locale_status.deserialize_json(
                data["botLocaleStatus"]
            )
        )
    return out
