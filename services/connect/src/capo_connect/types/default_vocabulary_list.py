"""Generated from Smithy shape ``com.amazonaws.connect#DefaultVocabularyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.default_vocabulary

DefaultVocabularyList: TypeAlias = list[
    "capo_connect.types.default_vocabulary.DefaultVocabulary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DefaultVocabularyList) -> list:
    import capo_connect.types.default_vocabulary

    out: list = []
    for item in value:
        out.append(capo_connect.types.default_vocabulary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DefaultVocabularyList:
    import capo_connect.types.default_vocabulary

    out: DefaultVocabularyList = []
    for item in data:
        out.append(capo_connect.types.default_vocabulary.deserialize_json(item))
    return out
