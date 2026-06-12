"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateDevicePoolResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_pool


class UpdateDevicePoolResult(TypedDict):
    device_pool: NotRequired["aws_sdk_device_farm.types.device_pool.DevicePool"]
    """<p>The device pool you just updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDevicePoolResult) -> dict:
    out: dict = {}
    if "device_pool" in value:
        import aws_sdk_device_farm.types.device_pool

        out["devicePool"] = (
            aws_sdk_device_farm.types.device_pool.serialize_aws_json_1_1(
                value["device_pool"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDevicePoolResult:
    out: UpdateDevicePoolResult = {}  # type: ignore[typeddict-item]
    if "devicePool" in data:
        import aws_sdk_device_farm.types.device_pool

        out["device_pool"] = (
            aws_sdk_device_farm.types.device_pool.deserialize_aws_json_1_1(
                data["devicePool"]
            )
        )
    return out
