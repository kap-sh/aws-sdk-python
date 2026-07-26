"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeviceSelectionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.device_name
    import capo_sagemaker.types.device_names
    import capo_sagemaker.types.device_subset_type
    import capo_sagemaker.types.percentage


class DeviceSelectionConfig(TypedDict, closed=True):
    device_subset_type: NotRequired[
        "capo_sagemaker.types.device_subset_type.DeviceSubsetType"
    ]
    """<p>Type of device subsets to deploy to the current stage.</p>"""
    percentage: NotRequired["capo_sagemaker.types.percentage.Percentage"]
    """<p>Percentage of devices in the fleet to deploy to the current stage.</p>"""
    device_names: NotRequired["capo_sagemaker.types.device_names.DeviceNames"]
    """<p>List of devices chosen to deploy.</p>"""
    device_name_contains: NotRequired["capo_sagemaker.types.device_name.DeviceName"]
    """<p>A filter to select devices with names containing this name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceSelectionConfig) -> dict:
    out: dict = {}
    if "device_subset_type" in value:
        import capo_sagemaker.types.device_subset_type

        out["DeviceSubsetType"] = (
            capo_sagemaker.types.device_subset_type.serialize_aws_json_1_1(
                value["device_subset_type"]
            )
        )
    if "percentage" in value:
        out["Percentage"] = value["percentage"]
    if "device_names" in value:
        import capo_sagemaker.types.device_names

        out["DeviceNames"] = capo_sagemaker.types.device_names.serialize_aws_json_1_1(
            value["device_names"]
        )
    if "device_name_contains" in value:
        out["DeviceNameContains"] = value["device_name_contains"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceSelectionConfig:
    out: DeviceSelectionConfig = {}  # type: ignore[typeddict-item]
    if "DeviceSubsetType" in data:
        import capo_sagemaker.types.device_subset_type

        out["device_subset_type"] = (
            capo_sagemaker.types.device_subset_type.deserialize_aws_json_1_1(
                data["DeviceSubsetType"]
            )
        )
    if "Percentage" in data:
        out["percentage"] = data["Percentage"]
    if "DeviceNames" in data:
        import capo_sagemaker.types.device_names

        out["device_names"] = (
            capo_sagemaker.types.device_names.deserialize_aws_json_1_1(
                data["DeviceNames"]
            )
        )
    if "DeviceNameContains" in data:
        out["device_name_contains"] = data["DeviceNameContains"]
    return out
