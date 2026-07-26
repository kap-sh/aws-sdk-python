"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CustomVocabularyStatus``."""

from typing import Literal, TypeAlias, cast

CustomVocabularyStatus: TypeAlias = Literal[
    "Ready",
    "Deleting",
    "Exporting",
    "Importing",
    "Creating",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomVocabularyStatus) -> str:
    return value


def deserialize_json(data: str) -> CustomVocabularyStatus:
    return cast(CustomVocabularyStatus, data)
