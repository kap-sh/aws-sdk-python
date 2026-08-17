"""Generated from Smithy shape ``com.amazonaws.ecs#InferenceAcceleratorOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class InferenceAcceleratorOverride(TypedDict, closed=True):
    device_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The Elastic Inference accelerator device name to override for the task. This parameter must match a <code>deviceName</code> specified in the task definition.</p>"""
    device_type: NotRequired["capo_ecs.types.string.String"]
    """<p>The Elastic Inference accelerator type to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceAcceleratorOverride) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    if "device_type" in value:
        out["deviceType"] = value["device_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceAcceleratorOverride:
    out: InferenceAcceleratorOverride = {}  # type: ignore[typeddict-item]
    if data.get("deviceName") is not None:
        out["device_name"] = data["deviceName"]
    if data.get("deviceType") is not None:
        out["device_type"] = data["deviceType"]
    return out
