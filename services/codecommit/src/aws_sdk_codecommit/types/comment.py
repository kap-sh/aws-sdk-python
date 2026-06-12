"""Generated from Smithy shape ``com.amazonaws.codecommit#Comment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.arn
    import aws_sdk_codecommit.types.caller_reactions
    import aws_sdk_codecommit.types.client_request_token
    import aws_sdk_codecommit.types.comment_id
    import aws_sdk_codecommit.types.content
    import aws_sdk_codecommit.types.creation_date
    import aws_sdk_codecommit.types.is_comment_deleted
    import aws_sdk_codecommit.types.last_modified_date
    import aws_sdk_codecommit.types.reaction_counts_map


class Comment(TypedDict):
    comment_id: NotRequired["aws_sdk_codecommit.types.comment_id.CommentId"]
    """<p>The system-generated comment ID.</p>"""
    content: NotRequired["aws_sdk_codecommit.types.content.Content"]
    """<p>The content of the comment.</p>"""
    in_reply_to: NotRequired["aws_sdk_codecommit.types.comment_id.CommentId"]
    """<p>The ID of the comment for which this comment is a reply, if any.</p>"""
    creation_date: NotRequired["aws_sdk_codecommit.types.creation_date.CreationDate"]
    """<p>The date and time the comment was created, in timestamp format.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_codecommit.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date and time the comment was most recently modified, in timestamp format.</p>"""
    author_arn: NotRequired["aws_sdk_codecommit.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the person who posted the comment.</p>"""
    deleted: "aws_sdk_codecommit.types.is_comment_deleted.IsCommentDeleted"
    """<p>A Boolean value indicating whether the comment has been deleted.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_codecommit.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.</p>"""
    caller_reactions: NotRequired[
        "aws_sdk_codecommit.types.caller_reactions.CallerReactions"
    ]
    """<p>The emoji reactions to a comment, if any, submitted by the user whose credentials are associated with the call to the API.</p>"""
    reaction_counts: NotRequired[
        "aws_sdk_codecommit.types.reaction_counts_map.ReactionCountsMap"
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
        import aws_sdk_codecommit.types.creation_date

        out["creationDate"] = (
            aws_sdk_codecommit.types.creation_date.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "last_modified_date" in value:
        import aws_sdk_codecommit.types.last_modified_date

        out["lastModifiedDate"] = (
            aws_sdk_codecommit.types.last_modified_date.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    if "author_arn" in value:
        out["authorArn"] = value["author_arn"]
    out["deleted"] = value.get("deleted", False)
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "caller_reactions" in value:
        import aws_sdk_codecommit.types.caller_reactions

        out["callerReactions"] = (
            aws_sdk_codecommit.types.caller_reactions.serialize_aws_json_1_1(
                value["caller_reactions"]
            )
        )
    if "reaction_counts" in value:
        import aws_sdk_codecommit.types.reaction_counts_map

        out["reactionCounts"] = (
            aws_sdk_codecommit.types.reaction_counts_map.serialize_aws_json_1_1(
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
        import aws_sdk_codecommit.types.creation_date

        out["creation_date"] = (
            aws_sdk_codecommit.types.creation_date.deserialize_aws_json_1_1(
                data["creationDate"]
            )
        )
    if "lastModifiedDate" in data:
        import aws_sdk_codecommit.types.last_modified_date

        out["last_modified_date"] = (
            aws_sdk_codecommit.types.last_modified_date.deserialize_aws_json_1_1(
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
        import aws_sdk_codecommit.types.caller_reactions

        out["caller_reactions"] = (
            aws_sdk_codecommit.types.caller_reactions.deserialize_aws_json_1_1(
                data["callerReactions"]
            )
        )
    if "reactionCounts" in data:
        import aws_sdk_codecommit.types.reaction_counts_map

        out["reaction_counts"] = (
            aws_sdk_codecommit.types.reaction_counts_map.deserialize_aws_json_1_1(
                data["reactionCounts"]
            )
        )
    return out
