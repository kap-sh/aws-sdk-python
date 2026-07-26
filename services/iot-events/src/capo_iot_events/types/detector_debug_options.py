"""Generated from Smithy shape ``com.amazonaws.iotevents#DetectorDebugOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events.types.detector_debug_option

DetectorDebugOptions: TypeAlias = list[
    "capo_iot_events.types.detector_debug_option.DetectorDebugOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorDebugOptions) -> list:
    import capo_iot_events.types.detector_debug_option

    out: list = []
    for item in value:
        out.append(capo_iot_events.types.detector_debug_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> DetectorDebugOptions:
    import capo_iot_events.types.detector_debug_option

    out: DetectorDebugOptions = []
    for item in data:
        out.append(capo_iot_events.types.detector_debug_option.deserialize_json(item))
    return out
