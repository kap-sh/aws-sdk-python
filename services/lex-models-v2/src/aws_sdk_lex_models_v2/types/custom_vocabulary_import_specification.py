"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CustomVocabularyImportSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class CustomVocabularyImportSpecification(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot to import the custom vocabulary to.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot to import the custom vocabulary to.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the local to import the custom vocabulary to. The value must be <code>en_GB</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomVocabularyImportSpecification) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    out["botVersion"] = value["bot_version"]
    out["localeId"] = value["locale_id"]
    return out


def deserialize_json(data: dict) -> CustomVocabularyImportSpecification:
    out: CustomVocabularyImportSpecification = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    else:
        raise DeserializationError(
            "CustomVocabularyImportSpecification.bot_id required"
        )
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    else:
        raise DeserializationError(
            "CustomVocabularyImportSpecification.bot_version required"
        )
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    else:
        raise DeserializationError(
            "CustomVocabularyImportSpecification.locale_id required"
        )
    return out
