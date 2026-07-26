"""Generated from Smithy shape ``com.amazonaws.securityir#UpdateCaseCommentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import capo_security_ir.types.case_id
    import capo_security_ir.types.comment_body
    import capo_security_ir.types.comment_id


class UpdateCaseCommentRequest(TypedDict, closed=True):
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p>Required element for UpdateCaseComment to identify the case ID containing the comment to be updated. </p>"""
    comment_id: "capo_security_ir.types.comment_id.CommentId"
    """<p>Required element for UpdateCaseComment to identify the case ID to be updated.</p>"""
    body: "capo_security_ir.types.comment_body.CommentBody"
    """<p>Required element for UpdateCaseComment to identify the content for the comment to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCaseCommentRequest) -> dict:
    out: dict = {}
    out["body"] = value["body"]
    return out


def deserialize_json(data: dict) -> UpdateCaseCommentRequest:
    out: UpdateCaseCommentRequest = {}  # type: ignore[typeddict-item]
    if "body" in data:
        out["body"] = data["body"]
    else:
        raise DeserializationError("UpdateCaseCommentRequest.body required")
    return out
