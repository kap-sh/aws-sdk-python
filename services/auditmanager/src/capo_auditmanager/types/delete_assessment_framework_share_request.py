"""Generated from Smithy shape ``com.amazonaws.auditmanager#DeleteAssessmentFrameworkShareRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.share_request_type
    import capo_auditmanager.types.uuid


class DeleteAssessmentFrameworkShareRequest(TypedDict, closed=True):
    request_id: "capo_auditmanager.types.uuid.UUID"
    """<p>The unique identifier for the share request to be deleted.</p>"""
    request_type: "capo_auditmanager.types.share_request_type.ShareRequestType"
    """<p>Specifies whether the share request is a sent request or a received request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssessmentFrameworkShareRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssessmentFrameworkShareRequest:
    out: DeleteAssessmentFrameworkShareRequest = {}  # type: ignore[typeddict-item]
    return out
