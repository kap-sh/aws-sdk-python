"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#ContentClassifier``."""

from typing import Literal, TypeAlias, cast

ContentClassifier: TypeAlias = Literal[
    "FreeOfPersonallyIdentifiableInformation",
    "FreeOfAdultContent",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentClassifier) -> str:
    return value


def deserialize_json(data: str) -> ContentClassifier:
    return cast(ContentClassifier, data)
