"""Generated from Smithy shape ``com.amazonaws.backup#ScanResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.malware_scanner
    import capo_backup.types.scan_findings
    import capo_backup.types.scan_job_state
    import capo_backup.types.timestamp


class ScanResult(TypedDict, closed=True):
    malware_scanner: NotRequired["capo_backup.types.malware_scanner.MalwareScanner"]
    """<p>The malware scanner used to perform the scan. Currently only <code>GUARDDUTY</code> is supported.</p>"""
    scan_job_state: NotRequired["capo_backup.types.scan_job_state.ScanJobState"]
    """<p>The final state of the scan job.</p> <p>Valid values: <code>COMPLETED</code> | <code>FAILED</code> | <code>CANCELED</code>.</p>"""
    last_scan_timestamp: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The timestamp of when the last scan was performed, in Unix format and Coordinated Universal Time (UTC).</p>"""
    findings: NotRequired["capo_backup.types.scan_findings.ScanFindings"]
    """<p>An array of findings discovered during the scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanResult) -> dict:
    out: dict = {}
    if "malware_scanner" in value:
        import capo_backup.types.malware_scanner

        out["MalwareScanner"] = capo_backup.types.malware_scanner.serialize_json(
            value["malware_scanner"]
        )
    if "scan_job_state" in value:
        import capo_backup.types.scan_job_state

        out["ScanJobState"] = capo_backup.types.scan_job_state.serialize_json(
            value["scan_job_state"]
        )
    if "last_scan_timestamp" in value:
        import capo_backup.types.timestamp

        out["LastScanTimestamp"] = capo_backup.types.timestamp.serialize_json(
            value["last_scan_timestamp"]
        )
    if "findings" in value:
        import capo_backup.types.scan_findings

        out["Findings"] = capo_backup.types.scan_findings.serialize_json(
            value["findings"]
        )
    return out


def deserialize_json(data: dict) -> ScanResult:
    out: ScanResult = {}  # type: ignore[typeddict-item]
    if "MalwareScanner" in data:
        import capo_backup.types.malware_scanner

        out["malware_scanner"] = capo_backup.types.malware_scanner.deserialize_json(
            data["MalwareScanner"]
        )
    if "ScanJobState" in data:
        import capo_backup.types.scan_job_state

        out["scan_job_state"] = capo_backup.types.scan_job_state.deserialize_json(
            data["ScanJobState"]
        )
    if "LastScanTimestamp" in data:
        import capo_backup.types.timestamp

        out["last_scan_timestamp"] = capo_backup.types.timestamp.deserialize_json(
            data["LastScanTimestamp"]
        )
    if "Findings" in data:
        import capo_backup.types.scan_findings

        out["findings"] = capo_backup.types.scan_findings.deserialize_json(
            data["Findings"]
        )
    return out
