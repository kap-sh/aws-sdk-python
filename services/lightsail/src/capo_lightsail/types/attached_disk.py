"""Generated from Smithy shape ``com.amazonaws.lightsail#AttachedDisk``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.integer
    import capo_lightsail.types.string


class AttachedDisk(TypedDict, closed=True):
    path: NotRequired["capo_lightsail.types.string.string"]
    """<p>The path of the disk (<code>/dev/xvdf</code>).</p>"""
    size_in_gb: NotRequired["capo_lightsail.types.integer.integer"]
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
