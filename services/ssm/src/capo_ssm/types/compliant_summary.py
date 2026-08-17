"""Generated from Smithy shape ``com.amazonaws.ssm#CompliantSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.compliance_summary_count
    import capo_ssm.types.severity_summary


class CompliantSummary(TypedDict, closed=True):
    compliant_count: "capo_ssm.types.compliance_summary_count.ComplianceSummaryCount"
    """<p>The total number of resources that are compliant.</p>"""
    severity_summary: NotRequired["capo_ssm.types.severity_summary.SeveritySummary"]
    """<p>A summary of the compliance severity by compliance type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompliantSummary) -> dict:
    out: dict = {}
    out["CompliantCount"] = value.get("compliant_count", 0)
    if "severity_summary" in value:
        import capo_ssm.types.severity_summary

        out["SeveritySummary"] = capo_ssm.types.severity_summary.serialize_aws_json_1_1(
            value["severity_summary"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CompliantSummary:
    out: CompliantSummary = {}  # type: ignore[typeddict-item]
    if data.get("CompliantCount") is not None:
        out["compliant_count"] = data["CompliantCount"]
    else:
        out["compliant_count"] = 0
    if data.get("SeveritySummary") is not None:
        import capo_ssm.types.severity_summary

        out["severity_summary"] = (
            capo_ssm.types.severity_summary.deserialize_aws_json_1_1(
                data["SeveritySummary"]
            )
        )
    return out
