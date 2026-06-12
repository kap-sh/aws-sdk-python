"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleExportSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class BotLocaleExportSpecification(TypedDict):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot to create the locale for.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of the bot to export.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale to export. The string must match one of the locales in the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleExportSpecification) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    out["botVersion"] = value["bot_version"]
    out["localeId"] = value["locale_id"]
    return out


def deserialize_json(data: dict) -> BotLocaleExportSpecification:
    out: BotLocaleExportSpecification = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    else:
        raise DeserializationError("BotLocaleExportSpecification.bot_id required")
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    else:
        raise DeserializationError("BotLocaleExportSpecification.bot_version required")
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    else:
        raise DeserializationError("BotLocaleExportSpecification.locale_id required")
    return out
