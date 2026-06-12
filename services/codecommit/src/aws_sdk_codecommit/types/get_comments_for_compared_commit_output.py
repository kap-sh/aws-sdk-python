"""Generated from Smithy shape ``com.amazonaws.codecommit#GetCommentsForComparedCommitOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.comments_for_compared_commit_data
    import aws_sdk_codecommit.types.next_token


class GetCommentsForComparedCommitOutput(TypedDict):
    comments_for_compared_commit_data: NotRequired[
        "aws_sdk_codecommit.types.comments_for_compared_commit_data.CommentsForComparedCommitData"
    ]
    """<p>A list of comment objects on the compared commit.</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommentsForComparedCommitOutput) -> dict:
    out: dict = {}
    if "comments_for_compared_commit_data" in value:
        import aws_sdk_codecommit.types.comments_for_compared_commit_data

        out["commentsForComparedCommitData"] = (
            aws_sdk_codecommit.types.comments_for_compared_commit_data.serialize_aws_json_1_1(
                value["comments_for_compared_commit_data"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommentsForComparedCommitOutput:
    out: GetCommentsForComparedCommitOutput = {}  # type: ignore[typeddict-item]
    if "commentsForComparedCommitData" in data:
        import aws_sdk_codecommit.types.comments_for_compared_commit_data

        out["comments_for_compared_commit_data"] = (
            aws_sdk_codecommit.types.comments_for_compared_commit_data.deserialize_aws_json_1_1(
                data["commentsForComparedCommitData"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
