"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeviceProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.device_profile

DeviceProfileList: TypeAlias = list[
    "capo_iot_wireless.types.device_profile.DeviceProfile"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceProfileList) -> list:
    import capo_iot_wireless.types.device_profile

    out: list = []
    for item in value:
        out.append(capo_iot_wireless.types.device_profile.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeviceProfileList:
    import capo_iot_wireless.types.device_profile

    out: DeviceProfileList = []
    for item in data:
        out.append(capo_iot_wireless.types.device_profile.deserialize_json(item))
    return out
