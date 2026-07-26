"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeContentIdentificationType``."""

from typing import Literal, TypeAlias, cast

TranscribeContentIdentificationType: TypeAlias = Literal["PII",]


# --- restJson1 ser/de ---
def serialize_json(value: TranscribeContentIdentificationType) -> str:
    return value


def deserialize_json(data: str) -> TranscribeContentIdentificationType:
    return cast(TranscribeContentIdentificationType, data)
