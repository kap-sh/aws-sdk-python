"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateConformancePackComplianceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.aggregate_conformance_pack_compliance_summary

AggregateConformancePackComplianceSummaryList: TypeAlias = list[
    "capo_config_service.types.aggregate_conformance_pack_compliance_summary.AggregateConformancePackComplianceSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AggregateConformancePackComplianceSummaryList,
) -> list:
    import capo_config_service.types.aggregate_conformance_pack_compliance_summary

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.aggregate_conformance_pack_compliance_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> AggregateConformancePackComplianceSummaryList:
    import capo_config_service.types.aggregate_conformance_pack_compliance_summary

    out: AggregateConformancePackComplianceSummaryList = []
    for item in data:
        out.append(
            capo_config_service.types.aggregate_conformance_pack_compliance_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
