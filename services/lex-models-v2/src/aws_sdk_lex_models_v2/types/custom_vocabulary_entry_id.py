"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CustomVocabularyEntryId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.item_id


class CustomVocabularyEntryId(TypedDict, closed=True):
    item_id: "aws_sdk_lex_models_v2.types.item_id.ItemId"
    """<p>The unique item identifier for the custom vocabulary items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomVocabularyEntryId) -> dict:
    out: dict = {}
    out["itemId"] = value["item_id"]
    return out


def deserialize_json(data: dict) -> CustomVocabularyEntryId:
    out: CustomVocabularyEntryId = {}  # type: ignore[typeddict-item]
    if "itemId" in data:
        out["item_id"] = data["itemId"]
    else:
        raise DeserializationError("CustomVocabularyEntryId.item_id required")
    return out
