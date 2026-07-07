"""Generated from Smithy shape ``com.amazonaws.guardduty#SeverityStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.double
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.timestamp


class SeverityStatistics(TypedDict, closed=True):
    last_generated_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which a finding type for a specific severity was last generated.</p>"""
    severity: NotRequired["aws_sdk_guardduty.types.double.Double"]
    """<p>The severity level associated with each finding type.</p>"""
    total_findings: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The total number of findings associated with this severity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SeverityStatistics) -> dict:
    out: dict = {}
    if "last_generated_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["lastGeneratedAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["last_generated_at"]
        )
    if "severity" in value:
        out["severity"] = value["severity"]
    if "total_findings" in value:
        out["totalFindings"] = value["total_findings"]
    return out


def deserialize_json(data: dict) -> SeverityStatistics:
    out: SeverityStatistics = {}  # type: ignore[typeddict-item]
    if "lastGeneratedAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["last_generated_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["lastGeneratedAt"]
        )
    if "severity" in data:
        out["severity"] = data["severity"]
    if "totalFindings" in data:
        out["total_findings"] = data["totalFindings"]
    return out
