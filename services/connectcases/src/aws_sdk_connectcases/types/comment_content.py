"""Generated from Smithy shape ``com.amazonaws.connectcases#CommentContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.comment_body
    import aws_sdk_connectcases.types.comment_body_text_type


class CommentContent(TypedDict, closed=True):
    body: "aws_sdk_connectcases.types.comment_body.CommentBody"
    """<p>Text in the body of a <code>Comment</code> on a case.</p>"""
    content_type: (
        "aws_sdk_connectcases.types.comment_body_text_type.CommentBodyTextType"
    )
    """<p>Type of the text in the box of a <code>Comment</code> on a case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommentContent) -> dict:
    out: dict = {}
    out["body"] = value["body"]
    out["contentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> CommentContent:
    out: CommentContent = {}  # type: ignore[typeddict-item]
    if "body" in data:
        out["body"] = data["body"]
    else:
        raise DeserializationError("CommentContent.body required")
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError("CommentContent.content_type required")
    return out
