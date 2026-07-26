"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ResourceId``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_codeguru_security.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_codeguru_security.types.uuid


class _ResourceId_codeArtifactId(TypedDict, closed=True):
    codeArtifactId: "capo_codeguru_security.types.uuid.Uuid"


ResourceId: TypeAlias = _ResourceId_codeArtifactId


# --- restJson1 ser/de ---
def serialize_json(value: ResourceId) -> dict:
    if "codeArtifactId" in value:
        return {"codeArtifactId": value["codeArtifactId"]}
    else:
        raise SerializationError("ResourceId: no variant present")


def deserialize_json(data: dict) -> ResourceId:
    if "codeArtifactId" in data:
        return {"codeArtifactId": data["codeArtifactId"]}
    else:
        raise DeserializationError("ResourceId: no recognized variant key")
