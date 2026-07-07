"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateArtifactMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.hash
    import aws_sdk_cleanrooms.types.hash_list


class AnalysisTemplateArtifactMetadata(TypedDict, closed=True):
    entry_point_hash: "aws_sdk_cleanrooms.types.hash.Hash"
    """<p> The hash of the entry point for the analysis template artifact metadata.</p>"""
    additional_artifact_hashes: NotRequired[
        "aws_sdk_cleanrooms.types.hash_list.HashList"
    ]
    """<p> Additional artifact hashes for the analysis template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateArtifactMetadata) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.hash

    out["entryPointHash"] = aws_sdk_cleanrooms.types.hash.serialize_json(
        value["entry_point_hash"]
    )
    if "additional_artifact_hashes" in value:
        import aws_sdk_cleanrooms.types.hash_list

        out["additionalArtifactHashes"] = (
            aws_sdk_cleanrooms.types.hash_list.serialize_json(
                value["additional_artifact_hashes"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisTemplateArtifactMetadata:
    out: AnalysisTemplateArtifactMetadata = {}  # type: ignore[typeddict-item]
    if "entryPointHash" in data:
        import aws_sdk_cleanrooms.types.hash

        out["entry_point_hash"] = aws_sdk_cleanrooms.types.hash.deserialize_json(
            data["entryPointHash"]
        )
    else:
        raise DeserializationError(
            "AnalysisTemplateArtifactMetadata.entry_point_hash required"
        )
    if "additionalArtifactHashes" in data:
        import aws_sdk_cleanrooms.types.hash_list

        out["additional_artifact_hashes"] = (
            aws_sdk_cleanrooms.types.hash_list.deserialize_json(
                data["additionalArtifactHashes"]
            )
        )
    return out
