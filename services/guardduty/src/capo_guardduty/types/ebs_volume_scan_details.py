"""Generated from Smithy shape ``com.amazonaws.guardduty#EbsVolumeScanDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.scan_detections
    import capo_guardduty.types.scan_type
    import capo_guardduty.types.sources
    import capo_guardduty.types.string
    import capo_guardduty.types.timestamp


class EbsVolumeScanDetails(TypedDict, closed=True):
    scan_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>Unique Id of the malware scan that generated the finding.</p>"""
    scan_started_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>Returns the start date and time of the malware scan.</p>"""
    scan_completed_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>Returns the completion date and time of the malware scan.</p>"""
    trigger_finding_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>GuardDuty finding ID that triggered a malware scan.</p>"""
    sources: NotRequired["capo_guardduty.types.sources.Sources"]
    """<p>Contains list of threat intelligence sources used to detect threats.</p>"""
    scan_detections: NotRequired["capo_guardduty.types.scan_detections.ScanDetections"]
    """<p>Contains a complete view providing malware scan result details.</p>"""
    scan_type: NotRequired["capo_guardduty.types.scan_type.ScanType"]
    """<p>Specifies the scan type that invoked the malware scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EbsVolumeScanDetails) -> dict:
    out: dict = {}
    if "scan_id" in value:
        out["scanId"] = value["scan_id"]
    if "scan_started_at" in value:
        import capo_guardduty.types.timestamp

        out["scanStartedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["scan_started_at"]
        )
    if "scan_completed_at" in value:
        import capo_guardduty.types.timestamp

        out["scanCompletedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["scan_completed_at"]
        )
    if "trigger_finding_id" in value:
        out["triggerFindingId"] = value["trigger_finding_id"]
    if "sources" in value:
        import capo_guardduty.types.sources

        out["sources"] = capo_guardduty.types.sources.serialize_json(value["sources"])
    if "scan_detections" in value:
        import capo_guardduty.types.scan_detections

        out["scanDetections"] = capo_guardduty.types.scan_detections.serialize_json(
            value["scan_detections"]
        )
    if "scan_type" in value:
        import capo_guardduty.types.scan_type

        out["scanType"] = capo_guardduty.types.scan_type.serialize_json(
            value["scan_type"]
        )
    return out


def deserialize_json(data: dict) -> EbsVolumeScanDetails:
    out: EbsVolumeScanDetails = {}  # type: ignore[typeddict-item]
    if "scanId" in data:
        out["scan_id"] = data["scanId"]
    if "scanStartedAt" in data:
        import capo_guardduty.types.timestamp

        out["scan_started_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["scanStartedAt"]
        )
    if "scanCompletedAt" in data:
        import capo_guardduty.types.timestamp

        out["scan_completed_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["scanCompletedAt"]
        )
    if "triggerFindingId" in data:
        out["trigger_finding_id"] = data["triggerFindingId"]
    if "sources" in data:
        import capo_guardduty.types.sources

        out["sources"] = capo_guardduty.types.sources.deserialize_json(data["sources"])
    if "scanDetections" in data:
        import capo_guardduty.types.scan_detections

        out["scan_detections"] = capo_guardduty.types.scan_detections.deserialize_json(
            data["scanDetections"]
        )
    if "scanType" in data:
        import capo_guardduty.types.scan_type

        out["scan_type"] = capo_guardduty.types.scan_type.deserialize_json(
            data["scanType"]
        )
    return out
