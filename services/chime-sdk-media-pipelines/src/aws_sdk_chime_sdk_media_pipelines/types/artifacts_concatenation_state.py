"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ArtifactsConcatenationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

ArtifactsConcatenationState: TypeAlias = Literal[
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


def serialize_json(value: ArtifactsConcatenationState) -> str:
    return value


def deserialize_json(data: str) -> ArtifactsConcatenationState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ArtifactsConcatenationState value: {data!r}"
        )
    return cast(ArtifactsConcatenationState, data)
