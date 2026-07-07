"""Generated from Smithy shape ``com.amazonaws.ssm#NonCompliantSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.compliance_summary_count
    import aws_sdk_ssm.types.severity_summary


class NonCompliantSummary(TypedDict, closed=True):
    non_compliant_count: (
        "aws_sdk_ssm.types.compliance_summary_count.ComplianceSummaryCount"
    )
    """<p>The total number of compliance items that aren't compliant.</p>"""
    severity_summary: NotRequired["aws_sdk_ssm.types.severity_summary.SeveritySummary"]
    """<p>A summary of the non-compliance severity by compliance type</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NonCompliantSummary) -> dict:
    out: dict = {}
    out["NonCompliantCount"] = value.get("non_compliant_count", 0)
    if "severity_summary" in value:
        import aws_sdk_ssm.types.severity_summary

        out["SeveritySummary"] = (
            aws_sdk_ssm.types.severity_summary.serialize_aws_json_1_1(
                value["severity_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NonCompliantSummary:
    out: NonCompliantSummary = {}  # type: ignore[typeddict-item]
    if "NonCompliantCount" in data:
        out["non_compliant_count"] = data["NonCompliantCount"]
    else:
        out["non_compliant_count"] = 0
    if "SeveritySummary" in data:
        import aws_sdk_ssm.types.severity_summary

        out["severity_summary"] = (
            aws_sdk_ssm.types.severity_summary.deserialize_aws_json_1_1(
                data["SeveritySummary"]
            )
        )
    return out
