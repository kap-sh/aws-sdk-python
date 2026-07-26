"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeviceStats``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.long


class DeviceStats(TypedDict, closed=True):
    connected_device_count: NotRequired["capo_sagemaker.types.long.Long"]
    """<p>The number of devices connected with a heartbeat.</p>"""
    registered_device_count: NotRequired["capo_sagemaker.types.long.Long"]
    """<p>The number of registered devices.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceStats) -> dict:
    out: dict = {}
    if "connected_device_count" in value:
        out["ConnectedDeviceCount"] = value["connected_device_count"]
    if "registered_device_count" in value:
        out["RegisteredDeviceCount"] = value["registered_device_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceStats:
    out: DeviceStats = {}  # type: ignore[typeddict-item]
    if "ConnectedDeviceCount" in data:
        out["connected_device_count"] = data["ConnectedDeviceCount"]
    if "RegisteredDeviceCount" in data:
        out["registered_device_count"] = data["RegisteredDeviceCount"]
    return out
