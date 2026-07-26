"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateDeviceDefinitionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of_device
    import capo_greengrass.types.__string


class CreateDeviceDefinitionVersionRequest(TypedDict, closed=True):
    amzn_client_token: NotRequired["capo_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    device_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the device definition."""
    devices: NotRequired["capo_greengrass.types.__list_of_device.__listOfDevice"]
    """A list of devices in the definition version."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeviceDefinitionVersionRequest) -> dict:
    out: dict = {}
    if "devices" in value:
        import capo_greengrass.types.__list_of_device

        out["Devices"] = capo_greengrass.types.__list_of_device.serialize_json(
            value["devices"]
        )
    return out


def deserialize_json(data: dict) -> CreateDeviceDefinitionVersionRequest:
    out: CreateDeviceDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    if "Devices" in data:
        import capo_greengrass.types.__list_of_device

        out["devices"] = capo_greengrass.types.__list_of_device.deserialize_json(
            data["Devices"]
        )
    return out
