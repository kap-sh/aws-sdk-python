"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#FailedCustomVocabularyItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.error_code
    import aws_sdk_lex_models_v2.types.error_message
    import aws_sdk_lex_models_v2.types.item_id


class FailedCustomVocabularyItem(TypedDict):
    item_id: NotRequired["aws_sdk_lex_models_v2.types.item_id.ItemId"]
    """<p>The unique item identifer for the failed custom vocabulary item from the custom vocabulary list.</p>"""
    error_message: NotRequired["aws_sdk_lex_models_v2.types.error_message.ErrorMessage"]
    """<p>The error message for the failed custom vocabulary item from the custom vocabulary list.</p>"""
    error_code: NotRequired["aws_sdk_lex_models_v2.types.error_code.ErrorCode"]
    """<p>The unique error code for the failed custom vocabulary item from the custom vocabulary list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedCustomVocabularyItem) -> dict:
    out: dict = {}
    if "item_id" in value:
        out["itemId"] = value["item_id"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_code" in value:
        import aws_sdk_lex_models_v2.types.error_code

        out["errorCode"] = aws_sdk_lex_models_v2.types.error_code.serialize_json(
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
        import aws_sdk_lex_models_v2.types.error_code

        out["error_code"] = aws_sdk_lex_models_v2.types.error_code.deserialize_json(
            data["errorCode"]
        )
    return out
