"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#FailedCustomVocabularyItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.failed_custom_vocabulary_item

FailedCustomVocabularyItems: TypeAlias = list[
    "capo_lex_models_v2.types.failed_custom_vocabulary_item.FailedCustomVocabularyItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedCustomVocabularyItems) -> list:
    import capo_lex_models_v2.types.failed_custom_vocabulary_item

    out: list = []
    for item in value:
        out.append(
            capo_lex_models_v2.types.failed_custom_vocabulary_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FailedCustomVocabularyItems:
    import capo_lex_models_v2.types.failed_custom_vocabulary_item

    out: FailedCustomVocabularyItems = []
    for item in data:
        out.append(
            capo_lex_models_v2.types.failed_custom_vocabulary_item.deserialize_json(
                item
            )
        )
    return out
