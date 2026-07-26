"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#DeviceUnderTestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.device_under_test

DeviceUnderTestList: TypeAlias = list[
    "capo_iotdeviceadvisor.types.device_under_test.DeviceUnderTest"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceUnderTestList) -> list:
    import capo_iotdeviceadvisor.types.device_under_test

    out: list = []
    for item in value:
        out.append(capo_iotdeviceadvisor.types.device_under_test.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeviceUnderTestList:
    import capo_iotdeviceadvisor.types.device_under_test

    out: DeviceUnderTestList = []
    for item in data:
        out.append(capo_iotdeviceadvisor.types.device_under_test.deserialize_json(item))
    return out
