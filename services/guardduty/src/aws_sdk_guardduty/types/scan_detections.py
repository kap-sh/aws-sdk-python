"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanDetections``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.highest_severity_threat_details
    import aws_sdk_guardduty.types.scanned_item_count
    import aws_sdk_guardduty.types.threat_detected_by_name
    import aws_sdk_guardduty.types.threats_detected_item_count


class ScanDetections(TypedDict):
    scanned_item_count: NotRequired[
        "aws_sdk_guardduty.types.scanned_item_count.ScannedItemCount"
    ]
    """<p>Total number of scanned files.</p>"""
    threats_detected_item_count: NotRequired[
        "aws_sdk_guardduty.types.threats_detected_item_count.ThreatsDetectedItemCount"
    ]
    """<p>Total number of infected files.</p>"""
    highest_severity_threat_details: NotRequired[
        "aws_sdk_guardduty.types.highest_severity_threat_details.HighestSeverityThreatDetails"
    ]
    """<p>Details of the highest severity threat detected during malware scan and number of infected files.</p>"""
    threat_detected_by_name: NotRequired[
        "aws_sdk_guardduty.types.threat_detected_by_name.ThreatDetectedByName"
    ]
    """<p>Contains details about identified threats organized by threat name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanDetections) -> dict:
    out: dict = {}
    if "scanned_item_count" in value:
        import aws_sdk_guardduty.types.scanned_item_count

        out["scannedItemCount"] = (
            aws_sdk_guardduty.types.scanned_item_count.serialize_json(
                value["scanned_item_count"]
            )
        )
    if "threats_detected_item_count" in value:
        import aws_sdk_guardduty.types.threats_detected_item_count

        out["threatsDetectedItemCount"] = (
            aws_sdk_guardduty.types.threats_detected_item_count.serialize_json(
                value["threats_detected_item_count"]
            )
        )
    if "highest_severity_threat_details" in value:
        import aws_sdk_guardduty.types.highest_severity_threat_details

        out["highestSeverityThreatDetails"] = (
            aws_sdk_guardduty.types.highest_severity_threat_details.serialize_json(
                value["highest_severity_threat_details"]
            )
        )
    if "threat_detected_by_name" in value:
        import aws_sdk_guardduty.types.threat_detected_by_name

        out["threatDetectedByName"] = (
            aws_sdk_guardduty.types.threat_detected_by_name.serialize_json(
                value["threat_detected_by_name"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScanDetections:
    out: ScanDetections = {}  # type: ignore[typeddict-item]
    if "scannedItemCount" in data:
        import aws_sdk_guardduty.types.scanned_item_count

        out["scanned_item_count"] = (
            aws_sdk_guardduty.types.scanned_item_count.deserialize_json(
                data["scannedItemCount"]
            )
        )
    if "threatsDetectedItemCount" in data:
        import aws_sdk_guardduty.types.threats_detected_item_count

        out["threats_detected_item_count"] = (
            aws_sdk_guardduty.types.threats_detected_item_count.deserialize_json(
                data["threatsDetectedItemCount"]
            )
        )
    if "highestSeverityThreatDetails" in data:
        import aws_sdk_guardduty.types.highest_severity_threat_details

        out["highest_severity_threat_details"] = (
            aws_sdk_guardduty.types.highest_severity_threat_details.deserialize_json(
                data["highestSeverityThreatDetails"]
            )
        )
    if "threatDetectedByName" in data:
        import aws_sdk_guardduty.types.threat_detected_by_name

        out["threat_detected_by_name"] = (
            aws_sdk_guardduty.types.threat_detected_by_name.deserialize_json(
                data["threatDetectedByName"]
            )
        )
    return out
