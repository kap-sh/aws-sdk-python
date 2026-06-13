"""Generated from Smithy shape ``com.amazonaws.backup#AggregatedScanResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.boolean
    import aws_sdk_backup.types.scan_findings
    import aws_sdk_backup.types.timestamp


class AggregatedScanResult(TypedDict):
    failed_scan: NotRequired["aws_sdk_backup.types.boolean.Boolean"]
    """<p>A Boolean value indicating whether any of the aggregated scans failed.</p>"""
    findings: NotRequired["aws_sdk_backup.types.scan_findings.ScanFindings"]
    """<p>An array of findings discovered across all aggregated scans.</p>"""
    last_computed: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The timestamp when the aggregated scan result was last computed, in Unix format and Coordinated Universal Time (UTC).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedScanResult) -> dict:
    out: dict = {}
    if "failed_scan" in value:
        out["FailedScan"] = value["failed_scan"]
    if "findings" in value:
        import aws_sdk_backup.types.scan_findings

        out["Findings"] = aws_sdk_backup.types.scan_findings.serialize_json(
            value["findings"]
        )
    if "last_computed" in value:
        import aws_sdk_backup.types.timestamp

        out["LastComputed"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["last_computed"]
        )
    return out


def deserialize_json(data: dict) -> AggregatedScanResult:
    out: AggregatedScanResult = {}  # type: ignore[typeddict-item]
    if "FailedScan" in data:
        out["failed_scan"] = data["FailedScan"]
    if "Findings" in data:
        import aws_sdk_backup.types.scan_findings

        out["findings"] = aws_sdk_backup.types.scan_findings.deserialize_json(
            data["Findings"]
        )
    if "LastComputed" in data:
        import aws_sdk_backup.types.timestamp

        out["last_computed"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["LastComputed"]
        )
    return out
