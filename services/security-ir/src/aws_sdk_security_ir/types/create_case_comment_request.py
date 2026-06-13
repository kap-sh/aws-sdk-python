"""Generated from Smithy shape ``com.amazonaws.securityir#CreateCaseCommentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.case_id
    import aws_sdk_security_ir.types.comment_body


class CreateCaseCommentRequest(TypedDict):
    case_id: "aws_sdk_security_ir.types.case_id.CaseId"
    """<p>Required element used in combination with CreateCaseComment to specify a case ID.</p>"""
    client_token: NotRequired["str"]
    """<note> <p>The <code>clientToken</code> field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided. </p> </note>"""
    body: "aws_sdk_security_ir.types.comment_body.CommentBody"
    """<p>Required element used in combination with CreateCaseComment to add content for the new comment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCaseCommentRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["body"] = value["body"]
    return out


def deserialize_json(data: dict) -> CreateCaseCommentRequest:
    out: CreateCaseCommentRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "body" in data:
        out["body"] = data["body"]
    else:
        raise DeserializationError("CreateCaseCommentRequest.body required")
    return out
