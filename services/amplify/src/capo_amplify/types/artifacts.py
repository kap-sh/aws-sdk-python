"""Generated from Smithy shape ``com.amazonaws.amplify#Artifacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplify.types.artifact

Artifacts: TypeAlias = list["capo_amplify.types.artifact.Artifact"]


# --- restJson1 ser/de ---
def serialize_json(value: Artifacts) -> list:
    import capo_amplify.types.artifact

    out: list = []
    for item in value:
        out.append(capo_amplify.types.artifact.serialize_json(item))
    return out


def deserialize_json(data: list) -> Artifacts:
    import capo_amplify.types.artifact

    out: Artifacts = []
    for item in data:
        out.append(capo_amplify.types.artifact.deserialize_json(item))
    return out
