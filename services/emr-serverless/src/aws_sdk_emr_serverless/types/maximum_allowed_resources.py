"""Generated from Smithy shape ``com.amazonaws.emrserverless#MaximumAllowedResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.cpu_size
    import aws_sdk_emr_serverless.types.disk_size
    import aws_sdk_emr_serverless.types.memory_size


class MaximumAllowedResources(TypedDict, closed=True):
    cpu: "aws_sdk_emr_serverless.types.cpu_size.CpuSize"
    """<p>The maximum allowed CPU for an application.</p>"""
    memory: "aws_sdk_emr_serverless.types.memory_size.MemorySize"
    """<p>The maximum allowed resources for an application.</p>"""
    disk: NotRequired["aws_sdk_emr_serverless.types.disk_size.DiskSize"]
    """<p>The maximum allowed disk for an application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MaximumAllowedResources) -> dict:
    out: dict = {}
    out["cpu"] = value["cpu"]
    out["memory"] = value["memory"]
    if "disk" in value:
        out["disk"] = value["disk"]
    return out


def deserialize_json(data: dict) -> MaximumAllowedResources:
    out: MaximumAllowedResources = {}  # type: ignore[typeddict-item]
    if "cpu" in data:
        out["cpu"] = data["cpu"]
    else:
        raise DeserializationError("MaximumAllowedResources.cpu required")
    if "memory" in data:
        out["memory"] = data["memory"]
    else:
        raise DeserializationError("MaximumAllowedResources.memory required")
    if "disk" in data:
        out["disk"] = data["disk"]
    return out
