"""Generated from Smithy shape ``com.amazonaws.codebuild#ListProjectsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.project_names
    import aws_sdk_codebuild.types.string


class ListProjectsOutput(TypedDict):
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a <i>nextToken</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call.</p>"""
    projects: NotRequired["aws_sdk_codebuild.types.project_names.ProjectNames"]
    """<p>The list of build project names, with each build project name representing a single build project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProjectsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "projects" in value:
        import aws_sdk_codebuild.types.project_names

        out["projects"] = aws_sdk_codebuild.types.project_names.serialize_aws_json_1_1(
            value["projects"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProjectsOutput:
    out: ListProjectsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "projects" in data:
        import aws_sdk_codebuild.types.project_names

        out["projects"] = (
            aws_sdk_codebuild.types.project_names.deserialize_aws_json_1_1(
                data["projects"]
            )
        )
    return out
