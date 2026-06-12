"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateComplianceCount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.compliance_summary
    import aws_sdk_config_service.types.string_with_char_limit256


class AggregateComplianceCount(TypedDict):
    group_name: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The 12-digit account ID or region based on the GroupByKey value.</p>"""
    compliance_summary: NotRequired[
        "aws_sdk_config_service.types.compliance_summary.ComplianceSummary"
    ]
    """<p>The number of compliant and noncompliant Config rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateComplianceCount) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "compliance_summary" in value:
        import aws_sdk_config_service.types.compliance_summary

        out["ComplianceSummary"] = (
            aws_sdk_config_service.types.compliance_summary.serialize_aws_json_1_1(
                value["compliance_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregateComplianceCount:
    out: AggregateComplianceCount = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "ComplianceSummary" in data:
        import aws_sdk_config_service.types.compliance_summary

        out["compliance_summary"] = (
            aws_sdk_config_service.types.compliance_summary.deserialize_aws_json_1_1(
                data["ComplianceSummary"]
            )
        )
    return out
