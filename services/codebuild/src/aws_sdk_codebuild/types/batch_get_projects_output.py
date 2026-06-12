"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetProjectsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.project_names
    import aws_sdk_codebuild.types.projects


class BatchGetProjectsOutput(TypedDict):
    projects: NotRequired["aws_sdk_codebuild.types.projects.Projects"]
    """<p>Information about the requested build projects.</p>"""
    projects_not_found: NotRequired[
        "aws_sdk_codebuild.types.project_names.ProjectNames"
    ]
    """<p>The names of build projects for which information could not be found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetProjectsOutput) -> dict:
    out: dict = {}
    if "projects" in value:
        import aws_sdk_codebuild.types.projects

        out["projects"] = aws_sdk_codebuild.types.projects.serialize_aws_json_1_1(
            value["projects"]
        )
    if "projects_not_found" in value:
        import aws_sdk_codebuild.types.project_names

        out["projectsNotFound"] = (
            aws_sdk_codebuild.types.project_names.serialize_aws_json_1_1(
                value["projects_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetProjectsOutput:
    out: BatchGetProjectsOutput = {}  # type: ignore[typeddict-item]
    if "projects" in data:
        import aws_sdk_codebuild.types.projects

        out["projects"] = aws_sdk_codebuild.types.projects.deserialize_aws_json_1_1(
            data["projects"]
        )
    if "projectsNotFound" in data:
        import aws_sdk_codebuild.types.project_names

        out["projects_not_found"] = (
            aws_sdk_codebuild.types.project_names.deserialize_aws_json_1_1(
                data["projectsNotFound"]
            )
        )
    return out
