"""Generated from Smithy shape ``com.amazonaws.sagemaker#ArtifactSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.artifact_arn
    import capo_sagemaker.types.artifact_source
    import capo_sagemaker.types.experiment_entity_name
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.timestamp


class ArtifactSummary(TypedDict, closed=True):
    artifact_arn: NotRequired["capo_sagemaker.types.artifact_arn.ArtifactArn"]
    """<p>The Amazon Resource Name (ARN) of the artifact.</p>"""
    artifact_name: NotRequired[
        "capo_sagemaker.types.experiment_entity_name.ExperimentEntityName"
    ]
    """<p>The name of the artifact.</p>"""
    source: NotRequired["capo_sagemaker.types.artifact_source.ArtifactSource"]
    """<p>The source of the artifact.</p>"""
    artifact_type: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The type of the artifact.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the artifact was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>When the artifact was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactSummary) -> dict:
    out: dict = {}
    if "artifact_arn" in value:
        out["ArtifactArn"] = value["artifact_arn"]
    if "artifact_name" in value:
        out["ArtifactName"] = value["artifact_name"]
    if "source" in value:
        import capo_sagemaker.types.artifact_source

        out["Source"] = capo_sagemaker.types.artifact_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "artifact_type" in value:
        out["ArtifactType"] = value["artifact_type"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ArtifactSummary:
    out: ArtifactSummary = {}  # type: ignore[typeddict-item]
    if "ArtifactArn" in data:
        out["artifact_arn"] = data["ArtifactArn"]
    if "ArtifactName" in data:
        out["artifact_name"] = data["ArtifactName"]
    if "Source" in data:
        import capo_sagemaker.types.artifact_source

        out["source"] = capo_sagemaker.types.artifact_source.deserialize_aws_json_1_1(
            data["Source"]
        )
    if "ArtifactType" in data:
        out["artifact_type"] = data["ArtifactType"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
