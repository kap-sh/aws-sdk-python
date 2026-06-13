"""Generated from Smithy shape ``com.amazonaws.rum#RumEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rum.types.rum_event

RumEventList: TypeAlias = list["aws_sdk_rum.types.rum_event.RumEvent"]


# --- restJson1 ser/de ---
def serialize_json(value: RumEventList) -> list:
    import aws_sdk_rum.types.rum_event

    out: list = []
    for item in value:
        out.append(aws_sdk_rum.types.rum_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> RumEventList:
    import aws_sdk_rum.types.rum_event

    out: RumEventList = []
    for item in data:
        out.append(aws_sdk_rum.types.rum_event.deserialize_json(item))
    return out
