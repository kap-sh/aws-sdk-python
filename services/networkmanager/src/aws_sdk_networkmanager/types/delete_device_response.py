"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteDeviceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.device


class DeleteDeviceResponse(TypedDict):
    device: NotRequired["aws_sdk_networkmanager.types.device.Device"]
    """<p>Information about the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDeviceResponse) -> dict:
    out: dict = {}
    if "device" in value:
        import aws_sdk_networkmanager.types.device

        out["Device"] = aws_sdk_networkmanager.types.device.serialize_json(
            value["device"]
        )
    return out


def deserialize_json(data: dict) -> DeleteDeviceResponse:
    out: DeleteDeviceResponse = {}  # type: ignore[typeddict-item]
    if "Device" in data:
        import aws_sdk_networkmanager.types.device

        out["device"] = aws_sdk_networkmanager.types.device.deserialize_json(
            data["Device"]
        )
    return out
