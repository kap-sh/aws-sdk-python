"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlComment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_comment_body
    import aws_sdk_auditmanager.types.timestamp
    import aws_sdk_auditmanager.types.username


class ControlComment(TypedDict, closed=True):
    author_name: NotRequired["aws_sdk_auditmanager.types.username.Username"]
    """<p> The name of the user who authored the comment. </p>"""
    comment_body: NotRequired[
        "aws_sdk_auditmanager.types.control_comment_body.ControlCommentBody"
    ]
    """<p> The body text of a control comment. </p>"""
    posted_date: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the comment was posted. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlComment) -> dict:
    out: dict = {}
    if "author_name" in value:
        out["authorName"] = value["author_name"]
    if "comment_body" in value:
        out["commentBody"] = value["comment_body"]
    if "posted_date" in value:
        import aws_sdk_auditmanager.types.timestamp

        out["postedDate"] = aws_sdk_auditmanager.types.timestamp.serialize_json(
            value["posted_date"]
        )
    return out


def deserialize_json(data: dict) -> ControlComment:
    out: ControlComment = {}  # type: ignore[typeddict-item]
    if "authorName" in data:
        out["author_name"] = data["authorName"]
    if "commentBody" in data:
        out["comment_body"] = data["commentBody"]
    if "postedDate" in data:
        import aws_sdk_auditmanager.types.timestamp

        out["posted_date"] = aws_sdk_auditmanager.types.timestamp.deserialize_json(
            data["postedDate"]
        )
    return out
