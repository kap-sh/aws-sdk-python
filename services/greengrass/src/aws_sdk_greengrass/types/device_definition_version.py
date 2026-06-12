"""Generated from Smithy shape ``com.amazonaws.greengrass#DeviceDefinitionVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of_device


class DeviceDefinitionVersion(TypedDict):
    devices: NotRequired["aws_sdk_greengrass.types.__list_of_device.__listOfDevice"]
    """A list of devices in the definition version."""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceDefinitionVersion) -> dict:
    out: dict = {}
    if "devices" in value:
        import aws_sdk_greengrass.types.__list_of_device

        out["Devices"] = aws_sdk_greengrass.types.__list_of_device.serialize_json(
            value["devices"]
        )
    return out


def deserialize_json(data: dict) -> DeviceDefinitionVersion:
    out: DeviceDefinitionVersion = {}  # type: ignore[typeddict-item]
    if "Devices" in data:
        import aws_sdk_greengrass.types.__list_of_device

        out["devices"] = aws_sdk_greengrass.types.__list_of_device.deserialize_json(
            data["Devices"]
        )
    return out
