"""Generated from Smithy shape ``com.amazonaws.securityagent#Artifact``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.artifact_type


class Artifact(TypedDict, closed=True):
    contents: "str"
    """<p>The content of the artifact.</p>"""
    type: "capo_securityagent.types.artifact_type.ArtifactType"
    """<p>The file type of the artifact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Artifact) -> dict:
    out: dict = {}
    out["contents"] = value["contents"]
    import capo_securityagent.types.artifact_type

    out["type"] = capo_securityagent.types.artifact_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> Artifact:
    out: Artifact = {}  # type: ignore[typeddict-item]
    if "contents" in data:
        out["contents"] = data["contents"]
    else:
        raise DeserializationError("Artifact.contents required")
    if "type" in data:
        import capo_securityagent.types.artifact_type

        out["type"] = capo_securityagent.types.artifact_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("Artifact.type required")
    return out
