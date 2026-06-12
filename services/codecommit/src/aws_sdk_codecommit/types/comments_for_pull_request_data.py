"""Generated from Smithy shape ``com.amazonaws.codecommit#CommentsForPullRequestData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.comments_for_pull_request

CommentsForPullRequestData: TypeAlias = list[
    "aws_sdk_codecommit.types.comments_for_pull_request.CommentsForPullRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommentsForPullRequestData) -> list:
    import aws_sdk_codecommit.types.comments_for_pull_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecommit.types.comments_for_pull_request.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CommentsForPullRequestData:
    import aws_sdk_codecommit.types.comments_for_pull_request

    out: CommentsForPullRequestData = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.comments_for_pull_request.deserialize_aws_json_1_1(
                item
            )
        )
    return out
