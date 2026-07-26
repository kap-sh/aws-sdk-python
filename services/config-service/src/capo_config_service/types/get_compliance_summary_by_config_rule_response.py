"""Generated from Smithy shape ``com.amazonaws.configservice#GetComplianceSummaryByConfigRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.compliance_summary


class GetComplianceSummaryByConfigRuleResponse(TypedDict, closed=True):
    compliance_summary: NotRequired[
        "capo_config_service.types.compliance_summary.ComplianceSummary"
    ]
    """<p>The number of Config rules that are compliant and the number that are noncompliant, up to a maximum of 25 for each.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComplianceSummaryByConfigRuleResponse) -> dict:
    out: dict = {}
    if "compliance_summary" in value:
        import capo_config_service.types.compliance_summary

        out["ComplianceSummary"] = (
            capo_config_service.types.compliance_summary.serialize_aws_json_1_1(
                value["compliance_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComplianceSummaryByConfigRuleResponse:
    out: GetComplianceSummaryByConfigRuleResponse = {}  # type: ignore[typeddict-item]
    if "ComplianceSummary" in data:
        import capo_config_service.types.compliance_summary

        out["compliance_summary"] = (
            capo_config_service.types.compliance_summary.deserialize_aws_json_1_1(
                data["ComplianceSummary"]
            )
        )
    return out
