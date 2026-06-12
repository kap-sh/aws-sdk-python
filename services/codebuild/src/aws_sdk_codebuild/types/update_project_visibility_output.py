"""Generated from Smithy shape ``com.amazonaws.codebuild#UpdateProjectVisibilityOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.project_visibility_type


class UpdateProjectVisibilityOutput(TypedDict):
    project_arn: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the build project.</p>"""
    public_project_alias: NotRequired[
        "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>Contains the project identifier used with the public build APIs. </p>"""
    project_visibility: NotRequired[
        "aws_sdk_codebuild.types.project_visibility_type.ProjectVisibilityType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProjectVisibilityOutput) -> dict:
    out: dict = {}
    if "project_arn" in value:
        out["projectArn"] = value["project_arn"]
    if "public_project_alias" in value:
        out["publicProjectAlias"] = value["public_project_alias"]
    if "project_visibility" in value:
        import aws_sdk_codebuild.types.project_visibility_type

        out["projectVisibility"] = (
            aws_sdk_codebuild.types.project_visibility_type.serialize_aws_json_1_1(
                value["project_visibility"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProjectVisibilityOutput:
    out: UpdateProjectVisibilityOutput = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    if "publicProjectAlias" in data:
        out["public_project_alias"] = data["publicProjectAlias"]
    if "projectVisibility" in data:
        import aws_sdk_codebuild.types.project_visibility_type

        out["project_visibility"] = (
            aws_sdk_codebuild.types.project_visibility_type.deserialize_aws_json_1_1(
                data["projectVisibility"]
            )
        )
    return out
