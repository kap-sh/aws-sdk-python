"""Generated from Smithy shape ``com.amazonaws.codecommit#PostCommentReplyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.client_request_token
    import capo_codecommit.types.comment_id
    import capo_codecommit.types.content


class PostCommentReplyInput(TypedDict, closed=True):
    in_reply_to: "capo_codecommit.types.comment_id.CommentId"
    """<p>The system-generated ID of the comment to which you want to reply. To get this ID, use <a>GetCommentsForComparedCommit</a> or <a>GetCommentsForPullRequest</a>.</p>"""
    client_request_token: NotRequired[
        "capo_codecommit.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.</p>"""
    content: "capo_codecommit.types.content.Content"
    """<p>The contents of your reply to a comment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PostCommentReplyInput) -> dict:
    out: dict = {}
    out["inReplyTo"] = value["in_reply_to"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["content"] = value["content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PostCommentReplyInput:
    out: PostCommentReplyInput = {}  # type: ignore[typeddict-item]
    if "inReplyTo" in data:
        out["in_reply_to"] = data["inReplyTo"]
    else:
        raise DeserializationError("PostCommentReplyInput.in_reply_to required")
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "content" in data:
        out["content"] = data["content"]
    else:
        raise DeserializationError("PostCommentReplyInput.content required")
    return out
