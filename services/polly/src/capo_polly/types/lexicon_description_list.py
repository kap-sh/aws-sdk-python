"""Generated from Smithy shape ``com.amazonaws.polly#LexiconDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_polly.types.lexicon_description

LexiconDescriptionList: TypeAlias = list[
    "capo_polly.types.lexicon_description.LexiconDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: LexiconDescriptionList) -> list:
    import capo_polly.types.lexicon_description

    out: list = []
    for item in value:
        out.append(capo_polly.types.lexicon_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> LexiconDescriptionList:
    import capo_polly.types.lexicon_description

    out: LexiconDescriptionList = []
    for item in data:
        out.append(capo_polly.types.lexicon_description.deserialize_json(item))
    return out
