"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeContentRedactionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

TranscribeContentRedactionType: TypeAlias = Literal["PII",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PII",))


def serialize_json(value: TranscribeContentRedactionType) -> str:
    return value


def deserialize_json(data: str) -> TranscribeContentRedactionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TranscribeContentRedactionType value: {data!r}"
        )
    return cast(TranscribeContentRedactionType, data)
