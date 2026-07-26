"""Generated from Smithy shape ``com.amazonaws.iot#ViolationEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.violation_event

ViolationEvents: TypeAlias = list["capo_iot.types.violation_event.ViolationEvent"]


# --- restJson1 ser/de ---
def serialize_json(value: ViolationEvents) -> list:
    import capo_iot.types.violation_event

    out: list = []
    for item in value:
        out.append(capo_iot.types.violation_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> ViolationEvents:
    import capo_iot.types.violation_event

    out: ViolationEvents = []
    for item in data:
        out.append(capo_iot.types.violation_event.deserialize_json(item))
    return out
