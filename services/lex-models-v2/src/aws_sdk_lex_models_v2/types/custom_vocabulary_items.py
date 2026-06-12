"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CustomVocabularyItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.custom_vocabulary_item

CustomVocabularyItems: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.custom_vocabulary_item.CustomVocabularyItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomVocabularyItems) -> list:
    import aws_sdk_lex_models_v2.types.custom_vocabulary_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.custom_vocabulary_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CustomVocabularyItems:
    import aws_sdk_lex_models_v2.types.custom_vocabulary_item

    out: CustomVocabularyItems = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.custom_vocabulary_item.deserialize_json(item)
        )
    return out
