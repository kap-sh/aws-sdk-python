"""Generated from Smithy shape ``com.amazonaws.braket#InstanceConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.instance_type


class InstanceConfig(TypedDict):
    instance_type: "aws_sdk_braket.types.instance_type.InstanceType"
    """<p>Configures the type of resource instances to use while running an Amazon Braket hybrid job.</p>"""
    volume_size_in_gb: "int"
    """<p>The size of the storage volume, in GB, to provision.</p>"""
    instance_count: NotRequired["int"]
    """<p>Configures the number of resource instances to use while running an Amazon Braket hybrid job on Amazon Braket. The default value is 1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceConfig) -> dict:
    out: dict = {}
    out["instanceType"] = value["instance_type"]
    out["volumeSizeInGb"] = value["volume_size_in_gb"]
    if "instance_count" in value:
        out["instanceCount"] = value["instance_count"]
    return out


def deserialize_json(data: dict) -> InstanceConfig:
    out: InstanceConfig = {}  # type: ignore[typeddict-item]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    else:
        raise DeserializationError("InstanceConfig.instance_type required")
    if "volumeSizeInGb" in data:
        out["volume_size_in_gb"] = data["volumeSizeInGb"]
    else:
        raise DeserializationError("InstanceConfig.volume_size_in_gb required")
    if "instanceCount" in data:
        out["instance_count"] = data["instanceCount"]
    return out
