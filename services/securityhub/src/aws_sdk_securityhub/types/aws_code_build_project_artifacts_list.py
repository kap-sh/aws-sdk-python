"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectArtifactsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_code_build_project_artifacts_details

AwsCodeBuildProjectArtifactsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_code_build_project_artifacts_details.AwsCodeBuildProjectArtifactsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsCodeBuildProjectArtifactsList) -> list:
    import aws_sdk_securityhub.types.aws_code_build_project_artifacts_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_code_build_project_artifacts_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsCodeBuildProjectArtifactsList:
    import aws_sdk_securityhub.types.aws_code_build_project_artifacts_details

    out: AwsCodeBuildProjectArtifactsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_code_build_project_artifacts_details.deserialize_json(
                item
            )
        )
    return out
