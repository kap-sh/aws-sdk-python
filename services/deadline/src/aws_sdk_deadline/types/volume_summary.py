"""Generated from Smithy shape ``com.amazonaws.deadline#VolumeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.persistent_volume_size_gi_b
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.volume_id
    import aws_sdk_deadline.types.volume_state
    import aws_sdk_deadline.types.worker_id


class VolumeSummary(TypedDict):
    volume_id: "aws_sdk_deadline.types.volume_id.VolumeId"
    """<p>The volume ID.</p>"""
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm that contains the fleet.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID of the fleet that contains the volume.</p>"""
    state: "aws_sdk_deadline.types.volume_state.VolumeState"
    """<p>The state of the volume.</p>"""
    size_gi_b: (
        "aws_sdk_deadline.types.persistent_volume_size_gi_b.PersistentVolumeSizeGiB"
    )
    """<p>The volume size in GiB.</p>"""
    availability_zone_id: "aws_sdk_deadline.types.string.String"
    """<p>The Availability Zone ID of the volume.</p>"""
    attached_worker_id: NotRequired["aws_sdk_deadline.types.worker_id.WorkerId"]
    """<p>The worker ID of the worker the volume is attached to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VolumeSummary) -> dict:
    out: dict = {}
    out["volumeId"] = value["volume_id"]
    out["farmId"] = value["farm_id"]
    out["fleetId"] = value["fleet_id"]
    import aws_sdk_deadline.types.volume_state

    out["state"] = aws_sdk_deadline.types.volume_state.serialize_json(value["state"])
    out["sizeGiB"] = value["size_gi_b"]
    out["availabilityZoneId"] = value["availability_zone_id"]
    if "attached_worker_id" in value:
        out["attachedWorkerId"] = value["attached_worker_id"]
    return out


def deserialize_json(data: dict) -> VolumeSummary:
    out: VolumeSummary = {}  # type: ignore[typeddict-item]
    if "volumeId" in data:
        out["volume_id"] = data["volumeId"]
    else:
        raise DeserializationError("VolumeSummary.volume_id required")
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("VolumeSummary.farm_id required")
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("VolumeSummary.fleet_id required")
    if "state" in data:
        import aws_sdk_deadline.types.volume_state

        out["state"] = aws_sdk_deadline.types.volume_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("VolumeSummary.state required")
    if "sizeGiB" in data:
        out["size_gi_b"] = data["sizeGiB"]
    else:
        raise DeserializationError("VolumeSummary.size_gi_b required")
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    else:
        raise DeserializationError("VolumeSummary.availability_zone_id required")
    if "attachedWorkerId" in data:
        out["attached_worker_id"] = data["attachedWorkerId"]
    return out
