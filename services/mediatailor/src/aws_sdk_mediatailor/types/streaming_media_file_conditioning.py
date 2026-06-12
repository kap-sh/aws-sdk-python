"""Generated from Smithy shape ``com.amazonaws.mediatailor#StreamingMediaFileConditioning``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

StreamingMediaFileConditioning: TypeAlias = Literal[
    "TRANSCODE",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRANSCODE",
        "NONE",
    )
)


def serialize_json(value: StreamingMediaFileConditioning) -> str:
    return value


def deserialize_json(data: str) -> StreamingMediaFileConditioning:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StreamingMediaFileConditioning value: {data!r}"
        )
    return cast(StreamingMediaFileConditioning, data)
