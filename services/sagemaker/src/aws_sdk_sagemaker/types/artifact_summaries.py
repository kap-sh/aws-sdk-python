"""Generated from Smithy shape ``com.amazonaws.sagemaker#ArtifactSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.artifact_summary

ArtifactSummaries: TypeAlias = list[
    "aws_sdk_sagemaker.types.artifact_summary.ArtifactSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactSummaries) -> list:
    import aws_sdk_sagemaker.types.artifact_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.artifact_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ArtifactSummaries:
    import aws_sdk_sagemaker.types.artifact_summary

    out: ArtifactSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.artifact_summary.deserialize_aws_json_1_1(item)
        )
    return out
