"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetDevicePoolCompatibilityResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.device_pool_compatibility_results


class GetDevicePoolCompatibilityResult(TypedDict, closed=True):
    compatible_devices: NotRequired[
        "capo_device_farm.types.device_pool_compatibility_results.DevicePoolCompatibilityResults"
    ]
    """<p>Information about compatible devices.</p>"""
    incompatible_devices: NotRequired[
        "capo_device_farm.types.device_pool_compatibility_results.DevicePoolCompatibilityResults"
    ]
    """<p>Information about incompatible devices.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDevicePoolCompatibilityResult) -> dict:
    out: dict = {}
    if "compatible_devices" in value:
        import capo_device_farm.types.device_pool_compatibility_results

        out["compatibleDevices"] = (
            capo_device_farm.types.device_pool_compatibility_results.serialize_aws_json_1_1(
                value["compatible_devices"]
            )
        )
    if "incompatible_devices" in value:
        import capo_device_farm.types.device_pool_compatibility_results

        out["incompatibleDevices"] = (
            capo_device_farm.types.device_pool_compatibility_results.serialize_aws_json_1_1(
                value["incompatible_devices"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDevicePoolCompatibilityResult:
    out: GetDevicePoolCompatibilityResult = {}  # type: ignore[typeddict-item]
    if "compatibleDevices" in data:
        import capo_device_farm.types.device_pool_compatibility_results

        out["compatible_devices"] = (
            capo_device_farm.types.device_pool_compatibility_results.deserialize_aws_json_1_1(
                data["compatibleDevices"]
            )
        )
    if "incompatibleDevices" in data:
        import capo_device_farm.types.device_pool_compatibility_results

        out["incompatible_devices"] = (
            capo_device_farm.types.device_pool_compatibility_results.deserialize_aws_json_1_1(
                data["incompatibleDevices"]
            )
        )
    return out
