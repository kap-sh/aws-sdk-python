"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeContentRedactionType``."""

from typing import Literal, TypeAlias, cast

TranscribeContentRedactionType: TypeAlias = Literal["PII",]


# --- restJson1 ser/de ---
def serialize_json(value: TranscribeContentRedactionType) -> str:
    return value


def deserialize_json(data: str) -> TranscribeContentRedactionType:
    return cast(TranscribeContentRedactionType, data)
