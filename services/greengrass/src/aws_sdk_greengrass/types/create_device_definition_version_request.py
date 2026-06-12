"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateDeviceDefinitionVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of_device
    import aws_sdk_greengrass.types.__string


class CreateDeviceDefinitionVersionRequest(TypedDict):
    amzn_client_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    device_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the device definition."""
    devices: NotRequired["aws_sdk_greengrass.types.__list_of_device.__listOfDevice"]
    """A list of devices in the definition version."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeviceDefinitionVersionRequest) -> dict:
    out: dict = {}
    if "devices" in value:
        import aws_sdk_greengrass.types.__list_of_device

        out["Devices"] = aws_sdk_greengrass.types.__list_of_device.serialize_json(
            value["devices"]
        )
    return out


def deserialize_json(data: dict) -> CreateDeviceDefinitionVersionRequest:
    out: CreateDeviceDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    if "Devices" in data:
        import aws_sdk_greengrass.types.__list_of_device

        out["devices"] = aws_sdk_greengrass.types.__list_of_device.deserialize_json(
            data["Devices"]
        )
    return out
