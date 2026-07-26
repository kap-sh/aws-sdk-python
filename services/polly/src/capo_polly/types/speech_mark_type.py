"""Generated from Smithy shape ``com.amazonaws.polly#SpeechMarkType``."""

from typing import Literal, TypeAlias, cast

SpeechMarkType: TypeAlias = Literal[
    "sentence",
    "ssml",
    "viseme",
    "word",
]


# --- restJson1 ser/de ---
def serialize_json(value: SpeechMarkType) -> str:
    return value


def deserialize_json(data: str) -> SpeechMarkType:
    return cast(SpeechMarkType, data)
