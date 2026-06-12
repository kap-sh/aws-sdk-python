"""Generated from Smithy shape ``com.amazonaws.batch#MountPoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.boolean
    import aws_sdk_batch.types.string


class MountPoint(TypedDict):
    container_path: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The path on the container where the host volume is mounted.</p>"""
    read_only: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>If this value is <code>true</code>, the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is <code>false</code>.</p>"""
    source_volume: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the volume to mount.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MountPoint) -> dict:
    out: dict = {}
    if "container_path" in value:
        out["containerPath"] = value["container_path"]
    if "read_only" in value:
        out["readOnly"] = value["read_only"]
    if "source_volume" in value:
        out["sourceVolume"] = value["source_volume"]
    return out


def deserialize_json(data: dict) -> MountPoint:
    out: MountPoint = {}  # type: ignore[typeddict-item]
    if "containerPath" in data:
        out["container_path"] = data["containerPath"]
    if "readOnly" in data:
        out["read_only"] = data["readOnly"]
    if "sourceVolume" in data:
        out["source_volume"] = data["sourceVolume"]
    return out
