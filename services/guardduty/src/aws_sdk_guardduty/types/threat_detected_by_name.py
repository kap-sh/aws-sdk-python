"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatDetectedByName``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.boolean
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.scan_threat_names


class ThreatDetectedByName(TypedDict):
    item_count: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>Total number of infected files identified.</p>"""
    unique_threat_name_count: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>Total number of unique threats by name identified, as part of the malware scan.</p>"""
    shortened: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>Flag to determine if the finding contains every single infected file-path and/or every threat.</p>"""
    threat_names: NotRequired[
        "aws_sdk_guardduty.types.scan_threat_names.ScanThreatNames"
    ]
    """<p>List of identified threats with details, organized by threat name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatDetectedByName) -> dict:
    out: dict = {}
    if "item_count" in value:
        out["itemCount"] = value["item_count"]
    if "unique_threat_name_count" in value:
        out["uniqueThreatNameCount"] = value["unique_threat_name_count"]
    if "shortened" in value:
        out["shortened"] = value["shortened"]
    if "threat_names" in value:
        import aws_sdk_guardduty.types.scan_threat_names

        out["threatNames"] = aws_sdk_guardduty.types.scan_threat_names.serialize_json(
            value["threat_names"]
        )
    return out


def deserialize_json(data: dict) -> ThreatDetectedByName:
    out: ThreatDetectedByName = {}  # type: ignore[typeddict-item]
    if "itemCount" in data:
        out["item_count"] = data["itemCount"]
    if "uniqueThreatNameCount" in data:
        out["unique_threat_name_count"] = data["uniqueThreatNameCount"]
    if "shortened" in data:
        out["shortened"] = data["shortened"]
    if "threatNames" in data:
        import aws_sdk_guardduty.types.scan_threat_names

        out["threat_names"] = (
            aws_sdk_guardduty.types.scan_threat_names.deserialize_json(
                data["threatNames"]
            )
        )
    return out
