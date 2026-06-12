"""Generated from Smithy shape ``com.amazonaws.lightsail#AttachedDisk``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.string


class AttachedDisk(TypedDict):
    path: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The path of the disk (<code>/dev/xvdf</code>).</p>"""
    size_in_gb: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The size of the disk in GB.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachedDisk) -> dict:
    out: dict = {}
    if "path" in value:
        out["path"] = value["path"]
    if "size_in_gb" in value:
        out["sizeInGb"] = value["size_in_gb"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachedDisk:
    out: AttachedDisk = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    if "sizeInGb" in data:
        out["size_in_gb"] = data["sizeInGb"]
    return out
