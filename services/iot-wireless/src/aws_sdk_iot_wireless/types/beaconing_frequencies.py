"""Generated from Smithy shape ``com.amazonaws.iotwireless#BeaconingFrequencies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.beaconing_frequency

BeaconingFrequencies: TypeAlias = list[
    "aws_sdk_iot_wireless.types.beaconing_frequency.BeaconingFrequency"
]


# --- restJson1 ser/de ---
def serialize_json(value: BeaconingFrequencies) -> list:
    return list(value)


def deserialize_json(data: list) -> BeaconingFrequencies:
    return list(data)
