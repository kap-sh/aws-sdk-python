"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxVolumeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_environment_id
    import aws_sdk_finspace.types.kx_volume_name


class GetKxVolumeRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>"""
    volume_name: "aws_sdk_finspace.types.kx_volume_name.KxVolumeName"
    """<p>A unique identifier for the volume.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxVolumeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKxVolumeRequest:
    out: GetKxVolumeRequest = {}  # type: ignore[typeddict-item]
    return out
