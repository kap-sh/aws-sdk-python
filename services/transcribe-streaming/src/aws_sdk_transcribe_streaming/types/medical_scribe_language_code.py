"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeLanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

MedicalScribeLanguageCode: TypeAlias = Literal["en-US",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("en-US",))


def serialize_json(value: MedicalScribeLanguageCode) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeLanguageCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MedicalScribeLanguageCode value: {data!r}")
    return cast(MedicalScribeLanguageCode, data)
