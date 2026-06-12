"""Generated from Smithy shape ``com.amazonaws.guardduty#EbsVolumeScanDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.scan_detections
    import aws_sdk_guardduty.types.scan_type
    import aws_sdk_guardduty.types.sources
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.timestamp


class EbsVolumeScanDetails(TypedDict):
    scan_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Unique Id of the malware scan that generated the finding.</p>"""
    scan_started_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>Returns the start date and time of the malware scan.</p>"""
    scan_completed_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>Returns the completion date and time of the malware scan.</p>"""
    trigger_finding_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>GuardDuty finding ID that triggered a malware scan.</p>"""
    sources: NotRequired["aws_sdk_guardduty.types.sources.Sources"]
    """<p>Contains list of threat intelligence sources used to detect threats.</p>"""
    scan_detections: NotRequired[
        "aws_sdk_guardduty.types.scan_detections.ScanDetections"
    ]
    """<p>Contains a complete view providing malware scan result details.</p>"""
    scan_type: NotRequired["aws_sdk_guardduty.types.scan_type.ScanType"]
    """<p>Specifies the scan type that invoked the malware scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EbsVolumeScanDetails) -> dict:
    out: dict = {}
    if "scan_id" in value:
        out["scanId"] = value["scan_id"]
    if "scan_started_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["scanStartedAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["scan_started_at"]
        )
    if "scan_completed_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["scanCompletedAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["scan_completed_at"]
        )
    if "trigger_finding_id" in value:
        out["triggerFindingId"] = value["trigger_finding_id"]
    if "sources" in value:
        import aws_sdk_guardduty.types.sources

        out["sources"] = aws_sdk_guardduty.types.sources.serialize_json(
            value["sources"]
        )
    if "scan_detections" in value:
        import aws_sdk_guardduty.types.scan_detections

        out["scanDetections"] = aws_sdk_guardduty.types.scan_detections.serialize_json(
            value["scan_detections"]
        )
    if "scan_type" in value:
        import aws_sdk_guardduty.types.scan_type

        out["scanType"] = aws_sdk_guardduty.types.scan_type.serialize_json(
            value["scan_type"]
        )
    return out


def deserialize_json(data: dict) -> EbsVolumeScanDetails:
    out: EbsVolumeScanDetails = {}  # type: ignore[typeddict-item]
    if "scanId" in data:
        out["scan_id"] = data["scanId"]
    if "scanStartedAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["scan_started_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["scanStartedAt"]
        )
    if "scanCompletedAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["scan_completed_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["scanCompletedAt"]
        )
    if "triggerFindingId" in data:
        out["trigger_finding_id"] = data["triggerFindingId"]
    if "sources" in data:
        import aws_sdk_guardduty.types.sources

        out["sources"] = aws_sdk_guardduty.types.sources.deserialize_json(
            data["sources"]
        )
    if "scanDetections" in data:
        import aws_sdk_guardduty.types.scan_detections

        out["scan_detections"] = (
            aws_sdk_guardduty.types.scan_detections.deserialize_json(
                data["scanDetections"]
            )
        )
    if "scanType" in data:
        import aws_sdk_guardduty.types.scan_type

        out["scan_type"] = aws_sdk_guardduty.types.scan_type.deserialize_json(
            data["scanType"]
        )
    return out
