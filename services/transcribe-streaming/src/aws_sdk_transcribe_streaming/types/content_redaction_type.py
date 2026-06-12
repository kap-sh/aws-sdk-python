"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ContentRedactionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

ContentRedactionType: TypeAlias = Literal["PII",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PII",))


def serialize_json(value: ContentRedactionType) -> str:
    return value


def deserialize_json(data: str) -> ContentRedactionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentRedactionType value: {data!r}")
    return cast(ContentRedactionType, data)
