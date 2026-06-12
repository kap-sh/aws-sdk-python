"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CustomVocabularyItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.item_id
    import aws_sdk_lex_models_v2.types.phrase
    import aws_sdk_lex_models_v2.types.weight


class CustomVocabularyItem(TypedDict):
    item_id: "aws_sdk_lex_models_v2.types.item_id.ItemId"
    """<p>The unique item identifer for the custom vocabulary item from the custom vocabulary list.</p>"""
    phrase: "aws_sdk_lex_models_v2.types.phrase.Phrase"
    """<p>The unique phrase for the custom vocabulary item from the custom vocabulary list.</p>"""
    weight: NotRequired["aws_sdk_lex_models_v2.types.weight.Weight"]
    """<p>The weight assigned for the custom vocabulary item from the custom vocabulary list.</p>"""
    display_as: NotRequired["aws_sdk_lex_models_v2.types.phrase.Phrase"]
    """<p>The DisplayAs value for the custom vocabulary item from the custom vocabulary list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomVocabularyItem) -> dict:
    out: dict = {}
    out["itemId"] = value["item_id"]
    out["phrase"] = value["phrase"]
    if "weight" in value:
        out["weight"] = value["weight"]
    if "display_as" in value:
        out["displayAs"] = value["display_as"]
    return out


def deserialize_json(data: dict) -> CustomVocabularyItem:
    out: CustomVocabularyItem = {}  # type: ignore[typeddict-item]
    if "itemId" in data:
        out["item_id"] = data["itemId"]
    else:
        raise DeserializationError("CustomVocabularyItem.item_id required")
    if "phrase" in data:
        out["phrase"] = data["phrase"]
    else:
        raise DeserializationError("CustomVocabularyItem.phrase required")
    if "weight" in data:
        out["weight"] = data["weight"]
    if "displayAs" in data:
        out["display_as"] = data["displayAs"]
    return out
