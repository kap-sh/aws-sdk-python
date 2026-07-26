"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeModelStat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.edge_version
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.long


class EdgeModelStat(TypedDict, closed=True):
    model_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model.</p>"""
    model_version: NotRequired["capo_sagemaker.types.edge_version.EdgeVersion"]
    """<p>The model version.</p>"""
    offline_device_count: NotRequired["capo_sagemaker.types.long.Long"]
    """<p>The number of devices that have this model version and do not have a heart beat.</p>"""
    connected_device_count: NotRequired["capo_sagemaker.types.long.Long"]
    """<p>The number of devices that have this model version and have a heart beat. </p>"""
    active_device_count: NotRequired["capo_sagemaker.types.long.Long"]
    """<p>The number of devices that have this model version, a heart beat, and are currently running.</p>"""
    sampling_device_count: NotRequired["capo_sagemaker.types.long.Long"]
    """<p>The number of devices with this model version and are producing sample data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeModelStat) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    if "offline_device_count" in value:
        out["OfflineDeviceCount"] = value["offline_device_count"]
    if "connected_device_count" in value:
        out["ConnectedDeviceCount"] = value["connected_device_count"]
    if "active_device_count" in value:
        out["ActiveDeviceCount"] = value["active_device_count"]
    if "sampling_device_count" in value:
        out["SamplingDeviceCount"] = value["sampling_device_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EdgeModelStat:
    out: EdgeModelStat = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    if "OfflineDeviceCount" in data:
        out["offline_device_count"] = data["OfflineDeviceCount"]
    if "ConnectedDeviceCount" in data:
        out["connected_device_count"] = data["ConnectedDeviceCount"]
    if "ActiveDeviceCount" in data:
        out["active_device_count"] = data["ActiveDeviceCount"]
    if "SamplingDeviceCount" in data:
        out["sampling_device_count"] = data["SamplingDeviceCount"]
    return out
