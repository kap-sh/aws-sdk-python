"""Generated from Smithy shape ``com.amazonaws.backup#ScanJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.account_id
    import aws_sdk_backup.types.integer
    import aws_sdk_backup.types.malware_scanner
    import aws_sdk_backup.types.region
    import aws_sdk_backup.types.resource_type
    import aws_sdk_backup.types.scan_job_status
    import aws_sdk_backup.types.scan_result_status
    import aws_sdk_backup.types.timestamp


class ScanJobSummary(TypedDict):
    region: NotRequired["aws_sdk_backup.types.region.Region"]
    """<p>The Amazon Web Services Region where the scan jobs were executed.</p>"""
    account_id: NotRequired["aws_sdk_backup.types.account_id.AccountId"]
    """<p>The account ID that owns the scan jobs included in this summary.</p>"""
    state: NotRequired["aws_sdk_backup.types.scan_job_status.ScanJobStatus"]
    """<p>The state of the scan jobs included in this summary.</p> <p>Valid values: <code>CREATED</code> | <code>RUNNING</code> | <code>COMPLETED</code> | <code>COMPLETED_WITH_ISSUES</code> | <code>FAILED</code> | <code>CANCELED</code>.</p>"""
    resource_type: NotRequired["aws_sdk_backup.types.resource_type.ResourceType"]
    """<p>The type of Amazon Web Services resource for the scan jobs included in this summary.</p>"""
    count: "aws_sdk_backup.types.integer.integer"
    """<p>The number of scan jobs that match the specified criteria.</p>"""
    start_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The value of time in number format of a job start time.</p> <p>This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    end_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The value of time in number format of a job end time.</p> <p>This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    malware_scanner: NotRequired["aws_sdk_backup.types.malware_scanner.MalwareScanner"]
    """<p>Specifies the malware scanner used during the scan job. Currently only supports <code>GUARDDUTY</code>.</p>"""
    scan_result_status: NotRequired[
        "aws_sdk_backup.types.scan_result_status.ScanResultStatus"
    ]
    """<p>The scan result status for the scan jobs included in this summary.</p> <p>Valid values: <code>THREATS_FOUND</code> | <code>NO_THREATS_FOUND</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanJobSummary) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "state" in value:
        import aws_sdk_backup.types.scan_job_status

        out["State"] = aws_sdk_backup.types.scan_job_status.serialize_json(
            value["state"]
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    out["Count"] = value.get("count", 0)
    if "start_time" in value:
        import aws_sdk_backup.types.timestamp

        out["StartTime"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_backup.types.timestamp

        out["EndTime"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "malware_scanner" in value:
        import aws_sdk_backup.types.malware_scanner

        out["MalwareScanner"] = aws_sdk_backup.types.malware_scanner.serialize_json(
            value["malware_scanner"]
        )
    if "scan_result_status" in value:
        import aws_sdk_backup.types.scan_result_status

        out["ScanResultStatus"] = (
            aws_sdk_backup.types.scan_result_status.serialize_json(
                value["scan_result_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScanJobSummary:
    out: ScanJobSummary = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "State" in data:
        import aws_sdk_backup.types.scan_job_status

        out["state"] = aws_sdk_backup.types.scan_job_status.deserialize_json(
            data["State"]
        )
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    if "StartTime" in data:
        import aws_sdk_backup.types.timestamp

        out["start_time"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_backup.types.timestamp

        out["end_time"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["EndTime"]
        )
    if "MalwareScanner" in data:
        import aws_sdk_backup.types.malware_scanner

        out["malware_scanner"] = aws_sdk_backup.types.malware_scanner.deserialize_json(
            data["MalwareScanner"]
        )
    if "ScanResultStatus" in data:
        import aws_sdk_backup.types.scan_result_status

        out["scan_result_status"] = (
            aws_sdk_backup.types.scan_result_status.deserialize_json(
                data["ScanResultStatus"]
            )
        )
    return out
