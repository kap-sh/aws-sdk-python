"""Generated from Smithy shape ``com.amazonaws.inspector2#VMScannerState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.vm_scanner_status


class VMScannerState(TypedDict, closed=True):
    activated: NotRequired["bool"]
    """<p>Whether the VM scanner is activated.</p>"""
    activated_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time the VM scanner was activated.</p>"""
    status: NotRequired["capo_inspector2.types.vm_scanner_status.VMScannerStatus"]
    """<p>The status of the VM scanner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VMScannerState) -> dict:
    out: dict = {}
    if "activated" in value:
        out["activated"] = value["activated"]
    if "activated_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["activatedAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["activated_at"]
        )
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> VMScannerState:
    out: VMScannerState = {}  # type: ignore[typeddict-item]
    if "activated" in data:
        out["activated"] = data["activated"]
    if "activatedAt" in data:
        import capo_inspector2.types.date_time_timestamp

        out["activated_at"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["activatedAt"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    return out
