"""Generated from Smithy shape ``com.amazonaws.inspector2#StartCodeSecurityScanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_scan_status
    import aws_sdk_inspector2.types.code_security_uuid


class StartCodeSecurityScanResponse(TypedDict, closed=True):
    scan_id: NotRequired["aws_sdk_inspector2.types.code_security_uuid.CodeSecurityUuid"]
    """<p>The unique identifier of the initiated scan.</p>"""
    status: NotRequired["aws_sdk_inspector2.types.code_scan_status.CodeScanStatus"]
    """<p>The current status of the initiated scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCodeSecurityScanResponse) -> dict:
    out: dict = {}
    if "scan_id" in value:
        out["scanId"] = value["scan_id"]
    if "status" in value:
        import aws_sdk_inspector2.types.code_scan_status

        out["status"] = aws_sdk_inspector2.types.code_scan_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> StartCodeSecurityScanResponse:
    out: StartCodeSecurityScanResponse = {}  # type: ignore[typeddict-item]
    if "scanId" in data:
        out["scan_id"] = data["scanId"]
    if "status" in data:
        import aws_sdk_inspector2.types.code_scan_status

        out["status"] = aws_sdk_inspector2.types.code_scan_status.deserialize_json(
            data["status"]
        )
    return out
