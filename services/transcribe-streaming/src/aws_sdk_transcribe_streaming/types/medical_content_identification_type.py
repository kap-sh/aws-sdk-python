"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalContentIdentificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

MedicalContentIdentificationType: TypeAlias = Literal["PHI",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PHI",))


def serialize_json(value: MedicalContentIdentificationType) -> str:
    return value


def deserialize_json(data: str) -> MedicalContentIdentificationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MedicalContentIdentificationType value: {data!r}"
        )
    return cast(MedicalContentIdentificationType, data)
