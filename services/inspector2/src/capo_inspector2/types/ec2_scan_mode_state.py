"""Generated from Smithy shape ``com.amazonaws.inspector2#Ec2ScanModeState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.ec2_scan_mode
    import capo_inspector2.types.ec2_scan_mode_status


class Ec2ScanModeState(TypedDict, closed=True):
    scan_mode: NotRequired["capo_inspector2.types.ec2_scan_mode.Ec2ScanMode"]
    """<p>The scan method that is applied to the instance.</p>"""
    scan_mode_status: NotRequired[
        "capo_inspector2.types.ec2_scan_mode_status.Ec2ScanModeStatus"
    ]
    """<p>The status of the Amazon EC2 scan mode setting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2ScanModeState) -> dict:
    out: dict = {}
    if "scan_mode" in value:
        out["scanMode"] = value["scan_mode"]
    if "scan_mode_status" in value:
        out["scanModeStatus"] = value["scan_mode_status"]
    return out


def deserialize_json(data: dict) -> Ec2ScanModeState:
    out: Ec2ScanModeState = {}  # type: ignore[typeddict-item]
    if "scanMode" in data:
        out["scan_mode"] = data["scanMode"]
    if "scanModeStatus" in data:
        out["scan_mode_status"] = data["scanModeStatus"]
    return out
