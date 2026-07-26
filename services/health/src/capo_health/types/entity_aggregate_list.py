"""Generated from Smithy shape ``com.amazonaws.health#EntityAggregateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.entity_aggregate

EntityAggregateList: TypeAlias = list[
    "capo_health.types.entity_aggregate.EntityAggregate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityAggregateList) -> list:
    import capo_health.types.entity_aggregate

    out: list = []
    for item in value:
        out.append(capo_health.types.entity_aggregate.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EntityAggregateList:
    import capo_health.types.entity_aggregate

    out: EntityAggregateList = []
    for item in data:
        out.append(capo_health.types.entity_aggregate.deserialize_aws_json_1_1(item))
    return out
