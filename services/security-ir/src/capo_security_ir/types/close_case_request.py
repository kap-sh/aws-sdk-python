"""Generated from Smithy shape ``com.amazonaws.securityir#CloseCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.case_id


class CloseCaseRequest(TypedDict, closed=True):
    case_id: "capo_security_ir.types.case_id.CaseId"
    """<p>Required element used in combination with CloseCase to identify the case ID to close.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloseCaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CloseCaseRequest:
    out: CloseCaseRequest = {}  # type: ignore[typeddict-item]
    return out
