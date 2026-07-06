"""Generated from Smithy shape ``com.amazonaws.guardduty#HighestSeverityThreatDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.string


class HighestSeverityThreatDetails(TypedDict, closed=True):
    severity: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Severity level of the highest severity threat detected.</p>"""
    threat_name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Threat name of the highest severity threat detected as part of the malware scan.</p>"""
    count: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>Total number of infected files with the highest severity threat detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HighestSeverityThreatDetails) -> dict:
    out: dict = {}
    if "severity" in value:
        out["severity"] = value["severity"]
    if "threat_name" in value:
        out["threatName"] = value["threat_name"]
    if "count" in value:
        out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> HighestSeverityThreatDetails:
    out: HighestSeverityThreatDetails = {}  # type: ignore[typeddict-item]
    if "severity" in data:
        out["severity"] = data["severity"]
    if "threatName" in data:
        out["threat_name"] = data["threatName"]
    if "count" in data:
        out["count"] = data["count"]
    return out
