"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BatchDeleteCustomVocabularyItemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.custom_vocabulary_items
    import capo_lex_models_v2.types.failed_custom_vocabulary_items
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id


class BatchDeleteCustomVocabularyItemResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot associated with this custom vocabulary.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The identifier of the version of the bot associated with this custom vocabulary.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see Supported languages (https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).</p>"""
    errors: NotRequired[
        "capo_lex_models_v2.types.failed_custom_vocabulary_items.FailedCustomVocabularyItems"
    ]
    """<p>A list of custom vocabulary items that failed to delete during the operation. The reason for the error is contained within each error object.</p>"""
    resources: NotRequired[
        "capo_lex_models_v2.types.custom_vocabulary_items.CustomVocabularyItems"
    ]
    """<p>A list of custom vocabulary items that were successfully deleted during the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteCustomVocabularyItemResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "errors" in value:
        import capo_lex_models_v2.types.failed_custom_vocabulary_items

        out["errors"] = (
            capo_lex_models_v2.types.failed_custom_vocabulary_items.serialize_json(
                value["errors"]
            )
        )
    if "resources" in value:
        import capo_lex_models_v2.types.custom_vocabulary_items

        out["resources"] = (
            capo_lex_models_v2.types.custom_vocabulary_items.serialize_json(
                value["resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteCustomVocabularyItemResponse:
    out: BatchDeleteCustomVocabularyItemResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "errors" in data:
        import capo_lex_models_v2.types.failed_custom_vocabulary_items

        out["errors"] = (
            capo_lex_models_v2.types.failed_custom_vocabulary_items.deserialize_json(
                data["errors"]
            )
        )
    if "resources" in data:
        import capo_lex_models_v2.types.custom_vocabulary_items

        out["resources"] = (
            capo_lex_models_v2.types.custom_vocabulary_items.deserialize_json(
                data["resources"]
            )
        )
    return out
