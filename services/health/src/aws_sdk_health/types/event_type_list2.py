"""Generated from Smithy shape ``com.amazonaws.health#eventTypeList2``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.event_type2

eventTypeList2: TypeAlias = list["aws_sdk_health.types.event_type2.EventType2"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: eventTypeList2) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> eventTypeList2:
    return list(data)
