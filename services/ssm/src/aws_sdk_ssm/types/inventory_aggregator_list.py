"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryAggregatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_aggregator

InventoryAggregatorList: TypeAlias = list[
    "aws_sdk_ssm.types.inventory_aggregator.InventoryAggregator"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryAggregatorList) -> list:
    import aws_sdk_ssm.types.inventory_aggregator

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.inventory_aggregator.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InventoryAggregatorList:
    import aws_sdk_ssm.types.inventory_aggregator

    out: InventoryAggregatorList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.inventory_aggregator.deserialize_aws_json_1_1(item)
        )
    return out
