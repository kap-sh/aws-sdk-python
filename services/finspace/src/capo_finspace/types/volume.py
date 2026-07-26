"""Generated from Smithy shape ``com.amazonaws.finspace#Volume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.volume_name
    import capo_finspace.types.volume_type


class Volume(TypedDict, closed=True):
    volume_name: NotRequired["capo_finspace.types.volume_name.VolumeName"]
    """<p>A unique identifier for the volume.</p>"""
    volume_type: NotRequired["capo_finspace.types.volume_type.VolumeType"]
    """<p> The type of file system volume. Currently, FinSpace only supports <code>NAS_1</code> volume type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Volume) -> dict:
    out: dict = {}
    if "volume_name" in value:
        out["volumeName"] = value["volume_name"]
    if "volume_type" in value:
        import capo_finspace.types.volume_type

        out["volumeType"] = capo_finspace.types.volume_type.serialize_json(
            value["volume_type"]
        )
    return out


def deserialize_json(data: dict) -> Volume:
    out: Volume = {}  # type: ignore[typeddict-item]
    if "volumeName" in data:
        out["volume_name"] = data["volumeName"]
    if "volumeType" in data:
        import capo_finspace.types.volume_type

        out["volume_type"] = capo_finspace.types.volume_type.deserialize_json(
            data["volumeType"]
        )
    return out
