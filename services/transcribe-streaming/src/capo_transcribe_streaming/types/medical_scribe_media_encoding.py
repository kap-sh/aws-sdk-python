"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeMediaEncoding``."""

from typing import Literal, TypeAlias, cast

MedicalScribeMediaEncoding: TypeAlias = Literal[
    "pcm",
    "ogg-opus",
    "flac",
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeMediaEncoding) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeMediaEncoding:
    return cast(MedicalScribeMediaEncoding, data)
