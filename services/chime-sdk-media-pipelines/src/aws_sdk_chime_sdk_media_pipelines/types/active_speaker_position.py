"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ActiveSpeakerPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

ActiveSpeakerPosition: TypeAlias = Literal[
    "TopLeft",
    "TopRight",
    "BottomLeft",
    "BottomRight",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TopLeft",
        "TopRight",
        "BottomLeft",
        "BottomRight",
    )
)


def serialize_json(value: ActiveSpeakerPosition) -> str:
    return value


def deserialize_json(data: str) -> ActiveSpeakerPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActiveSpeakerPosition value: {data!r}")
    return cast(ActiveSpeakerPosition, data)
