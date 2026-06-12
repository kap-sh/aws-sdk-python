"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceSelectionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_filters
    import aws_sdk_device_farm.types.integer


class DeviceSelectionResult(TypedDict):
    filters: NotRequired["aws_sdk_device_farm.types.device_filters.DeviceFilters"]
    """<p>The filters in a device selection result.</p>"""
    matched_devices_count: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The number of devices that matched the device filter selection criteria.</p>"""
    max_devices: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The maximum number of devices to be selected by a device filter and included in a test run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceSelectionResult) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_device_farm.types.device_filters

        out["filters"] = (
            aws_sdk_device_farm.types.device_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "matched_devices_count" in value:
        out["matchedDevicesCount"] = value["matched_devices_count"]
    if "max_devices" in value:
        out["maxDevices"] = value["max_devices"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceSelectionResult:
    out: DeviceSelectionResult = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_device_farm.types.device_filters

        out["filters"] = (
            aws_sdk_device_farm.types.device_filters.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    if "matchedDevicesCount" in data:
        out["matched_devices_count"] = data["matchedDevicesCount"]
    if "maxDevices" in data:
        out["max_devices"] = data["maxDevices"]
    return out
