"""Generated from Smithy shape ``com.amazonaws.lightsail#DiskSnapshotInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.integer


class DiskSnapshotInfo(TypedDict):
    size_in_gb: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The size of the disk in GB (<code>32</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskSnapshotInfo) -> dict:
    out: dict = {}
    if "size_in_gb" in value:
        out["sizeInGb"] = value["size_in_gb"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiskSnapshotInfo:
    out: DiskSnapshotInfo = {}  # type: ignore[typeddict-item]
    if "sizeInGb" in data:
        out["size_in_gb"] = data["sizeInGb"]
    return out
