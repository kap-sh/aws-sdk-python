"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetDevicePoolCompatibilityResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_pool_compatibility_results


class GetDevicePoolCompatibilityResult(TypedDict):
    compatible_devices: NotRequired[
        "aws_sdk_device_farm.types.device_pool_compatibility_results.DevicePoolCompatibilityResults"
    ]
    """<p>Information about compatible devices.</p>"""
    incompatible_devices: NotRequired[
        "aws_sdk_device_farm.types.device_pool_compatibility_results.DevicePoolCompatibilityResults"
    ]
    """<p>Information about incompatible devices.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDevicePoolCompatibilityResult) -> dict:
    out: dict = {}
    if "compatible_devices" in value:
        import aws_sdk_device_farm.types.device_pool_compatibility_results

        out["compatibleDevices"] = (
            aws_sdk_device_farm.types.device_pool_compatibility_results.serialize_aws_json_1_1(
                value["compatible_devices"]
            )
        )
    if "incompatible_devices" in value:
        import aws_sdk_device_farm.types.device_pool_compatibility_results

        out["incompatibleDevices"] = (
            aws_sdk_device_farm.types.device_pool_compatibility_results.serialize_aws_json_1_1(
                value["incompatible_devices"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDevicePoolCompatibilityResult:
    out: GetDevicePoolCompatibilityResult = {}  # type: ignore[typeddict-item]
    if "compatibleDevices" in data:
        import aws_sdk_device_farm.types.device_pool_compatibility_results

        out["compatible_devices"] = (
            aws_sdk_device_farm.types.device_pool_compatibility_results.deserialize_aws_json_1_1(
                data["compatibleDevices"]
            )
        )
    if "incompatibleDevices" in data:
        import aws_sdk_device_farm.types.device_pool_compatibility_results

        out["incompatible_devices"] = (
            aws_sdk_device_farm.types.device_pool_compatibility_results.deserialize_aws_json_1_1(
                data["incompatibleDevices"]
            )
        )
    return out
