"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeMedicalContentIdentificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

TranscribeMedicalContentIdentificationType: TypeAlias = Literal["PHI",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PHI",))


def serialize_json(value: TranscribeMedicalContentIdentificationType) -> str:
    return value


def deserialize_json(data: str) -> TranscribeMedicalContentIdentificationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TranscribeMedicalContentIdentificationType value: {data!r}"
        )
    return cast(TranscribeMedicalContentIdentificationType, data)
