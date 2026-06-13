"""Generated from Smithy shape ``com.amazonaws.datazone#ComputeConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.instance_type


class ComputeConfig(TypedDict):
    instance_type: NotRequired["aws_sdk_datazone.types.instance_type.InstanceType"]
    """<p>The instance type for the notebook run compute.</p>"""
    environment_version: NotRequired["str"]
    """<p>The environment version for the notebook run compute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeConfig) -> dict:
    out: dict = {}
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "environment_version" in value:
        out["environmentVersion"] = value["environment_version"]
    return out


def deserialize_json(data: dict) -> ComputeConfig:
    out: ComputeConfig = {}  # type: ignore[typeddict-item]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "environmentVersion" in data:
        out["environment_version"] = data["environmentVersion"]
    return out
