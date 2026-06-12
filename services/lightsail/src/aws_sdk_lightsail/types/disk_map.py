"""Generated from Smithy shape ``com.amazonaws.lightsail#DiskMap``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.resource_name


class DiskMap(TypedDict):
    original_disk_path: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The original disk path exposed to the instance (for example, <code>/dev/sdh</code>).</p>"""
    new_disk_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The new disk name (<code>my-new-disk</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskMap) -> dict:
    out: dict = {}
    if "original_disk_path" in value:
        out["originalDiskPath"] = value["original_disk_path"]
    if "new_disk_name" in value:
        out["newDiskName"] = value["new_disk_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiskMap:
    out: DiskMap = {}  # type: ignore[typeddict-item]
    if "originalDiskPath" in data:
        out["original_disk_path"] = data["originalDiskPath"]
    if "newDiskName" in data:
        out["new_disk_name"] = data["newDiskName"]
    return out
