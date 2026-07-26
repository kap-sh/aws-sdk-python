"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeregisterDevicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.device_names
    import capo_sagemaker.types.entity_name


class DeregisterDevicesRequest(TypedDict, closed=True):
    device_fleet_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the fleet the devices belong to.</p>"""
    device_names: NotRequired["capo_sagemaker.types.device_names.DeviceNames"]
    """<p>The unique IDs of the devices.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterDevicesRequest) -> dict:
    out: dict = {}
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "device_names" in value:
        import capo_sagemaker.types.device_names

        out["DeviceNames"] = capo_sagemaker.types.device_names.serialize_aws_json_1_1(
            value["device_names"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterDevicesRequest:
    out: DeregisterDevicesRequest = {}  # type: ignore[typeddict-item]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if "DeviceNames" in data:
        import capo_sagemaker.types.device_names

        out["device_names"] = (
            capo_sagemaker.types.device_names.deserialize_aws_json_1_1(
                data["DeviceNames"]
            )
        )
    return out
