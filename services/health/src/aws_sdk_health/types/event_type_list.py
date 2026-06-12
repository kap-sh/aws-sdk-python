"""Generated from Smithy shape ``com.amazonaws.health#EventTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.event_type

EventTypeList: TypeAlias = list["aws_sdk_health.types.event_type.EventType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTypeList) -> list:
    import aws_sdk_health.types.event_type

    out: list = []
    for item in value:
        out.append(aws_sdk_health.types.event_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventTypeList:
    import aws_sdk_health.types.event_type

    out: EventTypeList = []
    for item in data:
        out.append(aws_sdk_health.types.event_type.deserialize_aws_json_1_1(item))
    return out
