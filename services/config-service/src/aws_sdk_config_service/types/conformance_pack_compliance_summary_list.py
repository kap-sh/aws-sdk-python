"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackComplianceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_compliance_summary

ConformancePackComplianceSummaryList: TypeAlias = list[
    "aws_sdk_config_service.types.conformance_pack_compliance_summary.ConformancePackComplianceSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackComplianceSummaryList) -> list:
    import aws_sdk_config_service.types.conformance_pack_compliance_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.conformance_pack_compliance_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConformancePackComplianceSummaryList:
    import aws_sdk_config_service.types.conformance_pack_compliance_summary

    out: ConformancePackComplianceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.conformance_pack_compliance_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
