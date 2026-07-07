"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerVolumeMount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.boolean
    import aws_sdk_batch.types.string


class EksContainerVolumeMount(TypedDict, closed=True):
    name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name the volume mount. This must match the name of one of the volumes in the pod.</p>"""
    mount_path: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The path on the container where the volume is mounted.</p>"""
    sub_path: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>A sub-path inside the referenced volume instead of its root.</p>"""
    read_only: NotRequired["aws_sdk_batch.types.boolean.Boolean"]
    """<p>If this value is <code>true</code>, the container has read-only access to the volume. Otherwise, the container can write to the volume. The default value is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerVolumeMount) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "mount_path" in value:
        out["mountPath"] = value["mount_path"]
    if "sub_path" in value:
        out["subPath"] = value["sub_path"]
    if "read_only" in value:
        out["readOnly"] = value["read_only"]
    return out


def deserialize_json(data: dict) -> EksContainerVolumeMount:
    out: EksContainerVolumeMount = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "mountPath" in data:
        out["mount_path"] = data["mountPath"]
    if "subPath" in data:
        out["sub_path"] = data["subPath"]
    if "readOnly" in data:
        out["read_only"] = data["readOnly"]
    return out
