"""Generated from Smithy shape ``com.amazonaws.guardduty#DateStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.double
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.timestamp


class DateStatistics(TypedDict):
    date: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    r"""<p>The timestamp when the total findings count is observed.</p> <p>For example, <code>Date</code> would look like <code>\"2024-09-05T17:00:00-07:00\"</code> whereas <code>LastGeneratedAt</code> would look like 2024-09-05T17:12:29-07:00\".</p>"""
    last_generated_at: NotRequired["aws_sdk_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the last finding in the findings count, was generated.</p>"""
    severity: NotRequired["aws_sdk_guardduty.types.double.Double"]
    """<p>The severity of the findings generated on each date.</p>"""
    total_findings: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The total number of findings that were generated per severity level on each date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateStatistics) -> dict:
    out: dict = {}
    if "date" in value:
        import aws_sdk_guardduty.types.timestamp

        out["date"] = aws_sdk_guardduty.types.timestamp.serialize_json(value["date"])
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


def deserialize_json(data: dict) -> DateStatistics:
    out: DateStatistics = {}  # type: ignore[typeddict-item]
    if "date" in data:
        import aws_sdk_guardduty.types.timestamp

        out["date"] = aws_sdk_guardduty.types.timestamp.deserialize_json(data["date"])
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
