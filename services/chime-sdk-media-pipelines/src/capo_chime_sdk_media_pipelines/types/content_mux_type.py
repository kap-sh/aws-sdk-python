"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ContentMuxType``."""

from typing import Literal, TypeAlias, cast

ContentMuxType: TypeAlias = Literal["ContentOnly",]


# --- restJson1 ser/de ---
def serialize_json(value: ContentMuxType) -> str:
    return value


def deserialize_json(data: str) -> ContentMuxType:
    return cast(ContentMuxType, data)
