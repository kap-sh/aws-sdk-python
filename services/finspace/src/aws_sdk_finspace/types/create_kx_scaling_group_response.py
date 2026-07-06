"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxScalingGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.availability_zone_id
    import aws_sdk_finspace.types.kx_environment_id
    import aws_sdk_finspace.types.kx_host_type
    import aws_sdk_finspace.types.kx_scaling_group_name
    import aws_sdk_finspace.types.kx_scaling_group_status
    import aws_sdk_finspace.types.timestamp


class CreateKxScalingGroupResponse(TypedDict, closed=True):
    environment_id: NotRequired[
        "aws_sdk_finspace.types.kx_environment_id.KxEnvironmentId"
    ]
    """<p>A unique identifier for the kdb environment, where you create the scaling group. </p>"""
    scaling_group_name: NotRequired[
        "aws_sdk_finspace.types.kx_scaling_group_name.KxScalingGroupName"
    ]
    """<p>A unique identifier for the kdb scaling group. </p>"""
    host_type: NotRequired["aws_sdk_finspace.types.kx_host_type.KxHostType"]
    """<p> The memory and CPU capabilities of the scaling group host on which FinSpace Managed kdb clusters will be placed. </p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_finspace.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The identifier of the availability zones.</p>"""
    status: NotRequired[
        "aws_sdk_finspace.types.kx_scaling_group_status.KxScalingGroupStatus"
    ]
    """<p>The status of scaling group.</p> <ul> <li> <p>CREATING – The scaling group creation is in progress.</p> </li> <li> <p>CREATE_FAILED – The scaling group creation has failed.</p> </li> <li> <p>ACTIVE – The scaling group is active.</p> </li> <li> <p>UPDATING – The scaling group is in the process of being updated.</p> </li> <li> <p>UPDATE_FAILED – The update action failed.</p> </li> <li> <p>DELETING – The scaling group is in the process of being deleted.</p> </li> <li> <p>DELETE_FAILED – The system failed to delete the scaling group.</p> </li> <li> <p>DELETED – The scaling group is successfully deleted.</p> </li> </ul>"""
    last_modified_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p> The last time that the scaling group was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000. </p>"""
    created_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p> The timestamp at which the scaling group was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxScalingGroupResponse) -> dict:
    out: dict = {}
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "scaling_group_name" in value:
        out["scalingGroupName"] = value["scaling_group_name"]
    if "host_type" in value:
        out["hostType"] = value["host_type"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "status" in value:
        import aws_sdk_finspace.types.kx_scaling_group_status

        out["status"] = aws_sdk_finspace.types.kx_scaling_group_status.serialize_json(
            value["status"]
        )
    if "last_modified_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["lastModifiedTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["last_modified_timestamp"]
        )
    if "created_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["createdTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> CreateKxScalingGroupResponse:
    out: CreateKxScalingGroupResponse = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "scalingGroupName" in data:
        out["scaling_group_name"] = data["scalingGroupName"]
    if "hostType" in data:
        out["host_type"] = data["hostType"]
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if "status" in data:
        import aws_sdk_finspace.types.kx_scaling_group_status

        out["status"] = aws_sdk_finspace.types.kx_scaling_group_status.deserialize_json(
            data["status"]
        )
    if "lastModifiedTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["last_modified_timestamp"] = (
            aws_sdk_finspace.types.timestamp.deserialize_json(
                data["lastModifiedTimestamp"]
            )
        )
    if "createdTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["created_timestamp"] = aws_sdk_finspace.types.timestamp.deserialize_json(
            data["createdTimestamp"]
        )
    return out
