"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.volume_id


class DeleteVolumeRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm that contains the fleet.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the fleet that contains the volume.</p>"""
    volume_id: "aws_sdk_deadline.types.volume_id.VolumeId"
    """<p>The volume ID of the volume to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVolumeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVolumeRequest:
    out: DeleteVolumeRequest = {}  # type: ignore[typeddict-item]
    return out
