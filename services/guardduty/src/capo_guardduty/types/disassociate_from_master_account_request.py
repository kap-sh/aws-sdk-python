"""Generated from Smithy shape ``com.amazonaws.guardduty#DisassociateFromMasterAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id


class DisassociateFromMasterAccountRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector of the GuardDuty member account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateFromMasterAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateFromMasterAccountRequest:
    out: DisassociateFromMasterAccountRequest = {}  # type: ignore[typeddict-item]
    return out
