"""Generated from Smithy shape ``com.amazonaws.backup#ScanAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.malware_scanner
    import capo_backup.types.scan_mode


class ScanAction(TypedDict, closed=True):
    malware_scanner: NotRequired["capo_backup.types.malware_scanner.MalwareScanner"]
    """<p>The malware scanner to use for the scan action. Currently only <code>GUARDDUTY</code> is supported.</p>"""
    scan_mode: NotRequired["capo_backup.types.scan_mode.ScanMode"]
    """<p>The scanning mode to use for the scan action.</p> <p>Valid values: <code>FULL_SCAN</code> | <code>INCREMENTAL_SCAN</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanAction) -> dict:
    out: dict = {}
    if "malware_scanner" in value:
        import capo_backup.types.malware_scanner

        out["MalwareScanner"] = capo_backup.types.malware_scanner.serialize_json(
            value["malware_scanner"]
        )
    if "scan_mode" in value:
        import capo_backup.types.scan_mode

        out["ScanMode"] = capo_backup.types.scan_mode.serialize_json(value["scan_mode"])
    return out


def deserialize_json(data: dict) -> ScanAction:
    out: ScanAction = {}  # type: ignore[typeddict-item]
    if "MalwareScanner" in data:
        import capo_backup.types.malware_scanner

        out["malware_scanner"] = capo_backup.types.malware_scanner.deserialize_json(
            data["MalwareScanner"]
        )
    if "ScanMode" in data:
        import capo_backup.types.scan_mode

        out["scan_mode"] = capo_backup.types.scan_mode.deserialize_json(
            data["ScanMode"]
        )
    return out
