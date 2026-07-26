"""Generated from Smithy shape ``com.amazonaws.codecommit#GetCommentsForPullRequestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.comments_for_pull_request_data
    import capo_codecommit.types.next_token


class GetCommentsForPullRequestOutput(TypedDict, closed=True):
    comments_for_pull_request_data: NotRequired[
        "capo_codecommit.types.comments_for_pull_request_data.CommentsForPullRequestData"
    ]
    """<p>An array of comment objects on the pull request.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommentsForPullRequestOutput) -> dict:
    out: dict = {}
    if "comments_for_pull_request_data" in value:
        import capo_codecommit.types.comments_for_pull_request_data

        out["commentsForPullRequestData"] = (
            capo_codecommit.types.comments_for_pull_request_data.serialize_aws_json_1_1(
                value["comments_for_pull_request_data"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommentsForPullRequestOutput:
    out: GetCommentsForPullRequestOutput = {}  # type: ignore[typeddict-item]
    if "commentsForPullRequestData" in data:
        import capo_codecommit.types.comments_for_pull_request_data

        out["comments_for_pull_request_data"] = (
            capo_codecommit.types.comments_for_pull_request_data.deserialize_aws_json_1_1(
                data["commentsForPullRequestData"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
