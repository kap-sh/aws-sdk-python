"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AudioRecognitionStrategy``."""

from typing import Literal, TypeAlias, cast

AudioRecognitionStrategy: TypeAlias = Literal["UseSlotValuesAsCustomVocabulary",]


# --- restJson1 ser/de ---
def serialize_json(value: AudioRecognitionStrategy) -> str:
    return value


def deserialize_json(data: str) -> AudioRecognitionStrategy:
    return cast(AudioRecognitionStrategy, data)
