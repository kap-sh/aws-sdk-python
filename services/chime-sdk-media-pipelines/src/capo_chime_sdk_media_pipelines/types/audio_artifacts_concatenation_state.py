"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#AudioArtifactsConcatenationState``."""

from typing import Literal, TypeAlias, cast

AudioArtifactsConcatenationState: TypeAlias = Literal["Enabled",]


# --- restJson1 ser/de ---
def serialize_json(value: AudioArtifactsConcatenationState) -> str:
    return value


def deserialize_json(data: str) -> AudioArtifactsConcatenationState:
    return cast(AudioArtifactsConcatenationState, data)
