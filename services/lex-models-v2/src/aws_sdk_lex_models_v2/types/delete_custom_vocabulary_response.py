"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteCustomVocabularyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.custom_vocabulary_status
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id


class DeleteCustomVocabularyResponse(TypedDict):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot that the custom vocabulary was removed from.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The version of the bot that the custom vocabulary was removed from.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale identifier for the locale that the custom vocabulary was removed from.</p>"""
    custom_vocabulary_status: NotRequired[
        "aws_sdk_lex_models_v2.types.custom_vocabulary_status.CustomVocabularyStatus"
    ]
    """<p>The status of removing the custom vocabulary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomVocabularyResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "custom_vocabulary_status" in value:
        import aws_sdk_lex_models_v2.types.custom_vocabulary_status

        out["customVocabularyStatus"] = (
            aws_sdk_lex_models_v2.types.custom_vocabulary_status.serialize_json(
                value["custom_vocabulary_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteCustomVocabularyResponse:
    out: DeleteCustomVocabularyResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "customVocabularyStatus" in data:
        import aws_sdk_lex_models_v2.types.custom_vocabulary_status

        out["custom_vocabulary_status"] = (
            aws_sdk_lex_models_v2.types.custom_vocabulary_status.deserialize_json(
                data["customVocabularyStatus"]
            )
        )
    return out
