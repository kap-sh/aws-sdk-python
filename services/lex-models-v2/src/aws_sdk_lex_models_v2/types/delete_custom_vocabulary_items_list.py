"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteCustomVocabularyItemsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.custom_vocabulary_entry_id

DeleteCustomVocabularyItemsList: TypeAlias = list[
    "aws_sdk_lex_models_v2.types.custom_vocabulary_entry_id.CustomVocabularyEntryId"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomVocabularyItemsList) -> list:
    import aws_sdk_lex_models_v2.types.custom_vocabulary_entry_id

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lex_models_v2.types.custom_vocabulary_entry_id.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeleteCustomVocabularyItemsList:
    import aws_sdk_lex_models_v2.types.custom_vocabulary_entry_id

    out: DeleteCustomVocabularyItemsList = []
    for item in data:
        out.append(
            aws_sdk_lex_models_v2.types.custom_vocabulary_entry_id.deserialize_json(
                item
            )
        )
    return out
