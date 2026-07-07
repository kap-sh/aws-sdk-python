"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateConformancePackComplianceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregate_conformance_pack_compliance_count
    import aws_sdk_config_service.types.string_with_char_limit256


class AggregateConformancePackComplianceSummary(TypedDict, closed=True):
    compliance_summary: NotRequired[
        "aws_sdk_config_service.types.aggregate_conformance_pack_compliance_count.AggregateConformancePackComplianceCount"
    ]
    """<p>Returns an <code>AggregateConformancePackComplianceCount</code> object. </p>"""
    group_name: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>Groups the result based on Amazon Web Services account ID or Amazon Web Services Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateConformancePackComplianceSummary) -> dict:
    out: dict = {}
    if "compliance_summary" in value:
        import aws_sdk_config_service.types.aggregate_conformance_pack_compliance_count

        out["ComplianceSummary"] = (
            aws_sdk_config_service.types.aggregate_conformance_pack_compliance_count.serialize_aws_json_1_1(
                value["compliance_summary"]
            )
        )
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregateConformancePackComplianceSummary:
    out: AggregateConformancePackComplianceSummary = {}  # type: ignore[typeddict-item]
    if "ComplianceSummary" in data:
        import aws_sdk_config_service.types.aggregate_conformance_pack_compliance_count

        out["compliance_summary"] = (
            aws_sdk_config_service.types.aggregate_conformance_pack_compliance_count.deserialize_aws_json_1_1(
                data["ComplianceSummary"]
            )
        )
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    return out
