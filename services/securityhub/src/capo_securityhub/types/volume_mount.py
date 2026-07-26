"""Generated from Smithy shape ``com.amazonaws.securityhub#VolumeMount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class VolumeMount(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the volume. </p>"""
    mount_path: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path in the container at which the volume should be mounted. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VolumeMount) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "mount_path" in value:
        out["MountPath"] = value["mount_path"]
    return out


def deserialize_json(data: dict) -> VolumeMount:
    out: VolumeMount = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "MountPath" in data:
        out["mount_path"] = data["MountPath"]
    return out
