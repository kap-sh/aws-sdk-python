"""Generated from Smithy shape ``com.amazonaws.configservice#ComplianceSummariesByResourceType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.compliance_summary_by_resource_type

ComplianceSummariesByResourceType: TypeAlias = list[
    "aws_sdk_config_service.types.compliance_summary_by_resource_type.ComplianceSummaryByResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceSummariesByResourceType) -> list:
    import aws_sdk_config_service.types.compliance_summary_by_resource_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.compliance_summary_by_resource_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ComplianceSummariesByResourceType:
    import aws_sdk_config_service.types.compliance_summary_by_resource_type

    out: ComplianceSummariesByResourceType = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.compliance_summary_by_resource_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
