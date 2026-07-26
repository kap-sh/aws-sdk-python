"""Generated from Smithy shape ``com.amazonaws.securityir#ListCommentsItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_security_ir.types.comment_body
    import capo_security_ir.types.comment_id
    import capo_security_ir.types.principal_id


class ListCommentsItem(TypedDict, closed=True):
    comment_id: "capo_security_ir.types.comment_id.CommentId"
    """<p/>"""
    created_date: NotRequired["datetime.datetime"]
    """<p/>"""
    last_updated_date: NotRequired["datetime.datetime"]
    """<p/>"""
    creator: NotRequired["capo_security_ir.types.principal_id.PrincipalId"]
    """<p/>"""
    last_updated_by: NotRequired["capo_security_ir.types.principal_id.PrincipalId"]
    """<p/>"""
    body: NotRequired["capo_security_ir.types.comment_body.CommentBody"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCommentsItem) -> dict:
    out: dict = {}
    out["commentId"] = value["comment_id"]
    if "created_date" in value:
        import capo_security_ir.types._prelude.timestamp

        out["createdDate"] = capo_security_ir.types._prelude.timestamp.serialize_json(
            value["created_date"]
        )
    if "last_updated_date" in value:
        import capo_security_ir.types._prelude.timestamp

        out["lastUpdatedDate"] = (
            capo_security_ir.types._prelude.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "creator" in value:
        out["creator"] = value["creator"]
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    if "body" in value:
        out["body"] = value["body"]
    return out


def deserialize_json(data: dict) -> ListCommentsItem:
    out: ListCommentsItem = {}  # type: ignore[typeddict-item]
    if "commentId" in data:
        out["comment_id"] = data["commentId"]
    else:
        raise DeserializationError("ListCommentsItem.comment_id required")
    if "createdDate" in data:
        import capo_security_ir.types._prelude.timestamp

        out["created_date"] = (
            capo_security_ir.types._prelude.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if "lastUpdatedDate" in data:
        import capo_security_ir.types._prelude.timestamp

        out["last_updated_date"] = (
            capo_security_ir.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if "creator" in data:
        out["creator"] = data["creator"]
    if "lastUpdatedBy" in data:
        out["last_updated_by"] = data["lastUpdatedBy"]
    if "body" in data:
        out["body"] = data["body"]
    return out
