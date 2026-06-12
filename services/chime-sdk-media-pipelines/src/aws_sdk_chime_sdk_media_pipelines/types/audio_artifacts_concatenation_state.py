"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#AudioArtifactsConcatenationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

AudioArtifactsConcatenationState: TypeAlias = Literal["Enabled",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Enabled",))


def serialize_json(value: AudioArtifactsConcatenationState) -> str:
    return value


def deserialize_json(data: str) -> AudioArtifactsConcatenationState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AudioArtifactsConcatenationState value: {data!r}"
        )
    return cast(AudioArtifactsConcatenationState, data)
