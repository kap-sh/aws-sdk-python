"""Generated from Smithy shape ``com.amazonaws.guardduty#Scan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_id
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.non_empty_string
    import aws_sdk_guardduty.types.positive_long
    import aws_sdk_guardduty.types.resource_details
    import aws_sdk_guardduty.types.scan_result_details
    import aws_sdk_guardduty.types.scan_status
    import aws_sdk_guardduty.types.scan_type
    import aws_sdk_guardduty.types.timestamp
    import aws_sdk_guardduty.types.trigger_details
    import aws_sdk_guardduty.types.volume_details


class Scan(TypedDict, closed=True):
    detector_id: NotRequired["aws_sdk_guardduty.types.detector_id.DetectorId"]
    r"""<p>The unique ID of the detector that is associated with the request.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    admin_detector_id: NotRequired["aws_sdk_guardduty.types.detector_id.DetectorId"]
    r"""<p>The unique detector ID of the administrator account that the request is associated with. If the account is an administrator, the <code>AdminDetectorId</code> will be the same as the one used for <code>DetectorId</code>.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    scan_id: NotRequired["aws_sdk_guardduty.types.non_empty_string.NonEmptyString"]
    """<p>The unique scan ID associated with a scan entry.</p>"""
    scan_status: NotRequired["aws_sdk_guardduty.types.scan_status.ScanStatus"]
    """<p>An enum value representing possible scan statuses.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_guardduty.types.non_empty_string.NonEmptyString"
    ]
    """<p>Represents the reason for <code>FAILED</code> scan status.</p>"""
    scan_start_time: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp of when the scan was triggered.</p>"""
    scan_end_time: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp of when the scan was finished.</p>"""
    trigger_details: NotRequired[
        "aws_sdk_guardduty.types.trigger_details.TriggerDetails"
    ]
    """<p>Specifies the reason why the scan was initiated.</p>"""
    resource_details: NotRequired[
        "aws_sdk_guardduty.types.resource_details.ResourceDetails"
    ]
    """<p>Represents the resources that were scanned in the scan entry.</p>"""
    scan_result_details: NotRequired[
        "aws_sdk_guardduty.types.scan_result_details.ScanResultDetails"
    ]
    """<p>Represents the result of the scan.</p>"""
    account_id: NotRequired["aws_sdk_guardduty.types.account_id.AccountId"]
    """<p>The ID for the account that belongs to the scan.</p>"""
    total_bytes: NotRequired["aws_sdk_guardduty.types.positive_long.PositiveLong"]
    """<p>Represents total bytes that were scanned.</p>"""
    file_count: NotRequired["aws_sdk_guardduty.types.positive_long.PositiveLong"]
    """<p>Represents the number of files that were scanned.</p>"""
    attached_volumes: NotRequired[
        "aws_sdk_guardduty.types.volume_details.VolumeDetails"
    ]
    """<p>List of volumes that were attached to the original instance to be scanned.</p>"""
    scan_type: NotRequired["aws_sdk_guardduty.types.scan_type.ScanType"]
    """<p>Specifies the scan type that invoked the malware scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Scan) -> dict:
    out: dict = {}
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "admin_detector_id" in value:
        out["adminDetectorId"] = value["admin_detector_id"]
    if "scan_id" in value:
        out["scanId"] = value["scan_id"]
    if "scan_status" in value:
        import aws_sdk_guardduty.types.scan_status

        out["scanStatus"] = aws_sdk_guardduty.types.scan_status.serialize_json(
            value["scan_status"]
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "scan_start_time" in value:
        import aws_sdk_guardduty.types.timestamp

        out["scanStartTime"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["scan_start_time"]
        )
    if "scan_end_time" in value:
        import aws_sdk_guardduty.types.timestamp

        out["scanEndTime"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["scan_end_time"]
        )
    if "trigger_details" in value:
        import aws_sdk_guardduty.types.trigger_details

        out["triggerDetails"] = aws_sdk_guardduty.types.trigger_details.serialize_json(
            value["trigger_details"]
        )
    if "resource_details" in value:
        import aws_sdk_guardduty.types.resource_details

        out["resourceDetails"] = (
            aws_sdk_guardduty.types.resource_details.serialize_json(
                value["resource_details"]
            )
        )
    if "scan_result_details" in value:
        import aws_sdk_guardduty.types.scan_result_details

        out["scanResultDetails"] = (
            aws_sdk_guardduty.types.scan_result_details.serialize_json(
                value["scan_result_details"]
            )
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "total_bytes" in value:
        out["totalBytes"] = value["total_bytes"]
    if "file_count" in value:
        out["fileCount"] = value["file_count"]
    if "attached_volumes" in value:
        import aws_sdk_guardduty.types.volume_details

        out["attachedVolumes"] = aws_sdk_guardduty.types.volume_details.serialize_json(
            value["attached_volumes"]
        )
    if "scan_type" in value:
        import aws_sdk_guardduty.types.scan_type

        out["scanType"] = aws_sdk_guardduty.types.scan_type.serialize_json(
            value["scan_type"]
        )
    return out


def deserialize_json(data: dict) -> Scan:
    out: Scan = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "adminDetectorId" in data:
        out["admin_detector_id"] = data["adminDetectorId"]
    if "scanId" in data:
        out["scan_id"] = data["scanId"]
    if "scanStatus" in data:
        import aws_sdk_guardduty.types.scan_status

        out["scan_status"] = aws_sdk_guardduty.types.scan_status.deserialize_json(
            data["scanStatus"]
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "scanStartTime" in data:
        import aws_sdk_guardduty.types.timestamp

        out["scan_start_time"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["scanStartTime"]
        )
    if "scanEndTime" in data:
        import aws_sdk_guardduty.types.timestamp

        out["scan_end_time"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["scanEndTime"]
        )
    if "triggerDetails" in data:
        import aws_sdk_guardduty.types.trigger_details

        out["trigger_details"] = (
            aws_sdk_guardduty.types.trigger_details.deserialize_json(
                data["triggerDetails"]
            )
        )
    if "resourceDetails" in data:
        import aws_sdk_guardduty.types.resource_details

        out["resource_details"] = (
            aws_sdk_guardduty.types.resource_details.deserialize_json(
                data["resourceDetails"]
            )
        )
    if "scanResultDetails" in data:
        import aws_sdk_guardduty.types.scan_result_details

        out["scan_result_details"] = (
            aws_sdk_guardduty.types.scan_result_details.deserialize_json(
                data["scanResultDetails"]
            )
        )
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "totalBytes" in data:
        out["total_bytes"] = data["totalBytes"]
    if "fileCount" in data:
        out["file_count"] = data["fileCount"]
    if "attachedVolumes" in data:
        import aws_sdk_guardduty.types.volume_details

        out["attached_volumes"] = (
            aws_sdk_guardduty.types.volume_details.deserialize_json(
                data["attachedVolumes"]
            )
        )
    if "scanType" in data:
        import aws_sdk_guardduty.types.scan_type

        out["scan_type"] = aws_sdk_guardduty.types.scan_type.deserialize_json(
            data["scanType"]
        )
    return out
