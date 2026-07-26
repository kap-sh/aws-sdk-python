"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteCustomVocabularyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id


class DeleteCustomVocabularyRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot to remove the custom vocabulary from.</p>"""
    bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot to remove the custom vocabulary from.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The locale identifier for the locale that contains the custom vocabulary to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomVocabularyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCustomVocabularyRequest:
    out: DeleteCustomVocabularyRequest = {}  # type: ignore[typeddict-item]
    return out
