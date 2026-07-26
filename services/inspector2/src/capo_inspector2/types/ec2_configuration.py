"""Generated from Smithy shape ``com.amazonaws.inspector2#Ec2Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.ec2_scan_mode


class Ec2Configuration(TypedDict, closed=True):
    scan_mode: "capo_inspector2.types.ec2_scan_mode.Ec2ScanMode"
    """<p>The scan method that is applied to the instance.</p>"""
    activate_vm_scanner: NotRequired["bool"]
    """<p>Whether to activate Amazon Inspector VM scanner for Amazon EC2 scanning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2Configuration) -> dict:
    out: dict = {}
    out["scanMode"] = value["scan_mode"]
    if "activate_vm_scanner" in value:
        out["activateVMScanner"] = value["activate_vm_scanner"]
    return out


def deserialize_json(data: dict) -> Ec2Configuration:
    out: Ec2Configuration = {}  # type: ignore[typeddict-item]
    if "scanMode" in data:
        out["scan_mode"] = data["scanMode"]
    else:
        raise DeserializationError("Ec2Configuration.scan_mode required")
    if "activateVMScanner" in data:
        out["activate_vm_scanner"] = data["activateVMScanner"]
    return out
