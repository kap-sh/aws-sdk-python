"""Generated from Smithy shape ``com.amazonaws.inspector2#VMScannerState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.date_time_timestamp
    import aws_sdk_inspector2.types.vm_scanner_status


class VMScannerState(TypedDict):
    activated: NotRequired["bool"]
    """<p>Whether the VM scanner is activated.</p>"""
    activated_at: NotRequired[
        "aws_sdk_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time the VM scanner was activated.</p>"""
    status: NotRequired["aws_sdk_inspector2.types.vm_scanner_status.VMScannerStatus"]
    """<p>The status of the VM scanner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VMScannerState) -> dict:
    out: dict = {}
    if "activated" in value:
        out["activated"] = value["activated"]
    if "activated_at" in value:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["activatedAt"] = (
            aws_sdk_inspector2.types.date_time_timestamp.serialize_json(
                value["activated_at"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> VMScannerState:
    out: VMScannerState = {}  # type: ignore[typeddict-item]
    if "activated" in data:
        out["activated"] = data["activated"]
    if "activatedAt" in data:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["activated_at"] = (
            aws_sdk_inspector2.types.date_time_timestamp.deserialize_json(
                data["activatedAt"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    return out
