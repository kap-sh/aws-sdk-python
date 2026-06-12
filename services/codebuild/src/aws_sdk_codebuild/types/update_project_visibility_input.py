"""Generated from Smithy shape ``com.amazonaws.codebuild#UpdateProjectVisibilityInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.project_visibility_type


class UpdateProjectVisibilityInput(TypedDict):
    project_arn: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Resource Name (ARN) of the build project.</p>"""
    project_visibility: (
        "aws_sdk_codebuild.types.project_visibility_type.ProjectVisibilityType"
    )
    resource_access_role: NotRequired[
        "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the IAM role that enables CodeBuild to access the CloudWatch Logs and Amazon S3 artifacts for the project's builds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProjectVisibilityInput) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    import aws_sdk_codebuild.types.project_visibility_type

    out["projectVisibility"] = (
        aws_sdk_codebuild.types.project_visibility_type.serialize_aws_json_1_1(
            value["project_visibility"]
        )
    )
    if "resource_access_role" in value:
        out["resourceAccessRole"] = value["resource_access_role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProjectVisibilityInput:
    out: UpdateProjectVisibilityInput = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("UpdateProjectVisibilityInput.project_arn required")
    if "projectVisibility" in data:
        import aws_sdk_codebuild.types.project_visibility_type

        out["project_visibility"] = (
            aws_sdk_codebuild.types.project_visibility_type.deserialize_aws_json_1_1(
                data["projectVisibility"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateProjectVisibilityInput.project_visibility required"
        )
    if "resourceAccessRole" in data:
        out["resource_access_role"] = data["resourceAccessRole"]
    return out
