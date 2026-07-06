"""Generated from Smithy shape ``com.amazonaws.codecommit#GetCommentReactionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.next_token
    import aws_sdk_codecommit.types.reactions_for_comment_list


class GetCommentReactionsOutput(TypedDict, closed=True):
    reactions_for_comment: (
        "aws_sdk_codecommit.types.reactions_for_comment_list.ReactionsForCommentList"
    )
    """<p>An array of reactions to the specified comment.</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommentReactionsOutput) -> dict:
    out: dict = {}
    import aws_sdk_codecommit.types.reactions_for_comment_list

    out["reactionsForComment"] = (
        aws_sdk_codecommit.types.reactions_for_comment_list.serialize_aws_json_1_1(
            value["reactions_for_comment"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommentReactionsOutput:
    out: GetCommentReactionsOutput = {}  # type: ignore[typeddict-item]
    if "reactionsForComment" in data:
        import aws_sdk_codecommit.types.reactions_for_comment_list

        out["reactions_for_comment"] = (
            aws_sdk_codecommit.types.reactions_for_comment_list.deserialize_aws_json_1_1(
                data["reactionsForComment"]
            )
        )
    else:
        raise DeserializationError(
            "GetCommentReactionsOutput.reactions_for_comment required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
