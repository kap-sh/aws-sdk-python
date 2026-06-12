"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateComplianceCountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregate_compliance_count

AggregateComplianceCountList: TypeAlias = list[
    "aws_sdk_config_service.types.aggregate_compliance_count.AggregateComplianceCount"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateComplianceCountList) -> list:
    import aws_sdk_config_service.types.aggregate_compliance_count

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.aggregate_compliance_count.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AggregateComplianceCountList:
    import aws_sdk_config_service.types.aggregate_compliance_count

    out: AggregateComplianceCountList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.aggregate_compliance_count.deserialize_aws_json_1_1(
                item
            )
        )
    return out
