"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateArtifacts``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_template_artifact
    import aws_sdk_cleanrooms.types.analysis_template_artifact_list
    import aws_sdk_cleanrooms.types.role_arn


class AnalysisTemplateArtifacts(TypedDict):
    entry_point: (
        "aws_sdk_cleanrooms.types.analysis_template_artifact.AnalysisTemplateArtifact"
    )
    """<p> The entry point for the analysis template artifacts.</p>"""
    additional_artifacts: NotRequired[
        "aws_sdk_cleanrooms.types.analysis_template_artifact_list.AnalysisTemplateArtifactList"
    ]
    """<p> Additional artifacts for the analysis template.</p>"""
    role_arn: "aws_sdk_cleanrooms.types.role_arn.RoleArn"
    """<p> The role ARN for the analysis template artifacts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateArtifacts) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.analysis_template_artifact

    out["entryPoint"] = (
        aws_sdk_cleanrooms.types.analysis_template_artifact.serialize_json(
            value["entry_point"]
        )
    )
    if "additional_artifacts" in value:
        import aws_sdk_cleanrooms.types.analysis_template_artifact_list

        out["additionalArtifacts"] = (
            aws_sdk_cleanrooms.types.analysis_template_artifact_list.serialize_json(
                value["additional_artifacts"]
            )
        )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> AnalysisTemplateArtifacts:
    out: AnalysisTemplateArtifacts = {}  # type: ignore[typeddict-item]
    if "entryPoint" in data:
        import aws_sdk_cleanrooms.types.analysis_template_artifact

        out["entry_point"] = (
            aws_sdk_cleanrooms.types.analysis_template_artifact.deserialize_json(
                data["entryPoint"]
            )
        )
    else:
        raise DeserializationError("AnalysisTemplateArtifacts.entry_point required")
    if "additionalArtifacts" in data:
        import aws_sdk_cleanrooms.types.analysis_template_artifact_list

        out["additional_artifacts"] = (
            aws_sdk_cleanrooms.types.analysis_template_artifact_list.deserialize_json(
                data["additionalArtifacts"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("AnalysisTemplateArtifacts.role_arn required")
    return out
