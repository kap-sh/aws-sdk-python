"""Generated from Smithy shape ``com.amazonaws.workdocs#Comment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.comment_id_type
    import aws_sdk_workdocs.types.comment_status_type
    import aws_sdk_workdocs.types.comment_text_type
    import aws_sdk_workdocs.types.comment_visibility_type
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.timestamp_type
    import aws_sdk_workdocs.types.user


class Comment(TypedDict):
    comment_id: "aws_sdk_workdocs.types.comment_id_type.CommentIdType"
    """<p>The ID of the comment.</p>"""
    parent_id: NotRequired["aws_sdk_workdocs.types.comment_id_type.CommentIdType"]
    """<p>The ID of the parent comment.</p>"""
    thread_id: NotRequired["aws_sdk_workdocs.types.comment_id_type.CommentIdType"]
    """<p>The ID of the root comment in the thread.</p>"""
    text: NotRequired["aws_sdk_workdocs.types.comment_text_type.CommentTextType"]
    """<p>The text of the comment.</p>"""
    contributor: NotRequired["aws_sdk_workdocs.types.user.User"]
    """<p>The details of the user who made the comment.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_workdocs.types.timestamp_type.TimestampType"
    ]
    """<p>The time that the comment was created.</p>"""
    status: NotRequired["aws_sdk_workdocs.types.comment_status_type.CommentStatusType"]
    """<p>The status of the comment.</p>"""
    visibility: NotRequired[
        "aws_sdk_workdocs.types.comment_visibility_type.CommentVisibilityType"
    ]
    """<p>The visibility of the comment. Options are either PRIVATE, where the comment is visible only to the comment author and document owner and co-owners, or PUBLIC, where the comment is visible to document owners, co-owners, and contributors.</p>"""
    recipient_id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>If the comment is a reply to another user's comment, this field contains the user ID of the user being replied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Comment) -> dict:
    out: dict = {}
    out["CommentId"] = value["comment_id"]
    if "parent_id" in value:
        out["ParentId"] = value["parent_id"]
    if "thread_id" in value:
        out["ThreadId"] = value["thread_id"]
    if "text" in value:
        out["Text"] = value["text"]
    if "contributor" in value:
        import aws_sdk_workdocs.types.user

        out["Contributor"] = aws_sdk_workdocs.types.user.serialize_json(
            value["contributor"]
        )
    if "created_timestamp" in value:
        import aws_sdk_workdocs.types.timestamp_type

        out["CreatedTimestamp"] = aws_sdk_workdocs.types.timestamp_type.serialize_json(
            value["created_timestamp"]
        )
    if "status" in value:
        import aws_sdk_workdocs.types.comment_status_type

        out["Status"] = aws_sdk_workdocs.types.comment_status_type.serialize_json(
            value["status"]
        )
    if "visibility" in value:
        import aws_sdk_workdocs.types.comment_visibility_type

        out["Visibility"] = (
            aws_sdk_workdocs.types.comment_visibility_type.serialize_json(
                value["visibility"]
            )
        )
    if "recipient_id" in value:
        out["RecipientId"] = value["recipient_id"]
    return out


def deserialize_json(data: dict) -> Comment:
    out: Comment = {}  # type: ignore[typeddict-item]
    if "CommentId" in data:
        out["comment_id"] = data["CommentId"]
    else:
        raise DeserializationError("Comment.comment_id required")
    if "ParentId" in data:
        out["parent_id"] = data["ParentId"]
    if "ThreadId" in data:
        out["thread_id"] = data["ThreadId"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Contributor" in data:
        import aws_sdk_workdocs.types.user

        out["contributor"] = aws_sdk_workdocs.types.user.deserialize_json(
            data["Contributor"]
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_workdocs.types.timestamp_type

        out["created_timestamp"] = (
            aws_sdk_workdocs.types.timestamp_type.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "Status" in data:
        import aws_sdk_workdocs.types.comment_status_type

        out["status"] = aws_sdk_workdocs.types.comment_status_type.deserialize_json(
            data["Status"]
        )
    if "Visibility" in data:
        import aws_sdk_workdocs.types.comment_visibility_type

        out["visibility"] = (
            aws_sdk_workdocs.types.comment_visibility_type.deserialize_json(
                data["Visibility"]
            )
        )
    if "RecipientId" in data:
        out["recipient_id"] = data["RecipientId"]
    return out
