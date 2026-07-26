"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#FailedCustomVocabularyItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.error_code
    import capo_lex_models_v2.types.error_message
    import capo_lex_models_v2.types.item_id


class FailedCustomVocabularyItem(TypedDict, closed=True):
    item_id: NotRequired["capo_lex_models_v2.types.item_id.ItemId"]
    """<p>The unique item identifer for the failed custom vocabulary item from the custom vocabulary list.</p>"""
    error_message: NotRequired["capo_lex_models_v2.types.error_message.ErrorMessage"]
    """<p>The error message for the failed custom vocabulary item from the custom vocabulary list.</p>"""
    error_code: NotRequired["capo_lex_models_v2.types.error_code.ErrorCode"]
    """<p>The unique error code for the failed custom vocabulary item from the custom vocabulary list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedCustomVocabularyItem) -> dict:
    out: dict = {}
    if "item_id" in value:
        out["itemId"] = value["item_id"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_code" in value:
        import capo_lex_models_v2.types.error_code

        out["errorCode"] = capo_lex_models_v2.types.error_code.serialize_json(
            value["error_code"]
        )
    return out


def deserialize_json(data: dict) -> FailedCustomVocabularyItem:
    out: FailedCustomVocabularyItem = {}  # type: ignore[typeddict-item]
    if "itemId" in data:
        out["item_id"] = data["itemId"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorCode" in data:
        import capo_lex_models_v2.types.error_code

        out["error_code"] = capo_lex_models_v2.types.error_code.deserialize_json(
            data["errorCode"]
        )
    return out
