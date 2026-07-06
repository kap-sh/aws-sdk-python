"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitPushFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.git_branch_filter_criteria
    import aws_sdk_codepipeline.types.git_file_path_filter_criteria
    import aws_sdk_codepipeline.types.git_tag_filter_criteria


class GitPushFilter(TypedDict, closed=True):
    tags: NotRequired[
        "aws_sdk_codepipeline.types.git_tag_filter_criteria.GitTagFilterCriteria"
    ]
    """<p>The field that contains the details for the Git tags trigger configuration.</p>"""
    branches: NotRequired[
        "aws_sdk_codepipeline.types.git_branch_filter_criteria.GitBranchFilterCriteria"
    ]
    """<p>The field that specifies to filter on branches for the push trigger configuration.</p>"""
    file_paths: NotRequired[
        "aws_sdk_codepipeline.types.git_file_path_filter_criteria.GitFilePathFilterCriteria"
    ]
    """<p>The field that specifies to filter on file paths for the push trigger configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitPushFilter) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_codepipeline.types.git_tag_filter_criteria

        out["tags"] = (
            aws_sdk_codepipeline.types.git_tag_filter_criteria.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    if "branches" in value:
        import aws_sdk_codepipeline.types.git_branch_filter_criteria

        out["branches"] = (
            aws_sdk_codepipeline.types.git_branch_filter_criteria.serialize_aws_json_1_1(
                value["branches"]
            )
        )
    if "file_paths" in value:
        import aws_sdk_codepipeline.types.git_file_path_filter_criteria

        out["filePaths"] = (
            aws_sdk_codepipeline.types.git_file_path_filter_criteria.serialize_aws_json_1_1(
                value["file_paths"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GitPushFilter:
    out: GitPushFilter = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_codepipeline.types.git_tag_filter_criteria

        out["tags"] = (
            aws_sdk_codepipeline.types.git_tag_filter_criteria.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    if "branches" in data:
        import aws_sdk_codepipeline.types.git_branch_filter_criteria

        out["branches"] = (
            aws_sdk_codepipeline.types.git_branch_filter_criteria.deserialize_aws_json_1_1(
                data["branches"]
            )
        )
    if "filePaths" in data:
        import aws_sdk_codepipeline.types.git_file_path_filter_criteria

        out["file_paths"] = (
            aws_sdk_codepipeline.types.git_file_path_filter_criteria.deserialize_aws_json_1_1(
                data["filePaths"]
            )
        )
    return out
