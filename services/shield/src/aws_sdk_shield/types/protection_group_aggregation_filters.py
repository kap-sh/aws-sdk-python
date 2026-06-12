"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupAggregationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_shield.types.protection_group_aggregation

ProtectionGroupAggregationFilters: TypeAlias = list[
    "aws_sdk_shield.types.protection_group_aggregation.ProtectionGroupAggregation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroupAggregationFilters) -> list:
    import aws_sdk_shield.types.protection_group_aggregation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_shield.types.protection_group_aggregation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProtectionGroupAggregationFilters:
    import aws_sdk_shield.types.protection_group_aggregation

    out: ProtectionGroupAggregationFilters = []
    for item in data:
        out.append(
            aws_sdk_shield.types.protection_group_aggregation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
