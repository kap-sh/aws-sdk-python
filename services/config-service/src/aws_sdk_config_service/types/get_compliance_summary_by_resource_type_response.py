"""Generated from Smithy shape ``com.amazonaws.configservice#GetComplianceSummaryByResourceTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.compliance_summaries_by_resource_type


class GetComplianceSummaryByResourceTypeResponse(TypedDict, closed=True):
    compliance_summaries_by_resource_type: NotRequired[
        "aws_sdk_config_service.types.compliance_summaries_by_resource_type.ComplianceSummariesByResourceType"
    ]
    """<p>The number of resources that are compliant and the number that are noncompliant. If one or more resource types were provided with the request, the numbers are returned for each resource type. The maximum number returned is 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComplianceSummaryByResourceTypeResponse) -> dict:
    out: dict = {}
    if "compliance_summaries_by_resource_type" in value:
        import aws_sdk_config_service.types.compliance_summaries_by_resource_type

        out["ComplianceSummariesByResourceType"] = (
            aws_sdk_config_service.types.compliance_summaries_by_resource_type.serialize_aws_json_1_1(
                value["compliance_summaries_by_resource_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComplianceSummaryByResourceTypeResponse:
    out: GetComplianceSummaryByResourceTypeResponse = {}  # type: ignore[typeddict-item]
    if "ComplianceSummariesByResourceType" in data:
        import aws_sdk_config_service.types.compliance_summaries_by_resource_type

        out["compliance_summaries_by_resource_type"] = (
            aws_sdk_config_service.types.compliance_summaries_by_resource_type.deserialize_aws_json_1_1(
                data["ComplianceSummariesByResourceType"]
            )
        )
    return out
