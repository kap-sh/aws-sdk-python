"""Generated from Smithy shape ``com.amazonaws.guardduty#VolumeMount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class VolumeMount(TypedDict):
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Volume mount name.</p>"""
    mount_path: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Volume mount path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VolumeMount) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "mount_path" in value:
        out["mountPath"] = value["mount_path"]
    return out


def deserialize_json(data: dict) -> VolumeMount:
    out: VolumeMount = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "mountPath" in data:
        out["mount_path"] = data["mountPath"]
    return out
