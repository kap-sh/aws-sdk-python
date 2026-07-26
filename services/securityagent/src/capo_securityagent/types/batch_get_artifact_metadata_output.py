"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetArtifactMetadataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.artifact_metadata_list


class BatchGetArtifactMetadataOutput(TypedDict, closed=True):
    artifact_metadata_list: (
        "capo_securityagent.types.artifact_metadata_list.ArtifactMetadataList"
    )
    """<p>The list of artifact metadata items that were found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetArtifactMetadataOutput) -> dict:
    out: dict = {}
    import capo_securityagent.types.artifact_metadata_list

    out["artifactMetadataList"] = (
        capo_securityagent.types.artifact_metadata_list.serialize_json(
            value["artifact_metadata_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetArtifactMetadataOutput:
    out: BatchGetArtifactMetadataOutput = {}  # type: ignore[typeddict-item]
    if "artifactMetadataList" in data:
        import capo_securityagent.types.artifact_metadata_list

        out["artifact_metadata_list"] = (
            capo_securityagent.types.artifact_metadata_list.deserialize_json(
                data["artifactMetadataList"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetArtifactMetadataOutput.artifact_metadata_list required"
        )
    return out
