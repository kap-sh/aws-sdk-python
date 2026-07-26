"""Generated from Smithy shape ``com.amazonaws.sagemaker#ArtifactSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.artifact_summary

ArtifactSummaries: TypeAlias = list[
    "capo_sagemaker.types.artifact_summary.ArtifactSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactSummaries) -> list:
    import capo_sagemaker.types.artifact_summary

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.artifact_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ArtifactSummaries:
    import capo_sagemaker.types.artifact_summary

    out: ArtifactSummaries = []
    for item in data:
        out.append(capo_sagemaker.types.artifact_summary.deserialize_aws_json_1_1(item))
    return out
