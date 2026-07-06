"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxVolumeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.availability_zone_ids
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.kx_attached_clusters
    import aws_sdk_finspace.types.kx_az_mode
    import aws_sdk_finspace.types.kx_environment_id
    import aws_sdk_finspace.types.kx_nas1_configuration
    import aws_sdk_finspace.types.kx_volume_arn
    import aws_sdk_finspace.types.kx_volume_name
    import aws_sdk_finspace.types.kx_volume_status
    import aws_sdk_finspace.types.kx_volume_status_reason
    import aws_sdk_finspace.types.kx_volume_type
    import aws_sdk_finspace.types.timestamp


class GetKxVolumeResponse(TypedDict, closed=True):
    environment_id: NotRequired[
        "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId"
    ]
    """<p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>"""
    volume_name: NotRequired["aws_sdk_finspace.types.kx_volume_name.KxVolumeName"]
    """<p> A unique identifier for the volume.</p>"""
    volume_type: NotRequired["aws_sdk_finspace.types.kx_volume_type.KxVolumeType"]
    """<p> The type of file system volume. Currently, FinSpace only supports <code>NAS_1</code> volume type. </p>"""
    volume_arn: NotRequired["aws_sdk_finspace.types.kx_volume_arn.KxVolumeArn"]
    """<p> The ARN identifier of the volume. </p>"""
    nas1_configuration: NotRequired[
        "aws_sdk_finspace.types.kx_nas1_configuration.KxNAS1Configuration"
    ]
    """<p> Specifies the configuration for the Network attached storage (NAS_1) file system volume.</p>"""
    status: NotRequired["aws_sdk_finspace.types.kx_volume_status.KxVolumeStatus"]
    """<p>The status of volume creation.</p> <ul> <li> <p>CREATING – The volume creation is in progress.</p> </li> <li> <p>CREATE_FAILED – The volume creation has failed.</p> </li> <li> <p>ACTIVE – The volume is active.</p> </li> <li> <p>UPDATING – The volume is in the process of being updated.</p> </li> <li> <p>UPDATE_FAILED – The update action failed.</p> </li> <li> <p>UPDATED – The volume is successfully updated.</p> </li> <li> <p>DELETING – The volume is in the process of being deleted.</p> </li> <li> <p>DELETE_FAILED – The system failed to delete the volume.</p> </li> <li> <p>DELETED – The volume is successfully deleted.</p> </li> </ul>"""
    status_reason: NotRequired[
        "aws_sdk_finspace.types.kx_volume_status_reason.KxVolumeStatusReason"
    ]
    """<p>The error message when a failed state occurs. </p>"""
    created_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p> The timestamp at which the volume was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000. </p>"""
    description: NotRequired["aws_sdk_finspace.types.description.Description"]
    """<p> A description of the volume. </p>"""
    az_mode: NotRequired["aws_sdk_finspace.types.kx_az_mode.KxAzMode"]
    """<p>The number of availability zones you want to assign per volume. Currently, FinSpace only supports <code>SINGLE</code> for volumes. This places dataview in a single AZ.</p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_finspace.types.availability_zone_ids.AvailabilityZoneIds"
    ]
    """<p>The identifier of the availability zones.</p>"""
    last_modified_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The last time that the volume was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    attached_clusters: NotRequired[
        "aws_sdk_finspace.types.kx_attached_clusters.KxAttachedClusters"
    ]
    """<p> A list of cluster identifiers that a volume is attached to. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxVolumeResponse) -> dict:
    out: dict = {}
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "volume_name" in value:
        out["volumeName"] = value["volume_name"]
    if "volume_type" in value:
        import aws_sdk_finspace.types.kx_volume_type

        out["volumeType"] = aws_sdk_finspace.types.kx_volume_type.serialize_json(
            value["volume_type"]
        )
    if "volume_arn" in value:
        out["volumeArn"] = value["volume_arn"]
    if "nas1_configuration" in value:
        import aws_sdk_finspace.types.kx_nas1_configuration

        out["nas1Configuration"] = (
            aws_sdk_finspace.types.kx_nas1_configuration.serialize_json(
                value["nas1_configuration"]
            )
        )
    if "status" in value:
        import aws_sdk_finspace.types.kx_volume_status

        out["status"] = aws_sdk_finspace.types.kx_volume_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "created_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["createdTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "az_mode" in value:
        import aws_sdk_finspace.types.kx_az_mode

        out["azMode"] = aws_sdk_finspace.types.kx_az_mode.serialize_json(
            value["az_mode"]
        )
    if "availability_zone_ids" in value:
        import aws_sdk_finspace.types.availability_zone_ids

        out["availabilityZoneIds"] = (
            aws_sdk_finspace.types.availability_zone_ids.serialize_json(
                value["availability_zone_ids"]
            )
        )
    if "last_modified_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["lastModifiedTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["last_modified_timestamp"]
        )
    if "attached_clusters" in value:
        import aws_sdk_finspace.types.kx_attached_clusters

        out["attachedClusters"] = (
            aws_sdk_finspace.types.kx_attached_clusters.serialize_json(
                value["attached_clusters"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetKxVolumeResponse:
    out: GetKxVolumeResponse = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "volumeName" in data:
        out["volume_name"] = data["volumeName"]
    if "volumeType" in data:
        import aws_sdk_finspace.types.kx_volume_type

        out["volume_type"] = aws_sdk_finspace.types.kx_volume_type.deserialize_json(
            data["volumeType"]
        )
    if "volumeArn" in data:
        out["volume_arn"] = data["volumeArn"]
    if "nas1Configuration" in data:
        import aws_sdk_finspace.types.kx_nas1_configuration

        out["nas1_configuration"] = (
            aws_sdk_finspace.types.kx_nas1_configuration.deserialize_json(
                data["nas1Configuration"]
            )
        )
    if "status" in data:
        import aws_sdk_finspace.types.kx_volume_status

        out["status"] = aws_sdk_finspace.types.kx_volume_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "createdTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["created_timestamp"] = aws_sdk_finspace.types.timestamp.deserialize_json(
            data["createdTimestamp"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "azMode" in data:
        import aws_sdk_finspace.types.kx_az_mode

        out["az_mode"] = aws_sdk_finspace.types.kx_az_mode.deserialize_json(
            data["azMode"]
        )
    if "availabilityZoneIds" in data:
        import aws_sdk_finspace.types.availability_zone_ids

        out["availability_zone_ids"] = (
            aws_sdk_finspace.types.availability_zone_ids.deserialize_json(
                data["availabilityZoneIds"]
            )
        )
    if "lastModifiedTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["last_modified_timestamp"] = (
            aws_sdk_finspace.types.timestamp.deserialize_json(
                data["lastModifiedTimestamp"]
            )
        )
    if "attachedClusters" in data:
        import aws_sdk_finspace.types.kx_attached_clusters

        out["attached_clusters"] = (
            aws_sdk_finspace.types.kx_attached_clusters.deserialize_json(
                data["attachedClusters"]
            )
        )
    return out
