"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ContentIdentificationType``."""

from typing import Literal, TypeAlias, cast

ContentIdentificationType: TypeAlias = Literal["PII",]


# --- restJson1 ser/de ---
def serialize_json(value: ContentIdentificationType) -> str:
    return value


def deserialize_json(data: str) -> ContentIdentificationType:
    return cast(ContentIdentificationType, data)
