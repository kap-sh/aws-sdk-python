"""Generated from Smithy shape ``com.amazonaws.codecommit#GetCommentReactionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.arn
    import aws_sdk_codecommit.types.comment_id
    import aws_sdk_codecommit.types.max_results
    import aws_sdk_codecommit.types.next_token


class GetCommentReactionsInput(TypedDict, closed=True):
    comment_id: "aws_sdk_codecommit.types.comment_id.CommentId"
    """<p>The ID of the comment for which you want to get reactions information.</p>"""
    reaction_user_arn: NotRequired["aws_sdk_codecommit.types.arn.Arn"]
    """<p>Optional. The Amazon Resource Name (ARN) of the user or identity for which you want to get reaction information.</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that, when provided in a request, returns the next batch of the results. </p>"""
    max_results: NotRequired["aws_sdk_codecommit.types.max_results.MaxResults"]
    """<p>A non-zero, non-negative integer used to limit the number of returned results. The default is the same as the allowed maximum, 1,000.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommentReactionsInput) -> dict:
    out: dict = {}
    out["commentId"] = value["comment_id"]
    if "reaction_user_arn" in value:
        out["reactionUserArn"] = value["reaction_user_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommentReactionsInput:
    out: GetCommentReactionsInput = {}  # type: ignore[typeddict-item]
    if "commentId" in data:
        out["comment_id"] = data["commentId"]
    else:
        raise DeserializationError("GetCommentReactionsInput.comment_id required")
    if "reactionUserArn" in data:
        out["reaction_user_arn"] = data["reactionUserArn"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
