"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeContentIdentificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

TranscribeContentIdentificationType: TypeAlias = Literal["PII",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PII",))


def serialize_json(value: TranscribeContentIdentificationType) -> str:
    return value


def deserialize_json(data: str) -> TranscribeContentIdentificationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TranscribeContentIdentificationType value: {data!r}"
        )
    return cast(TranscribeContentIdentificationType, data)
