"""Generated from Smithy shape ``com.amazonaws.iotevents#DetectorDebugOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.detector_debug_option

DetectorDebugOptions: TypeAlias = list[
    "aws_sdk_iot_events.types.detector_debug_option.DetectorDebugOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorDebugOptions) -> list:
    import aws_sdk_iot_events.types.detector_debug_option

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_events.types.detector_debug_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> DetectorDebugOptions:
    import aws_sdk_iot_events.types.detector_debug_option

    out: DetectorDebugOptions = []
    for item in data:
        out.append(
            aws_sdk_iot_events.types.detector_debug_option.deserialize_json(item)
        )
    return out
