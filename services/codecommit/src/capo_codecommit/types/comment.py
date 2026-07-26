"""Generated from Smithy shape ``com.amazonaws.codecommit#Comment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.arn
    import capo_codecommit.types.caller_reactions
    import capo_codecommit.types.client_request_token
    import capo_codecommit.types.comment_id
    import capo_codecommit.types.content
    import capo_codecommit.types.creation_date
    import capo_codecommit.types.is_comment_deleted
    import capo_codecommit.types.last_modified_date
    import capo_codecommit.types.reaction_counts_map


class Comment(TypedDict, closed=True):
    comment_id: NotRequired["capo_codecommit.types.comment_id.CommentId"]
    """<p>The system-generated comment ID.</p>"""
    content: NotRequired["capo_codecommit.types.content.Content"]
    """<p>The content of the comment.</p>"""
    in_reply_to: NotRequired["capo_codecommit.types.comment_id.CommentId"]
    """<p>The ID of the comment for which this comment is a reply, if any.</p>"""
    creation_date: NotRequired["capo_codecommit.types.creation_date.CreationDate"]
    """<p>The date and time the comment was created, in timestamp format.</p>"""
    last_modified_date: NotRequired[
        "capo_codecommit.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date and time the comment was most recently modified, in timestamp format.</p>"""
    author_arn: NotRequired["capo_codecommit.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the person who posted the comment.</p>"""
    deleted: "capo_codecommit.types.is_comment_deleted.IsCommentDeleted"
    """<p>A Boolean value indicating whether the comment has been deleted.</p>"""
    client_request_token: NotRequired[
        "capo_codecommit.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.</p>"""
    caller_reactions: NotRequired[
        "capo_codecommit.types.caller_reactions.CallerReactions"
    ]
    """<p>The emoji reactions to a comment, if any, submitted by the user whose credentials are associated with the call to the API.</p>"""
    reaction_counts: NotRequired[
        "capo_codecommit.types.reaction_counts_map.ReactionCountsMap"
    ]
    """<p>A string to integer map that represents the number of individual users who have responded to a comment with the specified reactions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Comment) -> dict:
    out: dict = {}
    if "comment_id" in value:
        out["commentId"] = value["comment_id"]
    if "content" in value:
        out["content"] = value["content"]
    if "in_reply_to" in value:
        out["inReplyTo"] = value["in_reply_to"]
    if "creation_date" in value:
        import capo_codecommit.types.creation_date

        out["creationDate"] = (
            capo_codecommit.types.creation_date.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "last_modified_date" in value:
        import capo_codecommit.types.last_modified_date

        out["lastModifiedDate"] = (
            capo_codecommit.types.last_modified_date.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    if "author_arn" in value:
        out["authorArn"] = value["author_arn"]
    out["deleted"] = value.get("deleted", False)
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "caller_reactions" in value:
        import capo_codecommit.types.caller_reactions

        out["callerReactions"] = (
            capo_codecommit.types.caller_reactions.serialize_aws_json_1_1(
                value["caller_reactions"]
            )
        )
    if "reaction_counts" in value:
        import capo_codecommit.types.reaction_counts_map

        out["reactionCounts"] = (
            capo_codecommit.types.reaction_counts_map.serialize_aws_json_1_1(
                value["reaction_counts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Comment:
    out: Comment = {}  # type: ignore[typeddict-item]
    if "commentId" in data:
        out["comment_id"] = data["commentId"]
    if "content" in data:
        out["content"] = data["content"]
    if "inReplyTo" in data:
        out["in_reply_to"] = data["inReplyTo"]
    if "creationDate" in data:
        import capo_codecommit.types.creation_date

        out["creation_date"] = (
            capo_codecommit.types.creation_date.deserialize_aws_json_1_1(
                data["creationDate"]
            )
        )
    if "lastModifiedDate" in data:
        import capo_codecommit.types.last_modified_date

        out["last_modified_date"] = (
            capo_codecommit.types.last_modified_date.deserialize_aws_json_1_1(
                data["lastModifiedDate"]
            )
        )
    if "authorArn" in data:
        out["author_arn"] = data["authorArn"]
    if "deleted" in data:
        out["deleted"] = data["deleted"]
    else:
        out["deleted"] = False
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "callerReactions" in data:
        import capo_codecommit.types.caller_reactions

        out["caller_reactions"] = (
            capo_codecommit.types.caller_reactions.deserialize_aws_json_1_1(
                data["callerReactions"]
            )
        )
    if "reactionCounts" in data:
        import capo_codecommit.types.reaction_counts_map

        out["reaction_counts"] = (
            capo_codecommit.types.reaction_counts_map.deserialize_aws_json_1_1(
                data["reactionCounts"]
            )
        )
    return out
