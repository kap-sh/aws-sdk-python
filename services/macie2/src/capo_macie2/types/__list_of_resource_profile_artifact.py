"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfResourceProfileArtifact``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.resource_profile_artifact

__listOfResourceProfileArtifact: TypeAlias = list[
    "capo_macie2.types.resource_profile_artifact.ResourceProfileArtifact"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfResourceProfileArtifact) -> list:
    import capo_macie2.types.resource_profile_artifact

    out: list = []
    for item in value:
        out.append(capo_macie2.types.resource_profile_artifact.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfResourceProfileArtifact:
    import capo_macie2.types.resource_profile_artifact

    out: __listOfResourceProfileArtifact = []
    for item in data:
        out.append(capo_macie2.types.resource_profile_artifact.deserialize_json(item))
    return out
