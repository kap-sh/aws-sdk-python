"""Generated from Smithy shape ``com.amazonaws.deadline#GetVolumeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.ebs_volume_type
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.persistent_volume_iops
    import aws_sdk_deadline.types.persistent_volume_size_gi_b
    import aws_sdk_deadline.types.persistent_volume_throughput_mi_b
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.timestamp
    import aws_sdk_deadline.types.volume_id
    import aws_sdk_deadline.types.volume_state
    import aws_sdk_deadline.types.worker_id


class GetVolumeResponse(TypedDict):
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
    volume_type: "aws_sdk_deadline.types.ebs_volume_type.EbsVolumeType"
    """<p>The EBS volume type.</p>"""
    iops: NotRequired[
        "aws_sdk_deadline.types.persistent_volume_iops.PersistentVolumeIops"
    ]
    """<p>The IOPS of the volume.</p>"""
    throughput_mi_b: NotRequired[
        "aws_sdk_deadline.types.persistent_volume_throughput_mi_b.PersistentVolumeThroughputMiB"
    ]
    """<p>The throughput of the volume in MiB.</p>"""
    created_at: "aws_sdk_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    last_assigned_at: NotRequired["aws_sdk_deadline.types.timestamp.Timestamp"]
    """<p>The date and time the volume was last assigned to a worker.</p>"""
    last_released_at: NotRequired["aws_sdk_deadline.types.timestamp.Timestamp"]
    """<p>The date and time the volume was last released from a worker.</p>"""
    expires_at: NotRequired["aws_sdk_deadline.types.timestamp.Timestamp"]
    """<p>The date and time the volume expires and will be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVolumeResponse) -> dict:
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
    import aws_sdk_deadline.types.ebs_volume_type

    out["volumeType"] = aws_sdk_deadline.types.ebs_volume_type.serialize_json(
        value["volume_type"]
    )
    if "iops" in value:
        out["iops"] = value["iops"]
    if "throughput_mi_b" in value:
        out["throughputMiB"] = value["throughput_mi_b"]
    import aws_sdk_deadline.types.created_at

    out["createdAt"] = aws_sdk_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    if "last_assigned_at" in value:
        import aws_sdk_deadline.types.timestamp

        out["lastAssignedAt"] = aws_sdk_deadline.types.timestamp.serialize_json(
            value["last_assigned_at"]
        )
    if "last_released_at" in value:
        import aws_sdk_deadline.types.timestamp

        out["lastReleasedAt"] = aws_sdk_deadline.types.timestamp.serialize_json(
            value["last_released_at"]
        )
    if "expires_at" in value:
        import aws_sdk_deadline.types.timestamp

        out["expiresAt"] = aws_sdk_deadline.types.timestamp.serialize_json(
            value["expires_at"]
        )
    return out


def deserialize_json(data: dict) -> GetVolumeResponse:
    out: GetVolumeResponse = {}  # type: ignore[typeddict-item]
    if "volumeId" in data:
        out["volume_id"] = data["volumeId"]
    else:
        raise DeserializationError("GetVolumeResponse.volume_id required")
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("GetVolumeResponse.farm_id required")
    if "fleetId" in data:
        out["fleet_id"] = data["fleetId"]
    else:
        raise DeserializationError("GetVolumeResponse.fleet_id required")
    if "state" in data:
        import aws_sdk_deadline.types.volume_state

        out["state"] = aws_sdk_deadline.types.volume_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("GetVolumeResponse.state required")
    if "sizeGiB" in data:
        out["size_gi_b"] = data["sizeGiB"]
    else:
        raise DeserializationError("GetVolumeResponse.size_gi_b required")
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    else:
        raise DeserializationError("GetVolumeResponse.availability_zone_id required")
    if "attachedWorkerId" in data:
        out["attached_worker_id"] = data["attachedWorkerId"]
    if "volumeType" in data:
        import aws_sdk_deadline.types.ebs_volume_type

        out["volume_type"] = aws_sdk_deadline.types.ebs_volume_type.deserialize_json(
            data["volumeType"]
        )
    else:
        raise DeserializationError("GetVolumeResponse.volume_type required")
    if "iops" in data:
        out["iops"] = data["iops"]
    if "throughputMiB" in data:
        out["throughput_mi_b"] = data["throughputMiB"]
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetVolumeResponse.created_at required")
    if "lastAssignedAt" in data:
        import aws_sdk_deadline.types.timestamp

        out["last_assigned_at"] = aws_sdk_deadline.types.timestamp.deserialize_json(
            data["lastAssignedAt"]
        )
    if "lastReleasedAt" in data:
        import aws_sdk_deadline.types.timestamp

        out["last_released_at"] = aws_sdk_deadline.types.timestamp.deserialize_json(
            data["lastReleasedAt"]
        )
    if "expiresAt" in data:
        import aws_sdk_deadline.types.timestamp

        out["expires_at"] = aws_sdk_deadline.types.timestamp.deserialize_json(
            data["expiresAt"]
        )
    return out
