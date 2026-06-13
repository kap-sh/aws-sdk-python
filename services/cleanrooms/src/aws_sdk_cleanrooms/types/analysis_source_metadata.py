"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisSourceMetadata``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_artifact_metadata


class _AnalysisSourceMetadata_artifacts(TypedDict):
    artifacts: "aws_sdk_cleanrooms.types.analysis_template_artifact_metadata.AnalysisTemplateArtifactMetadata"


AnalysisSourceMetadata: TypeAlias = _AnalysisSourceMetadata_artifacts


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSourceMetadata) -> dict:
    if "artifacts" in value:
        import aws_sdk_cleanrooms.types.analysis_template_artifact_metadata

        return {
            "artifacts": aws_sdk_cleanrooms.types.analysis_template_artifact_metadata.serialize_json(
                value["artifacts"]
            )
        }
    else:
        raise SerializationError("AnalysisSourceMetadata: no variant present")


def deserialize_json(data: dict) -> AnalysisSourceMetadata:
    if "artifacts" in data:
        import aws_sdk_cleanrooms.types.analysis_template_artifact_metadata

        return {
            "artifacts": aws_sdk_cleanrooms.types.analysis_template_artifact_metadata.deserialize_json(
                data["artifacts"]
            )
        }
    else:
        raise DeserializationError("AnalysisSourceMetadata: no recognized variant key")
