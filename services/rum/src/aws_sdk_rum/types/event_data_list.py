"""Generated from Smithy shape ``com.amazonaws.rum#EventDataList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_rum.types.event_data

EventDataList: TypeAlias = list["aws_sdk_rum.types.event_data.EventData"]


# --- restJson1 ser/de ---
def serialize_json(value: EventDataList) -> list:
    return list(value)


def deserialize_json(data: list) -> EventDataList:
    return list(data)