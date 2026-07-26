"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateComplianceByConformancePackList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.aggregate_compliance_by_conformance_pack

AggregateComplianceByConformancePackList: TypeAlias = list[
    "capo_config_service.types.aggregate_compliance_by_conformance_pack.AggregateComplianceByConformancePack"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateComplianceByConformancePackList) -> list:
    import capo_config_service.types.aggregate_compliance_by_conformance_pack

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.aggregate_compliance_by_conformance_pack.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AggregateComplianceByConformancePackList:
    import capo_config_service.types.aggregate_compliance_by_conformance_pack

    out: AggregateComplianceByConformancePackList = []
    for item in data:
        out.append(
            capo_config_service.types.aggregate_compliance_by_conformance_pack.deserialize_aws_json_1_1(
                item
            )
        )
    return out
