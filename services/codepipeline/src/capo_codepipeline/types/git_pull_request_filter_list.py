"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitPullRequestFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.git_pull_request_filter

GitPullRequestFilterList: TypeAlias = list[
    "capo_codepipeline.types.git_pull_request_filter.GitPullRequestFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitPullRequestFilterList) -> list:
    import capo_codepipeline.types.git_pull_request_filter

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.git_pull_request_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GitPullRequestFilterList:
    import capo_codepipeline.types.git_pull_request_filter

    out: GitPullRequestFilterList = []
    for item in data:
        out.append(
            capo_codepipeline.types.git_pull_request_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
