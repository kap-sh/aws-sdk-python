"""Generated from Smithy shape ``com.amazonaws.mediatailor#StreamingMediaFileConditioning``."""

from typing import Literal, TypeAlias, cast

StreamingMediaFileConditioning: TypeAlias = Literal[
    "TRANSCODE",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamingMediaFileConditioning) -> str:
    return value


def deserialize_json(data: str) -> StreamingMediaFileConditioning:
    return cast(StreamingMediaFileConditioning, data)
