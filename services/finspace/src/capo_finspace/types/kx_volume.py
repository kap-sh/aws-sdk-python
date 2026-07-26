"""Generated from Smithy shape ``com.amazonaws.finspace#KxVolume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.availability_zone_ids
    import capo_finspace.types.description
    import capo_finspace.types.kx_az_mode
    import capo_finspace.types.kx_volume_name
    import capo_finspace.types.kx_volume_status
    import capo_finspace.types.kx_volume_status_reason
    import capo_finspace.types.kx_volume_type
    import capo_finspace.types.timestamp


class KxVolume(TypedDict, closed=True):
    volume_name: NotRequired["capo_finspace.types.kx_volume_name.KxVolumeName"]
    """<p>A unique identifier for the volume.</p>"""
    volume_type: NotRequired["capo_finspace.types.kx_volume_type.KxVolumeType"]
    """<p> The type of file system volume. Currently, FinSpace only supports <code>NAS_1</code> volume type. </p>"""
    status: NotRequired["capo_finspace.types.kx_volume_status.KxVolumeStatus"]
    """<p>The status of volume.</p> <ul> <li> <p>CREATING – The volume creation is in progress.</p> </li> <li> <p>CREATE_FAILED – The volume creation has failed.</p> </li> <li> <p>ACTIVE – The volume is active.</p> </li> <li> <p>UPDATING – The volume is in the process of being updated.</p> </li> <li> <p>UPDATE_FAILED – The update action failed.</p> </li> <li> <p>UPDATED – The volume is successfully updated.</p> </li> <li> <p>DELETING – The volume is in the process of being deleted.</p> </li> <li> <p>DELETE_FAILED – The system failed to delete the volume.</p> </li> <li> <p>DELETED – The volume is successfully deleted.</p> </li> </ul>"""
    description: NotRequired["capo_finspace.types.description.Description"]
    """<p> A description of the volume. </p>"""
    status_reason: NotRequired[
        "capo_finspace.types.kx_volume_status_reason.KxVolumeStatusReason"
    ]
    """<p>The error message when a failed state occurs. </p>"""
    az_mode: NotRequired["capo_finspace.types.kx_az_mode.KxAzMode"]
    """<p>The number of availability zones you want to assign per volume. Currently, FinSpace only supports <code>SINGLE</code> for volumes. This places dataview in a single AZ.</p>"""
    availability_zone_ids: NotRequired[
        "capo_finspace.types.availability_zone_ids.AvailabilityZoneIds"
    ]
    """<p>The identifier of the availability zones.</p>"""
    created_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p> The timestamp at which the volume was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    last_modified_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p>The last time that the volume was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxVolume) -> dict:
    out: dict = {}
    if "volume_name" in value:
        out["volumeName"] = value["volume_name"]
    if "volume_type" in value:
        import capo_finspace.types.kx_volume_type

        out["volumeType"] = capo_finspace.types.kx_volume_type.serialize_json(
            value["volume_type"]
        )
    if "status" in value:
        import capo_finspace.types.kx_volume_status

        out["status"] = capo_finspace.types.kx_volume_status.serialize_json(
            value["status"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "az_mode" in value:
        import capo_finspace.types.kx_az_mode

        out["azMode"] = capo_finspace.types.kx_az_mode.serialize_json(value["az_mode"])
    if "availability_zone_ids" in value:
        import capo_finspace.types.availability_zone_ids

        out["availabilityZoneIds"] = (
            capo_finspace.types.availability_zone_ids.serialize_json(
                value["availability_zone_ids"]
            )
        )
    if "created_timestamp" in value:
        import capo_finspace.types.timestamp

        out["createdTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "last_modified_timestamp" in value:
        import capo_finspace.types.timestamp

        out["lastModifiedTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["last_modified_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> KxVolume:
    out: KxVolume = {}  # type: ignore[typeddict-item]
    if "volumeName" in data:
        out["volume_name"] = data["volumeName"]
    if "volumeType" in data:
        import capo_finspace.types.kx_volume_type

        out["volume_type"] = capo_finspace.types.kx_volume_type.deserialize_json(
            data["volumeType"]
        )
    if "status" in data:
        import capo_finspace.types.kx_volume_status

        out["status"] = capo_finspace.types.kx_volume_status.deserialize_json(
            data["status"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "azMode" in data:
        import capo_finspace.types.kx_az_mode

        out["az_mode"] = capo_finspace.types.kx_az_mode.deserialize_json(data["azMode"])
    if "availabilityZoneIds" in data:
        import capo_finspace.types.availability_zone_ids

        out["availability_zone_ids"] = (
            capo_finspace.types.availability_zone_ids.deserialize_json(
                data["availabilityZoneIds"]
            )
        )
    if "createdTimestamp" in data:
        import capo_finspace.types.timestamp

        out["created_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["createdTimestamp"]
        )
    if "lastModifiedTimestamp" in data:
        import capo_finspace.types.timestamp

        out["last_modified_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["lastModifiedTimestamp"]
        )
    return out
