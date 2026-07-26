"""Generated from Smithy shape ``com.amazonaws.health#EventTypeCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_type_code

EventTypeCodeList: TypeAlias = list["capo_health.types.event_type_code.eventTypeCode"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventTypeCodeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EventTypeCodeList:
    return list(data)
