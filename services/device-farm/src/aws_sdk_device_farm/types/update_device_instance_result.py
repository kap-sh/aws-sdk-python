"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateDeviceInstanceResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_instance


class UpdateDeviceInstanceResult(TypedDict):
    device_instance: NotRequired[
        "aws_sdk_device_farm.types.device_instance.DeviceInstance"
    ]
    """<p>An object that contains information about your device instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDeviceInstanceResult) -> dict:
    out: dict = {}
    if "device_instance" in value:
        import aws_sdk_device_farm.types.device_instance

        out["deviceInstance"] = (
            aws_sdk_device_farm.types.device_instance.serialize_aws_json_1_1(
                value["device_instance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDeviceInstanceResult:
    out: UpdateDeviceInstanceResult = {}  # type: ignore[typeddict-item]
    if "deviceInstance" in data:
        import aws_sdk_device_farm.types.device_instance

        out["device_instance"] = (
            aws_sdk_device_farm.types.device_instance.deserialize_aws_json_1_1(
                data["deviceInstance"]
            )
        )
    return out
