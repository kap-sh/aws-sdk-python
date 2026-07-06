"""Generated from Smithy shape ``com.amazonaws.sagemaker#ArtifactSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.artifact_source_types
    import aws_sdk_sagemaker.types.source_uri


class ArtifactSource(TypedDict, closed=True):
    source_uri: NotRequired["aws_sdk_sagemaker.types.source_uri.SourceUri"]
    """<p>The URI of the source.</p>"""
    source_types: NotRequired[
        "aws_sdk_sagemaker.types.artifact_source_types.ArtifactSourceTypes"
    ]
    """<p>A list of source types.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactSource) -> dict:
    out: dict = {}
    if "source_uri" in value:
        out["SourceUri"] = value["source_uri"]
    if "source_types" in value:
        import aws_sdk_sagemaker.types.artifact_source_types

        out["SourceTypes"] = (
            aws_sdk_sagemaker.types.artifact_source_types.serialize_aws_json_1_1(
                value["source_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ArtifactSource:
    out: ArtifactSource = {}  # type: ignore[typeddict-item]
    if "SourceUri" in data:
        out["source_uri"] = data["SourceUri"]
    if "SourceTypes" in data:
        import aws_sdk_sagemaker.types.artifact_source_types

        out["source_types"] = (
            aws_sdk_sagemaker.types.artifact_source_types.deserialize_aws_json_1_1(
                data["SourceTypes"]
            )
        )
    return out
