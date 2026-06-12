"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BatchUpdateCustomVocabularyItemResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version
    import aws_sdk_lex_models_v2.types.custom_vocabulary_items
    import aws_sdk_lex_models_v2.types.failed_custom_vocabulary_items
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class BatchUpdateCustomVocabularyItemResponse(TypedDict):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot associated with this custom vocabulary.</p>"""
    bot_version: NotRequired["aws_sdk_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The identifier of the version of the bot associated with this custom vocabulary.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\"> Supported Languages </a>.</p>"""
    errors: NotRequired[
        "aws_sdk_lex_models_v2.types.failed_custom_vocabulary_items.FailedCustomVocabularyItems"
    ]
    """<p>A list of custom vocabulary items that failed to update during the operation. The reason for the error is contained within each error object.</p>"""
    resources: NotRequired[
        "aws_sdk_lex_models_v2.types.custom_vocabulary_items.CustomVocabularyItems"
    ]
    """<p>A list of custom vocabulary items that were successfully updated during the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateCustomVocabularyItemResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "errors" in value:
        import aws_sdk_lex_models_v2.types.failed_custom_vocabulary_items

        out["errors"] = (
            aws_sdk_lex_models_v2.types.failed_custom_vocabulary_items.serialize_json(
                value["errors"]
            )
        )
    if "resources" in value:
        import aws_sdk_lex_models_v2.types.custom_vocabulary_items

        out["resources"] = (
            aws_sdk_lex_models_v2.types.custom_vocabulary_items.serialize_json(
                value["resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateCustomVocabularyItemResponse:
    out: BatchUpdateCustomVocabularyItemResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "errors" in data:
        import aws_sdk_lex_models_v2.types.failed_custom_vocabulary_items

        out["errors"] = (
            aws_sdk_lex_models_v2.types.failed_custom_vocabulary_items.deserialize_json(
                data["errors"]
            )
        )
    if "resources" in data:
        import aws_sdk_lex_models_v2.types.custom_vocabulary_items

        out["resources"] = (
            aws_sdk_lex_models_v2.types.custom_vocabulary_items.deserialize_json(
                data["resources"]
            )
        )
    return out
