"""Generated from Smithy shape ``com.amazonaws.securityagent#ArtifactIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.artifact_id

ArtifactIds: TypeAlias = list["capo_securityagent.types.artifact_id.ArtifactId"]


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactIds) -> list:
    return list(value)


def deserialize_json(data: list) -> ArtifactIds:
    return list(data)
