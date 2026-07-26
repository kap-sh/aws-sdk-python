"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceSummaryItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.compliance_type_name
    import capo_ssm.types.compliant_summary
    import capo_ssm.types.non_compliant_summary


class ComplianceSummaryItem(TypedDict, closed=True):
    compliance_type: NotRequired[
        "capo_ssm.types.compliance_type_name.ComplianceTypeName"
    ]
    """<p>The type of compliance item. For example, the compliance type can be Association, Patch, or Custom:string.</p>"""
    compliant_summary: NotRequired["capo_ssm.types.compliant_summary.CompliantSummary"]
    """<p>A list of COMPLIANT items for the specified compliance type.</p>"""
    non_compliant_summary: NotRequired[
        "capo_ssm.types.non_compliant_summary.NonCompliantSummary"
    ]
    """<p>A list of NON_COMPLIANT items for the specified compliance type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceSummaryItem) -> dict:
    out: dict = {}
    if "compliance_type" in value:
        out["ComplianceType"] = value["compliance_type"]
    if "compliant_summary" in value:
        import capo_ssm.types.compliant_summary

        out["CompliantSummary"] = (
            capo_ssm.types.compliant_summary.serialize_aws_json_1_1(
                value["compliant_summary"]
            )
        )
    if "non_compliant_summary" in value:
        import capo_ssm.types.non_compliant_summary

        out["NonCompliantSummary"] = (
            capo_ssm.types.non_compliant_summary.serialize_aws_json_1_1(
                value["non_compliant_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceSummaryItem:
    out: ComplianceSummaryItem = {}  # type: ignore[typeddict-item]
    if "ComplianceType" in data:
        out["compliance_type"] = data["ComplianceType"]
    if "CompliantSummary" in data:
        import capo_ssm.types.compliant_summary

        out["compliant_summary"] = (
            capo_ssm.types.compliant_summary.deserialize_aws_json_1_1(
                data["CompliantSummary"]
            )
        )
    if "NonCompliantSummary" in data:
        import capo_ssm.types.non_compliant_summary

        out["non_compliant_summary"] = (
            capo_ssm.types.non_compliant_summary.deserialize_aws_json_1_1(
                data["NonCompliantSummary"]
            )
        )
    return out
