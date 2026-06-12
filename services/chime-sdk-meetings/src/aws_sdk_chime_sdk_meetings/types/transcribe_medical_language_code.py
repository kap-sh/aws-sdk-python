"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeMedicalLanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

TranscribeMedicalLanguageCode: TypeAlias = Literal["en-US",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("en-US",))


def serialize_json(value: TranscribeMedicalLanguageCode) -> str:
    return value


def deserialize_json(data: str) -> TranscribeMedicalLanguageCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TranscribeMedicalLanguageCode value: {data!r}"
        )
    return cast(TranscribeMedicalLanguageCode, data)
