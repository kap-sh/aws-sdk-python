"""Generated from Smithy shape ``com.amazonaws.health#EventAggregateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_aggregate

EventAggregateList: TypeAlias = list["capo_health.types.event_aggregate.EventAggregate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventAggregateList) -> list:
    import capo_health.types.event_aggregate

    out: list = []
    for item in value:
        out.append(capo_health.types.event_aggregate.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventAggregateList:
    import capo_health.types.event_aggregate

    out: EventAggregateList = []
    for item in data:
        out.append(capo_health.types.event_aggregate.deserialize_aws_json_1_1(item))
    return out
