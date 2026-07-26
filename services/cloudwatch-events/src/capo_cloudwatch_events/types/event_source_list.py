"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#EventSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.event_source

EventSourceList: TypeAlias = list[
    "capo_cloudwatch_events.types.event_source.EventSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventSourceList) -> list:
    import capo_cloudwatch_events.types.event_source

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_events.types.event_source.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventSourceList:
    import capo_cloudwatch_events.types.event_source

    out: EventSourceList = []
    for item in data:
        out.append(
            capo_cloudwatch_events.types.event_source.deserialize_aws_json_1_1(item)
        )
    return out
