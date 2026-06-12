"""Generated from Smithy shape ``com.amazonaws.health#EventAggregateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.event_aggregate

EventAggregateList: TypeAlias = list[
    "aws_sdk_health.types.event_aggregate.EventAggregate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventAggregateList) -> list:
    import aws_sdk_health.types.event_aggregate

    out: list = []
    for item in value:
        out.append(aws_sdk_health.types.event_aggregate.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventAggregateList:
    import aws_sdk_health.types.event_aggregate

    out: EventAggregateList = []
    for item in data:
        out.append(aws_sdk_health.types.event_aggregate.deserialize_aws_json_1_1(item))
    return out
