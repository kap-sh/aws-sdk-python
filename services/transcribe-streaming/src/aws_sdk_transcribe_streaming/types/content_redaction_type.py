"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ContentRedactionType``."""

from typing import Literal, TypeAlias, cast

ContentRedactionType: TypeAlias = Literal["PII",]


# --- restJson1 ser/de ---
def serialize_json(value: ContentRedactionType) -> str:
    return value


def deserialize_json(data: str) -> ContentRedactionType:
    return cast(ContentRedactionType, data)
