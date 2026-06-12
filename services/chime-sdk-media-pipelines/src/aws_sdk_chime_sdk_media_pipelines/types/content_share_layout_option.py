"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ContentShareLayoutOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

ContentShareLayoutOption: TypeAlias = Literal[
    "PresenterOnly",
    "Horizontal",
    "Vertical",
    "ActiveSpeakerOnly",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PresenterOnly",
        "Horizontal",
        "Vertical",
        "ActiveSpeakerOnly",
    )
)


def serialize_json(value: ContentShareLayoutOption) -> str:
    return value


def deserialize_json(data: str) -> ContentShareLayoutOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentShareLayoutOption value: {data!r}")
    return cast(ContentShareLayoutOption, data)
