"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitPullRequestFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.git_branch_filter_criteria
    import capo_codepipeline.types.git_file_path_filter_criteria
    import capo_codepipeline.types.git_pull_request_event_type_list


class GitPullRequestFilter(TypedDict, closed=True):
    events: NotRequired[
        "capo_codepipeline.types.git_pull_request_event_type_list.GitPullRequestEventTypeList"
    ]
    """<p>The field that specifies which pull request events to filter on (OPEN, UPDATED, CLOSED) for the trigger configuration.</p>"""
    branches: NotRequired[
        "capo_codepipeline.types.git_branch_filter_criteria.GitBranchFilterCriteria"
    ]
    """<p>The field that specifies to filter on branches for the pull request trigger configuration.</p>"""
    file_paths: NotRequired[
        "capo_codepipeline.types.git_file_path_filter_criteria.GitFilePathFilterCriteria"
    ]
    """<p>The field that specifies to filter on file paths for the pull request trigger configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitPullRequestFilter) -> dict:
    out: dict = {}
    if "events" in value:
        import capo_codepipeline.types.git_pull_request_event_type_list

        out["events"] = (
            capo_codepipeline.types.git_pull_request_event_type_list.serialize_aws_json_1_1(
                value["events"]
            )
        )
    if "branches" in value:
        import capo_codepipeline.types.git_branch_filter_criteria

        out["branches"] = (
            capo_codepipeline.types.git_branch_filter_criteria.serialize_aws_json_1_1(
                value["branches"]
            )
        )
    if "file_paths" in value:
        import capo_codepipeline.types.git_file_path_filter_criteria

        out["filePaths"] = (
            capo_codepipeline.types.git_file_path_filter_criteria.serialize_aws_json_1_1(
                value["file_paths"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GitPullRequestFilter:
    out: GitPullRequestFilter = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import capo_codepipeline.types.git_pull_request_event_type_list

        out["events"] = (
            capo_codepipeline.types.git_pull_request_event_type_list.deserialize_aws_json_1_1(
                data["events"]
            )
        )
    if "branches" in data:
        import capo_codepipeline.types.git_branch_filter_criteria

        out["branches"] = (
            capo_codepipeline.types.git_branch_filter_criteria.deserialize_aws_json_1_1(
                data["branches"]
            )
        )
    if "filePaths" in data:
        import capo_codepipeline.types.git_file_path_filter_criteria

        out["file_paths"] = (
            capo_codepipeline.types.git_file_path_filter_criteria.deserialize_aws_json_1_1(
                data["filePaths"]
            )
        )
    return out
