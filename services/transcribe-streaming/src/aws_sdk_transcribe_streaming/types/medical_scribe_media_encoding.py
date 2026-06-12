"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeMediaEncoding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

MedicalScribeMediaEncoding: TypeAlias = Literal[
    "pcm",
    "ogg-opus",
    "flac",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pcm",
        "ogg-opus",
        "flac",
    )
)


def serialize_json(value: MedicalScribeMediaEncoding) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeMediaEncoding:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MedicalScribeMediaEncoding value: {data!r}"
        )
    return cast(MedicalScribeMediaEncoding, data)
