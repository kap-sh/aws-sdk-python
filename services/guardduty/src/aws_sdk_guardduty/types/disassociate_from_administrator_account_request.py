"""Generated from Smithy shape ``com.amazonaws.guardduty#DisassociateFromAdministratorAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.detector_id


class DisassociateFromAdministratorAccountRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector of the GuardDuty member account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateFromAdministratorAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateFromAdministratorAccountRequest:
    out: DisassociateFromAdministratorAccountRequest = {}  # type: ignore[typeddict-item]
    return out
