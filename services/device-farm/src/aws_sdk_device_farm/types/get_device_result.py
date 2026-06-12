"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetDeviceResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device


class GetDeviceResult(TypedDict):
    device: NotRequired["aws_sdk_device_farm.types.device.Device"]
    """<p>An object that contains information about the requested device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeviceResult) -> dict:
    out: dict = {}
    if "device" in value:
        import aws_sdk_device_farm.types.device

        out["device"] = aws_sdk_device_farm.types.device.serialize_aws_json_1_1(
            value["device"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeviceResult:
    out: GetDeviceResult = {}  # type: ignore[typeddict-item]
    if "device" in data:
        import aws_sdk_device_farm.types.device

        out["device"] = aws_sdk_device_farm.types.device.deserialize_aws_json_1_1(
            data["device"]
        )
    return out
