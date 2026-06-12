"""Generated from Smithy shape ``com.amazonaws.ssm#SeveritySummary``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.compliance_summary_count


class SeveritySummary(TypedDict):
    critical_count: "aws_sdk_ssm.types.compliance_summary_count.ComplianceSummaryCount"
    """<p>The total number of resources or compliance items that have a severity level of <code>Critical</code>. Critical severity is determined by the organization that published the compliance items.</p>"""
    high_count: "aws_sdk_ssm.types.compliance_summary_count.ComplianceSummaryCount"
    """<p>The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.</p>"""
    medium_count: "aws_sdk_ssm.types.compliance_summary_count.ComplianceSummaryCount"
    """<p>The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.</p>"""
    low_count: "aws_sdk_ssm.types.compliance_summary_count.ComplianceSummaryCount"
    """<p>The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.</p>"""
    informational_count: (
        "aws_sdk_ssm.types.compliance_summary_count.ComplianceSummaryCount"
    )
    """<p>The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.</p>"""
    unspecified_count: (
        "aws_sdk_ssm.types.compliance_summary_count.ComplianceSummaryCount"
    )
    """<p>The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SeveritySummary) -> dict:
    out: dict = {}
    out["CriticalCount"] = value.get("critical_count", 0)
    out["HighCount"] = value.get("high_count", 0)
    out["MediumCount"] = value.get("medium_count", 0)
    out["LowCount"] = value.get("low_count", 0)
    out["InformationalCount"] = value.get("informational_count", 0)
    out["UnspecifiedCount"] = value.get("unspecified_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> SeveritySummary:
    out: SeveritySummary = {}  # type: ignore[typeddict-item]
    if "CriticalCount" in data:
        out["critical_count"] = data["CriticalCount"]
    else:
        out["critical_count"] = 0
    if "HighCount" in data:
        out["high_count"] = data["HighCount"]
    else:
        out["high_count"] = 0
    if "MediumCount" in data:
        out["medium_count"] = data["MediumCount"]
    else:
        out["medium_count"] = 0
    if "LowCount" in data:
        out["low_count"] = data["LowCount"]
    else:
        out["low_count"] = 0
    if "InformationalCount" in data:
        out["informational_count"] = data["InformationalCount"]
    else:
        out["informational_count"] = 0
    if "UnspecifiedCount" in data:
        out["unspecified_count"] = data["UnspecifiedCount"]
    else:
        out["unspecified_count"] = 0
    return out
