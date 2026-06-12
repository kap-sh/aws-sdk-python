"""Generated from Smithy shape ``com.amazonaws.auditmanager#DeleteAssessmentFrameworkShareRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.share_request_type
    import aws_sdk_auditmanager.types.uuid


class DeleteAssessmentFrameworkShareRequest(TypedDict):
    request_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p>The unique identifier for the share request to be deleted.</p>"""
    request_type: "aws_sdk_auditmanager.types.share_request_type.ShareRequestType"
    """<p>Specifies whether the share request is a sent request or a received request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssessmentFrameworkShareRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssessmentFrameworkShareRequest:
    out: DeleteAssessmentFrameworkShareRequest = {}  # type: ignore[typeddict-item]
    return out
