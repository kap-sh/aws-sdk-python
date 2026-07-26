"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanDetections``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.highest_severity_threat_details
    import capo_guardduty.types.scanned_item_count
    import capo_guardduty.types.threat_detected_by_name
    import capo_guardduty.types.threats_detected_item_count


class ScanDetections(TypedDict, closed=True):
    scanned_item_count: NotRequired[
        "capo_guardduty.types.scanned_item_count.ScannedItemCount"
    ]
    """<p>Total number of scanned files.</p>"""
    threats_detected_item_count: NotRequired[
        "capo_guardduty.types.threats_detected_item_count.ThreatsDetectedItemCount"
    ]
    """<p>Total number of infected files.</p>"""
    highest_severity_threat_details: NotRequired[
        "capo_guardduty.types.highest_severity_threat_details.HighestSeverityThreatDetails"
    ]
    """<p>Details of the highest severity threat detected during malware scan and number of infected files.</p>"""
    threat_detected_by_name: NotRequired[
        "capo_guardduty.types.threat_detected_by_name.ThreatDetectedByName"
    ]
    """<p>Contains details about identified threats organized by threat name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanDetections) -> dict:
    out: dict = {}
    if "scanned_item_count" in value:
        import capo_guardduty.types.scanned_item_count

        out["scannedItemCount"] = (
            capo_guardduty.types.scanned_item_count.serialize_json(
                value["scanned_item_count"]
            )
        )
    if "threats_detected_item_count" in value:
        import capo_guardduty.types.threats_detected_item_count

        out["threatsDetectedItemCount"] = (
            capo_guardduty.types.threats_detected_item_count.serialize_json(
                value["threats_detected_item_count"]
            )
        )
    if "highest_severity_threat_details" in value:
        import capo_guardduty.types.highest_severity_threat_details

        out["highestSeverityThreatDetails"] = (
            capo_guardduty.types.highest_severity_threat_details.serialize_json(
                value["highest_severity_threat_details"]
            )
        )
    if "threat_detected_by_name" in value:
        import capo_guardduty.types.threat_detected_by_name

        out["threatDetectedByName"] = (
            capo_guardduty.types.threat_detected_by_name.serialize_json(
                value["threat_detected_by_name"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScanDetections:
    out: ScanDetections = {}  # type: ignore[typeddict-item]
    if "scannedItemCount" in data:
        import capo_guardduty.types.scanned_item_count

        out["scanned_item_count"] = (
            capo_guardduty.types.scanned_item_count.deserialize_json(
                data["scannedItemCount"]
            )
        )
    if "threatsDetectedItemCount" in data:
        import capo_guardduty.types.threats_detected_item_count

        out["threats_detected_item_count"] = (
            capo_guardduty.types.threats_detected_item_count.deserialize_json(
                data["threatsDetectedItemCount"]
            )
        )
    if "highestSeverityThreatDetails" in data:
        import capo_guardduty.types.highest_severity_threat_details

        out["highest_severity_threat_details"] = (
            capo_guardduty.types.highest_severity_threat_details.deserialize_json(
                data["highestSeverityThreatDetails"]
            )
        )
    if "threatDetectedByName" in data:
        import capo_guardduty.types.threat_detected_by_name

        out["threat_detected_by_name"] = (
            capo_guardduty.types.threat_detected_by_name.deserialize_json(
                data["threatDetectedByName"]
            )
        )
    return out
