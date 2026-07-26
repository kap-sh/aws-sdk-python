"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.kx_environment_id
    import capo_finspace.types.kx_volume_name


class GetKxVolumeRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>"""
    volume_name: "capo_finspace.types.kx_volume_name.KxVolumeName"
    """<p>A unique identifier for the volume.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxVolumeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKxVolumeRequest:
    out: GetKxVolumeRequest = {}  # type: ignore[typeddict-item]
    return out
