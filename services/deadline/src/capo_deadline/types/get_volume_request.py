"""Generated from Smithy shape ``com.amazonaws.deadline#GetVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.volume_id


class GetVolumeRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm that contains the fleet.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the fleet that contains the volume.</p>"""
    volume_id: "capo_deadline.types.volume_id.VolumeId"
    """<p>The volume ID of the volume to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVolumeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVolumeRequest:
    out: GetVolumeRequest = {}  # type: ignore[typeddict-item]
    return out
