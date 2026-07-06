"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CustomVocabularyExportSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class CustomVocabularyExportSpecification(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot that contains the custom vocabulary to export.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of the bot that contains the custom vocabulary to export.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    """<p>The locale of the bot that contains the custom vocabulary to export.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomVocabularyExportSpecification) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    out["botVersion"] = value["bot_version"]
    out["localeId"] = value["locale_id"]
    return out


def deserialize_json(data: dict) -> CustomVocabularyExportSpecification:
    out: CustomVocabularyExportSpecification = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    else:
        raise DeserializationError(
            "CustomVocabularyExportSpecification.bot_id required"
        )
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    else:
        raise DeserializationError(
            "CustomVocabularyExportSpecification.bot_version required"
        )
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    else:
        raise DeserializationError(
            "CustomVocabularyExportSpecification.locale_id required"
        )
    return out
