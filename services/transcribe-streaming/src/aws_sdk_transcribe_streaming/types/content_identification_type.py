"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ContentIdentificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

ContentIdentificationType: TypeAlias = Literal["PII",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PII",))


def serialize_json(value: ContentIdentificationType) -> str:
    return value


def deserialize_json(data: str) -> ContentIdentificationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentIdentificationType value: {data!r}")
    return cast(ContentIdentificationType, data)
