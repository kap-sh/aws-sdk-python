"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AudioRecognitionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AudioRecognitionStrategy: TypeAlias = Literal["UseSlotValuesAsCustomVocabulary",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("UseSlotValuesAsCustomVocabulary",))


def serialize_json(value: AudioRecognitionStrategy) -> str:
    return value


def deserialize_json(data: str) -> AudioRecognitionStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudioRecognitionStrategy value: {data!r}")
    return cast(AudioRecognitionStrategy, data)
