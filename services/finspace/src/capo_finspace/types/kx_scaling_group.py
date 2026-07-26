"""Generated from Smithy shape ``com.amazonaws.finspace#KxScalingGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.availability_zone_id
    import capo_finspace.types.kx_cluster_name_list
    import capo_finspace.types.kx_cluster_status_reason
    import capo_finspace.types.kx_host_type
    import capo_finspace.types.kx_scaling_group_name
    import capo_finspace.types.kx_scaling_group_status
    import capo_finspace.types.timestamp


class KxScalingGroup(TypedDict, closed=True):
    scaling_group_name: NotRequired[
        "capo_finspace.types.kx_scaling_group_name.KxScalingGroupName"
    ]
    """<p>A unique identifier for the kdb scaling group. </p>"""
    host_type: NotRequired["capo_finspace.types.kx_host_type.KxHostType"]
    """<p> The memory and CPU capabilities of the scaling group host on which FinSpace Managed kdb clusters will be placed.</p> <p>You can add one of the following values:</p> <ul> <li> <p> <code>kx.sg.large</code> – The host type with a configuration of 16 GiB memory and 2 vCPUs.</p> </li> <li> <p> <code>kx.sg.xlarge</code> – The host type with a configuration of 32 GiB memory and 4 vCPUs.</p> </li> <li> <p> <code>kx.sg.2xlarge</code> – The host type with a configuration of 64 GiB memory and 8 vCPUs.</p> </li> <li> <p> <code>kx.sg.4xlarge</code> – The host type with a configuration of 108 GiB memory and 16 vCPUs.</p> </li> <li> <p> <code>kx.sg.8xlarge</code> – The host type with a configuration of 216 GiB memory and 32 vCPUs.</p> </li> <li> <p> <code>kx.sg.16xlarge</code> – The host type with a configuration of 432 GiB memory and 64 vCPUs.</p> </li> <li> <p> <code>kx.sg.32xlarge</code> – The host type with a configuration of 864 GiB memory and 128 vCPUs.</p> </li> <li> <p> <code>kx.sg1.16xlarge</code> – The host type with a configuration of 1949 GiB memory and 64 vCPUs.</p> </li> <li> <p> <code>kx.sg1.24xlarge</code> – The host type with a configuration of 2948 GiB memory and 96 vCPUs.</p> </li> </ul>"""
    clusters: NotRequired["capo_finspace.types.kx_cluster_name_list.KxClusterNameList"]
    """<p> The list of clusters currently active in a given scaling group. </p>"""
    availability_zone_id: NotRequired[
        "capo_finspace.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The identifier of the availability zones.</p>"""
    status: NotRequired[
        "capo_finspace.types.kx_scaling_group_status.KxScalingGroupStatus"
    ]
    """<p> The status of scaling groups. </p>"""
    status_reason: NotRequired[
        "capo_finspace.types.kx_cluster_status_reason.KxClusterStatusReason"
    ]
    """<p> The error message when a failed state occurs. </p>"""
    last_modified_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p> The last time that the scaling group was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000. </p>"""
    created_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p> The timestamp at which the scaling group was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxScalingGroup) -> dict:
    out: dict = {}
    if "scaling_group_name" in value:
        out["scalingGroupName"] = value["scaling_group_name"]
    if "host_type" in value:
        out["hostType"] = value["host_type"]
    if "clusters" in value:
        import capo_finspace.types.kx_cluster_name_list

        out["clusters"] = capo_finspace.types.kx_cluster_name_list.serialize_json(
            value["clusters"]
        )
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "status" in value:
        import capo_finspace.types.kx_scaling_group_status

        out["status"] = capo_finspace.types.kx_scaling_group_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "last_modified_timestamp" in value:
        import capo_finspace.types.timestamp

        out["lastModifiedTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["last_modified_timestamp"]
        )
    if "created_timestamp" in value:
        import capo_finspace.types.timestamp

        out["createdTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["created_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> KxScalingGroup:
    out: KxScalingGroup = {}  # type: ignore[typeddict-item]
    if "scalingGroupName" in data:
        out["scaling_group_name"] = data["scalingGroupName"]
    if "hostType" in data:
        out["host_type"] = data["hostType"]
    if "clusters" in data:
        import capo_finspace.types.kx_cluster_name_list

        out["clusters"] = capo_finspace.types.kx_cluster_name_list.deserialize_json(
            data["clusters"]
        )
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if "status" in data:
        import capo_finspace.types.kx_scaling_group_status

        out["status"] = capo_finspace.types.kx_scaling_group_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "lastModifiedTimestamp" in data:
        import capo_finspace.types.timestamp

        out["last_modified_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["lastModifiedTimestamp"]
        )
    if "createdTimestamp" in data:
        import capo_finspace.types.timestamp

        out["created_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["createdTimestamp"]
        )
    return out
