"""Generated from Smithy shape ``com.amazonaws.lightsail#AttachDiskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.resource_name


class AttachDiskRequest(TypedDict, closed=True):
    disk_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The unique Lightsail disk name (<code>my-disk</code>).</p>"""
    instance_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the Lightsail instance where you want to utilize the storage disk.</p>"""
    disk_path: "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    """<p>The disk path to expose to the instance (<code>/dev/xvdf</code>).</p>"""
    auto_mounting: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value used to determine the automatic mounting of a storage volume to a virtual computer. The default value is <code>False</code>.</p> <important> <p>This value only applies to Lightsail for Research resources.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachDiskRequest) -> dict:
    out: dict = {}
    out["diskName"] = value["disk_name"]
    out["instanceName"] = value["instance_name"]
    out["diskPath"] = value["disk_path"]
    if "auto_mounting" in value:
        out["autoMounting"] = value["auto_mounting"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachDiskRequest:
    out: AttachDiskRequest = {}  # type: ignore[typeddict-item]
    if "diskName" in data:
        out["disk_name"] = data["diskName"]
    else:
        raise DeserializationError("AttachDiskRequest.disk_name required")
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError("AttachDiskRequest.instance_name required")
    if "diskPath" in data:
        out["disk_path"] = data["diskPath"]
    else:
        raise DeserializationError("AttachDiskRequest.disk_path required")
    if "autoMounting" in data:
        out["auto_mounting"] = data["autoMounting"]
    return out
