"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ArtifactsConcatenationState``."""

from typing import Literal, TypeAlias, cast

ArtifactsConcatenationState: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactsConcatenationState) -> str:
    return value


def deserialize_json(data: str) -> ArtifactsConcatenationState:
    return cast(ArtifactsConcatenationState, data)
