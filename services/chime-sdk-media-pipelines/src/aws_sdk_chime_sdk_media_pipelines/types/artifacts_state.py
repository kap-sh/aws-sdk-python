"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ArtifactsState``."""

from typing import Literal, TypeAlias, cast

ArtifactsState: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactsState) -> str:
    return value


def deserialize_json(data: str) -> ArtifactsState:
    return cast(ArtifactsState, data)
