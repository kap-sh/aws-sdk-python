"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingTypeStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.timestamp


class FindingTypeStatistics(TypedDict, closed=True):
    finding_type: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Name of the finding type.</p>"""
    last_generated_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which this finding type was last generated in your environment.</p>"""
    total_findings: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The total number of findings associated with generated for each distinct finding type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingTypeStatistics) -> dict:
    out: dict = {}
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    if "last_generated_at" in value:
        import aws_sdk_guardduty.types.timestamp

        out["lastGeneratedAt"] = aws_sdk_guardduty.types.timestamp.serialize_json(
            value["last_generated_at"]
        )
    if "total_findings" in value:
        out["totalFindings"] = value["total_findings"]
    return out


def deserialize_json(data: dict) -> FindingTypeStatistics:
    out: FindingTypeStatistics = {}  # type: ignore[typeddict-item]
    if "findingType" in data:
        out["finding_type"] = data["findingType"]
    if "lastGeneratedAt" in data:
        import aws_sdk_guardduty.types.timestamp

        out["last_generated_at"] = aws_sdk_guardduty.types.timestamp.deserialize_json(
            data["lastGeneratedAt"]
        )
    if "totalFindings" in data:
        out["total_findings"] = data["totalFindings"]
    return out
