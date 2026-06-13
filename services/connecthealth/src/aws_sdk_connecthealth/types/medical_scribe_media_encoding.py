"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeMediaEncoding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connecthealth.errors import DeserializationError

MedicalScribeMediaEncoding: TypeAlias = Literal[
    "pcm",
    "flac",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pcm",
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
