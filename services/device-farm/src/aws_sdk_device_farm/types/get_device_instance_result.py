"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetDeviceInstanceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_instance


class GetDeviceInstanceResult(TypedDict, closed=True):
    device_instance: NotRequired[
        "aws_sdk_device_farm.types.device_instance.DeviceInstance"
    ]
    """<p>An object that contains information about your device instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeviceInstanceResult) -> dict:
    out: dict = {}
    if "device_instance" in value:
        import aws_sdk_device_farm.types.device_instance

        out["deviceInstance"] = (
            aws_sdk_device_farm.types.device_instance.serialize_aws_json_1_1(
                value["device_instance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeviceInstanceResult:
    out: GetDeviceInstanceResult = {}  # type: ignore[typeddict-item]
    if "deviceInstance" in data:
        import aws_sdk_device_farm.types.device_instance

        out["device_instance"] = (
            aws_sdk_device_farm.types.device_instance.deserialize_aws_json_1_1(
                data["deviceInstance"]
            )
        )
    return out
