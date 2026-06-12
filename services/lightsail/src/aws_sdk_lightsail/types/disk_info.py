"""Generated from Smithy shape ``com.amazonaws.lightsail#DiskInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.string


class DiskInfo(TypedDict):
    name: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The disk name.</p>"""
    path: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The disk path.</p>"""
    size_in_gb: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The size of the disk in GB (<code>32</code>).</p>"""
    is_system_disk: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "path" in value:
        out["path"] = value["path"]
    if "size_in_gb" in value:
        out["sizeInGb"] = value["size_in_gb"]
    if "is_system_disk" in value:
        out["isSystemDisk"] = value["is_system_disk"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiskInfo:
    out: DiskInfo = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "path" in data:
        out["path"] = data["path"]
    if "sizeInGb" in data:
        out["size_in_gb"] = data["sizeInGb"]
    if "isSystemDisk" in data:
        out["is_system_disk"] = data["isSystemDisk"]
    return out
