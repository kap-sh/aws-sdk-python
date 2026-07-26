"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateCustomVocabularyItemsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.custom_vocabulary_item

UpdateCustomVocabularyItemsList: TypeAlias = list[
    "capo_lex_models_v2.types.custom_vocabulary_item.CustomVocabularyItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomVocabularyItemsList) -> list:
    import capo_lex_models_v2.types.custom_vocabulary_item

    out: list = []
    for item in value:
        out.append(capo_lex_models_v2.types.custom_vocabulary_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateCustomVocabularyItemsList:
    import capo_lex_models_v2.types.custom_vocabulary_item

    out: UpdateCustomVocabularyItemsList = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.custom_vocabulary_item.deserialize_json(item)
        )
    return out
