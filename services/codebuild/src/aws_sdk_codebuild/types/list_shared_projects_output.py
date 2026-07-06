"""Generated from Smithy shape ``com.amazonaws.codebuild#ListSharedProjectsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.project_arns
    import aws_sdk_codebuild.types.string


class ListSharedProjectsOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>"""
    projects: NotRequired["aws_sdk_codebuild.types.project_arns.ProjectArns"]
    """<p> The list of ARNs for the build projects shared with the current Amazon Web Services account or user. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSharedProjectsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "projects" in value:
        import aws_sdk_codebuild.types.project_arns

        out["projects"] = aws_sdk_codebuild.types.project_arns.serialize_aws_json_1_1(
            value["projects"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSharedProjectsOutput:
    out: ListSharedProjectsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "projects" in data:
        import aws_sdk_codebuild.types.project_arns

        out["projects"] = aws_sdk_codebuild.types.project_arns.deserialize_aws_json_1_1(
            data["projects"]
        )
    return out
