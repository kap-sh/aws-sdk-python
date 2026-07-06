"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.device


class UpdateDeviceResponse(TypedDict, closed=True):
    device: NotRequired["aws_sdk_networkmanager.types.device.Device"]
    """<p>Information about the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeviceResponse) -> dict:
    out: dict = {}
    if "device" in value:
        import aws_sdk_networkmanager.types.device

        out["Device"] = aws_sdk_networkmanager.types.device.serialize_json(
            value["device"]
        )
    return out


def deserialize_json(data: dict) -> UpdateDeviceResponse:
    out: UpdateDeviceResponse = {}  # type: ignore[typeddict-item]
    if "Device" in data:
        import aws_sdk_networkmanager.types.device

        out["device"] = aws_sdk_networkmanager.types.device.deserialize_json(
            data["Device"]
        )
    return out
