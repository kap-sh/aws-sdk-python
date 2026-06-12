"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateCustomVocabularyItemsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.new_custom_vocabulary_item

CreateCustomVocabularyItemsList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.new_custom_vocabulary_item.NewCustomVocabularyItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomVocabularyItemsList) -> list:
    import aws_sdk_lex_models_v2.types.new_custom_vocabulary_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.new_custom_vocabulary_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CreateCustomVocabularyItemsList:
    import aws_sdk_lex_models_v2.types.new_custom_vocabulary_item

    out: CreateCustomVocabularyItemsList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.new_custom_vocabulary_item.deserialize_json(
                item
            )
        )
    return out
