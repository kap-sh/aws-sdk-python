"""Generated from Smithy shape ``com.amazonaws.workdocs#CommentMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.comment_id_type
    import aws_sdk_workdocs.types.comment_status_type
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.timestamp_type
    import aws_sdk_workdocs.types.user


class CommentMetadata(TypedDict, closed=True):
    comment_id: NotRequired["aws_sdk_workdocs.types.comment_id_type.CommentIdType"]
    """<p>The ID of the comment.</p>"""
    contributor: NotRequired["aws_sdk_workdocs.types.user.User"]
    """<p>The user who made the comment.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_workdocs.types.timestamp_type.TimestampType"
    ]
    """<p>The timestamp that the comment was created.</p>"""
    comment_status: NotRequired[
        "aws_sdk_workdocs.types.comment_status_type.CommentStatusType"
    ]
    """<p>The status of the comment.</p>"""
    recipient_id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>The ID of the user being replied to.</p>"""
    contributor_id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>The ID of the user who made the comment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommentMetadata) -> dict:
    out: dict = {}
    if "comment_id" in value:
        out["CommentId"] = value["comment_id"]
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
    if "comment_status" in value:
        import aws_sdk_workdocs.types.comment_status_type

        out["CommentStatus"] = (
            aws_sdk_workdocs.types.comment_status_type.serialize_json(
                value["comment_status"]
            )
        )
    if "recipient_id" in value:
        out["RecipientId"] = value["recipient_id"]
    if "contributor_id" in value:
        out["ContributorId"] = value["contributor_id"]
    return out


def deserialize_json(data: dict) -> CommentMetadata:
    out: CommentMetadata = {}  # type: ignore[typeddict-item]
    if "CommentId" in data:
        out["comment_id"] = data["CommentId"]
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
    if "CommentStatus" in data:
        import aws_sdk_workdocs.types.comment_status_type

        out["comment_status"] = (
            aws_sdk_workdocs.types.comment_status_type.deserialize_json(
                data["CommentStatus"]
            )
        )
    if "RecipientId" in data:
        out["recipient_id"] = data["RecipientId"]
    if "ContributorId" in data:
        out["contributor_id"] = data["ContributorId"]
    return out
