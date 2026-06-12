"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxScalingGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.arn
    import aws_sdk_finspace.types.availability_zone_id
    import aws_sdk_finspace.types.kx_cluster_name_list
    import aws_sdk_finspace.types.kx_cluster_status_reason
    import aws_sdk_finspace.types.kx_host_type
    import aws_sdk_finspace.types.kx_scaling_group_name
    import aws_sdk_finspace.types.kx_scaling_group_status
    import aws_sdk_finspace.types.timestamp


class GetKxScalingGroupResponse(TypedDict):
    scaling_group_name: NotRequired[
        "aws_sdk_finspace.types.kx_scaling_group_name.KxScalingGroupName"
    ]
    """<p>A unique identifier for the kdb scaling group. </p>"""
    scaling_group_arn: NotRequired["aws_sdk_finspace.types.arn.arn"]
    """<p> The ARN identifier for the scaling group. </p>"""
    host_type: NotRequired["aws_sdk_finspace.types.kx_host_type.KxHostType"]
    """<p> The memory and CPU capabilities of the scaling group host on which FinSpace Managed kdb clusters will be placed.</p> <p>It can have one of the following values:</p> <ul> <li> <p> <code>kx.sg.large</code> – The host type with a configuration of 16 GiB memory and 2 vCPUs.</p> </li> <li> <p> <code>kx.sg.xlarge</code> – The host type with a configuration of 32 GiB memory and 4 vCPUs.</p> </li> <li> <p> <code>kx.sg.2xlarge</code> – The host type with a configuration of 64 GiB memory and 8 vCPUs.</p> </li> <li> <p> <code>kx.sg.4xlarge</code> – The host type with a configuration of 108 GiB memory and 16 vCPUs.</p> </li> <li> <p> <code>kx.sg.8xlarge</code> – The host type with a configuration of 216 GiB memory and 32 vCPUs.</p> </li> <li> <p> <code>kx.sg.16xlarge</code> – The host type with a configuration of 432 GiB memory and 64 vCPUs.</p> </li> <li> <p> <code>kx.sg.32xlarge</code> – The host type with a configuration of 864 GiB memory and 128 vCPUs.</p> </li> <li> <p> <code>kx.sg1.16xlarge</code> – The host type with a configuration of 1949 GiB memory and 64 vCPUs.</p> </li> <li> <p> <code>kx.sg1.24xlarge</code> – The host type with a configuration of 2948 GiB memory and 96 vCPUs.</p> </li> </ul>"""
    clusters: NotRequired[
        "aws_sdk_finspace.types.kx_cluster_name_list.KxClusterNameList"
    ]
    """<p> The list of Managed kdb clusters that are currently active in the given scaling group. </p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_finspace.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The identifier of the availability zones.</p>"""
    status: NotRequired[
        "aws_sdk_finspace.types.kx_scaling_group_status.KxScalingGroupStatus"
    ]
    """<p>The status of scaling group.</p> <ul> <li> <p>CREATING – The scaling group creation is in progress.</p> </li> <li> <p>CREATE_FAILED – The scaling group creation has failed.</p> </li> <li> <p>ACTIVE – The scaling group is active.</p> </li> <li> <p>UPDATING – The scaling group is in the process of being updated.</p> </li> <li> <p>UPDATE_FAILED – The update action failed.</p> </li> <li> <p>DELETING – The scaling group is in the process of being deleted.</p> </li> <li> <p>DELETE_FAILED – The system failed to delete the scaling group.</p> </li> <li> <p>DELETED – The scaling group is successfully deleted.</p> </li> </ul>"""
    status_reason: NotRequired[
        "aws_sdk_finspace.types.kx_cluster_status_reason.KxClusterStatusReason"
    ]
    """<p> The error message when a failed state occurs. </p>"""
    last_modified_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p> The last time that the scaling group was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000. </p>"""
    created_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p> The timestamp at which the scaling group was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxScalingGroupResponse) -> dict:
    out: dict = {}
    if "scaling_group_name" in value:
        out["scalingGroupName"] = value["scaling_group_name"]
    if "scaling_group_arn" in value:
        out["scalingGroupArn"] = value["scaling_group_arn"]
    if "host_type" in value:
        out["hostType"] = value["host_type"]
    if "clusters" in value:
        import aws_sdk_finspace.types.kx_cluster_name_list

        out["clusters"] = aws_sdk_finspace.types.kx_cluster_name_list.serialize_json(
            value["clusters"]
        )
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "status" in value:
        import aws_sdk_finspace.types.kx_scaling_group_status

        out["status"] = aws_sdk_finspace.types.kx_scaling_group_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
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


def deserialize_json(data: dict) -> GetKxScalingGroupResponse:
    out: GetKxScalingGroupResponse = {}  # type: ignore[typeddict-item]
    if "scalingGroupName" in data:
        out["scaling_group_name"] = data["scalingGroupName"]
    if "scalingGroupArn" in data:
        out["scaling_group_arn"] = data["scalingGroupArn"]
    if "hostType" in data:
        out["host_type"] = data["hostType"]
    if "clusters" in data:
        import aws_sdk_finspace.types.kx_cluster_name_list

        out["clusters"] = aws_sdk_finspace.types.kx_cluster_name_list.deserialize_json(
            data["clusters"]
        )
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if "status" in data:
        import aws_sdk_finspace.types.kx_scaling_group_status

        out["status"] = aws_sdk_finspace.types.kx_scaling_group_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
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
