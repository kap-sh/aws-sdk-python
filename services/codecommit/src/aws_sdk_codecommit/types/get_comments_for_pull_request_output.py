"""Generated from Smithy shape ``com.amazonaws.codecommit#GetCommentsForPullRequestOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.comments_for_pull_request_data
    import aws_sdk_codecommit.types.next_token


class GetCommentsForPullRequestOutput(TypedDict):
    comments_for_pull_request_data: NotRequired[
        "aws_sdk_codecommit.types.comments_for_pull_request_data.CommentsForPullRequestData"
    ]
    """<p>An array of comment objects on the pull request.</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommentsForPullRequestOutput) -> dict:
    out: dict = {}
    if "comments_for_pull_request_data" in value:
        import aws_sdk_codecommit.types.comments_for_pull_request_data

        out["commentsForPullRequestData"] = (
            aws_sdk_codecommit.types.comments_for_pull_request_data.serialize_aws_json_1_1(
                value["comments_for_pull_request_data"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommentsForPullRequestOutput:
    out: GetCommentsForPullRequestOutput = {}  # type: ignore[typeddict-item]
    if "commentsForPullRequestData" in data:
        import aws_sdk_codecommit.types.comments_for_pull_request_data

        out["comments_for_pull_request_data"] = (
            aws_sdk_codecommit.types.comments_for_pull_request_data.deserialize_aws_json_1_1(
                data["commentsForPullRequestData"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
