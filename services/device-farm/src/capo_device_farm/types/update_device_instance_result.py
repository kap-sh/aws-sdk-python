"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateDeviceInstanceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.device_instance


class UpdateDeviceInstanceResult(TypedDict, closed=True):
    device_instance: NotRequired[
        "capo_device_farm.types.device_instance.DeviceInstance"
    ]
    """<p>An object that contains information about your device instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDeviceInstanceResult) -> dict:
    out: dict = {}
    if "device_instance" in value:
        import capo_device_farm.types.device_instance

        out["deviceInstance"] = (
            capo_device_farm.types.device_instance.serialize_aws_json_1_1(
                value["device_instance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDeviceInstanceResult:
    out: UpdateDeviceInstanceResult = {}  # type: ignore[typeddict-item]
    if "deviceInstance" in data:
        import capo_device_farm.types.device_instance

        out["device_instance"] = (
            capo_device_farm.types.device_instance.deserialize_aws_json_1_1(
                data["deviceInstance"]
            )
        )
    return out
