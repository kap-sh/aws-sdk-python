"""Generated from Smithy shape ``com.amazonaws.health#EntityAggregateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.entity_aggregate

EntityAggregateList: TypeAlias = list[
    "aws_sdk_health.types.entity_aggregate.EntityAggregate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityAggregateList) -> list:
    import aws_sdk_health.types.entity_aggregate

    out: list = []
    for item in value:
        out.append(aws_sdk_health.types.entity_aggregate.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EntityAggregateList:
    import aws_sdk_health.types.entity_aggregate

    out: EntityAggregateList = []
    for item in data:
        out.append(aws_sdk_health.types.entity_aggregate.deserialize_aws_json_1_1(item))
    return out
