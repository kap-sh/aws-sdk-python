"""Generated from Smithy shape ``com.amazonaws.iot#ViolationEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.violation_event

ViolationEvents: TypeAlias = list["aws_sdk_iot.types.violation_event.ViolationEvent"]


# --- restJson1 ser/de ---
def serialize_json(value: ViolationEvents) -> list:
    import aws_sdk_iot.types.violation_event

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.violation_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> ViolationEvents:
    import aws_sdk_iot.types.violation_event

    out: ViolationEvents = []
    for item in data:
        out.append(aws_sdk_iot.types.violation_event.deserialize_json(item))
    return out
