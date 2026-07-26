"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitPullRequestEventTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.git_pull_request_event_type

GitPullRequestEventTypeList: TypeAlias = list[
    "capo_codepipeline.types.git_pull_request_event_type.GitPullRequestEventType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitPullRequestEventTypeList) -> list:
    import capo_codepipeline.types.git_pull_request_event_type

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.git_pull_request_event_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GitPullRequestEventTypeList:
    import capo_codepipeline.types.git_pull_request_event_type

    out: GitPullRequestEventTypeList = []
    for item in data:
        out.append(
            capo_codepipeline.types.git_pull_request_event_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
