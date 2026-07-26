"""Generated from Smithy shape ``com.amazonaws.greengrass#DeviceDefinitionVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of_device


class DeviceDefinitionVersion(TypedDict, closed=True):
    devices: NotRequired["capo_greengrass.types.__list_of_device.__listOfDevice"]
    """A list of devices in the definition version."""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceDefinitionVersion) -> dict:
    out: dict = {}
    if "devices" in value:
        import capo_greengrass.types.__list_of_device

        out["Devices"] = capo_greengrass.types.__list_of_device.serialize_json(
            value["devices"]
        )
    return out


def deserialize_json(data: dict) -> DeviceDefinitionVersion:
    out: DeviceDefinitionVersion = {}  # type: ignore[typeddict-item]
    if "Devices" in data:
        import capo_greengrass.types.__list_of_device

        out["devices"] = capo_greengrass.types.__list_of_device.deserialize_json(
            data["Devices"]
        )
    return out
