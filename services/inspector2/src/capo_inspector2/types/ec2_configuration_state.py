"""Generated from Smithy shape ``com.amazonaws.inspector2#Ec2ConfigurationState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.ec2_scan_mode_state
    import capo_inspector2.types.vm_scanner_state


class Ec2ConfigurationState(TypedDict, closed=True):
    scan_mode_state: NotRequired[
        "capo_inspector2.types.ec2_scan_mode_state.Ec2ScanModeState"
    ]
    """<p>An object that contains details about the state of the Amazon EC2 scan mode.</p>"""
    vm_scanner_state: NotRequired[
        "capo_inspector2.types.vm_scanner_state.VMScannerState"
    ]
    """<p>An object that contains details about the state of the Amazon Inspector VM scanner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2ConfigurationState) -> dict:
    out: dict = {}
    if "scan_mode_state" in value:
        import capo_inspector2.types.ec2_scan_mode_state

        out["scanModeState"] = capo_inspector2.types.ec2_scan_mode_state.serialize_json(
            value["scan_mode_state"]
        )
    if "vm_scanner_state" in value:
        import capo_inspector2.types.vm_scanner_state

        out["vmScannerState"] = capo_inspector2.types.vm_scanner_state.serialize_json(
            value["vm_scanner_state"]
        )
    return out


def deserialize_json(data: dict) -> Ec2ConfigurationState:
    out: Ec2ConfigurationState = {}  # type: ignore[typeddict-item]
    if "scanModeState" in data:
        import capo_inspector2.types.ec2_scan_mode_state

        out["scan_mode_state"] = (
            capo_inspector2.types.ec2_scan_mode_state.deserialize_json(
                data["scanModeState"]
            )
        )
    if "vmScannerState" in data:
        import capo_inspector2.types.vm_scanner_state

        out["vm_scanner_state"] = (
            capo_inspector2.types.vm_scanner_state.deserialize_json(
                data["vmScannerState"]
            )
        )
    return out
