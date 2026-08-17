"""Generated from Smithy shape ``com.amazonaws.ecs#MountPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.string


class MountPoint(TypedDict, closed=True):
    source_volume: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the volume to mount. Must be a volume name referenced in the <code>name</code> parameter of task definition <code>volume</code>.</p>"""
    container_path: NotRequired["capo_ecs.types.string.String"]
    """<p>The path on the container to mount the host volume at.</p>"""
    read_only: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If this value is <code>true</code>, the container has read-only access to the volume. If this value is <code>false</code>, then the container can write to the volume. The default value is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MountPoint) -> dict:
    out: dict = {}
    if "source_volume" in value:
        out["sourceVolume"] = value["source_volume"]
    if "container_path" in value:
        out["containerPath"] = value["container_path"]
    if "read_only" in value:
        out["readOnly"] = value["read_only"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MountPoint:
    out: MountPoint = {}  # type: ignore[typeddict-item]
    if data.get("sourceVolume") is not None:
        out["source_volume"] = data["sourceVolume"]
    if data.get("containerPath") is not None:
        out["container_path"] = data["containerPath"]
    if data.get("readOnly") is not None:
        out["read_only"] = data["readOnly"]
    return out
