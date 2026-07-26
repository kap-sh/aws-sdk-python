"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#GetScanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_security.types.scan_name
    import capo_codeguru_security.types.uuid


class GetScanRequest(TypedDict, closed=True):
    scan_name: "capo_codeguru_security.types.scan_name.ScanName"
    """<p>The name of the scan you want to view details about.</p>"""
    run_id: NotRequired["capo_codeguru_security.types.uuid.Uuid"]
    """<p>UUID that identifies the individual scan run you want to view details about. You retrieve this when you call the <code>CreateScan</code> operation. Defaults to the latest scan run if missing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetScanRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetScanRequest:
    out: GetScanRequest = {}  # type: ignore[typeddict-item]
    return out
