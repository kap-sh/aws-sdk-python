"""Generated from Smithy shape ``com.amazonaws.mturk#EventTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mturk.types.event_type

EventTypeList: TypeAlias = list["capo_mturk.types.event_type.EventType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTypeList) -> list:
    import capo_mturk.types.event_type

    out: list = []
    for item in value:
        out.append(capo_mturk.types.event_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EventTypeList:
    import capo_mturk.types.event_type

    out: EventTypeList = []
    for item in data:
        out.append(capo_mturk.types.event_type.deserialize_aws_json_1_1(item))
    return out
