"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ArtifactsState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

ArtifactsState: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_json(value: ArtifactsState) -> str:
    return value


def deserialize_json(data: str) -> ArtifactsState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArtifactsState value: {data!r}")
    return cast(ArtifactsState, data)
