"""Generated from Smithy shape ``com.amazonaws.pipes#EcsInferenceAcceleratorOverride``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pipes.types.string


class EcsInferenceAcceleratorOverride(TypedDict):
    device_name: NotRequired["aws_sdk_pipes.types.string.String"]
    """<p>The Elastic Inference accelerator device name to override for the task. This parameter must match a <code>deviceName</code> specified in the task definition.</p>"""
    device_type: NotRequired["aws_sdk_pipes.types.string.String"]
    """<p>The Elastic Inference accelerator type to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsInferenceAcceleratorOverride) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    if "device_type" in value:
        out["deviceType"] = value["device_type"]
    return out


def deserialize_json(data: dict) -> EcsInferenceAcceleratorOverride:
    out: EcsInferenceAcceleratorOverride = {}  # type: ignore[typeddict-item]
    if "deviceName" in data:
        out["device_name"] = data["deviceName"]
    if "deviceType" in data:
        out["device_type"] = data["deviceType"]
    return out
