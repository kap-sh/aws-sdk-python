"""Generated from Smithy shape ``com.amazonaws.polly#LexiconNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_polly.types.lexicon_name

LexiconNameList: TypeAlias = list["capo_polly.types.lexicon_name.LexiconName"]


# --- restJson1 ser/de ---
def serialize_json(value: LexiconNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> LexiconNameList:
    return list(data)
