"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeReservedCapacityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.availability_zone
    import capo_sagemaker.types.available_instance_count
    import capo_sagemaker.types.in_use_instance_count
    import capo_sagemaker.types.reserved_capacity_arn
    import capo_sagemaker.types.reserved_capacity_duration_hours
    import capo_sagemaker.types.reserved_capacity_duration_minutes
    import capo_sagemaker.types.reserved_capacity_instance_type
    import capo_sagemaker.types.reserved_capacity_status
    import capo_sagemaker.types.reserved_capacity_type
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.total_instance_count
    import capo_sagemaker.types.ultra_server_summary


class DescribeReservedCapacityResponse(TypedDict, closed=True):
    reserved_capacity_arn: NotRequired[
        "capo_sagemaker.types.reserved_capacity_arn.ReservedCapacityArn"
    ]
    """<p>ARN of the reserved capacity.</p>"""
    reserved_capacity_type: NotRequired[
        "capo_sagemaker.types.reserved_capacity_type.ReservedCapacityType"
    ]
    """<p>The type of reserved capacity.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.reserved_capacity_status.ReservedCapacityStatus"
    ]
    """<p>The current status of the reserved capacity.</p>"""
    availability_zone: NotRequired[
        "capo_sagemaker.types.availability_zone.AvailabilityZone"
    ]
    """<p>The Availability Zone where the reserved capacity is provisioned.</p>"""
    duration_hours: NotRequired[
        "capo_sagemaker.types.reserved_capacity_duration_hours.ReservedCapacityDurationHours"
    ]
    """<p>The total duration of the reserved capacity in hours.</p>"""
    duration_minutes: NotRequired[
        "capo_sagemaker.types.reserved_capacity_duration_minutes.ReservedCapacityDurationMinutes"
    ]
    """<p>The number of minutes for the duration of the reserved capacity. For example, if a reserved capacity starts at 08:55 and ends at 11:30, the minutes field would be 35.</p>"""
    start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when the reserved capacity becomes active.</p>"""
    end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp when the reserved capacity expires.</p>"""
    instance_type: NotRequired[
        "capo_sagemaker.types.reserved_capacity_instance_type.ReservedCapacityInstanceType"
    ]
    """<p>The Amazon EC2 instance type used in the reserved capacity.</p>"""
    total_instance_count: NotRequired[
        "capo_sagemaker.types.total_instance_count.TotalInstanceCount"
    ]
    """<p>The total number of instances allocated to this reserved capacity.</p>"""
    available_instance_count: NotRequired[
        "capo_sagemaker.types.available_instance_count.AvailableInstanceCount"
    ]
    """<p>The number of instances currently available for use in this reserved capacity.</p>"""
    in_use_instance_count: NotRequired[
        "capo_sagemaker.types.in_use_instance_count.InUseInstanceCount"
    ]
    """<p>The number of instances currently in use from this reserved capacity.</p>"""
    ultra_server_summary: NotRequired[
        "capo_sagemaker.types.ultra_server_summary.UltraServerSummary"
    ]
    """<p>A summary of the UltraServer associated with this reserved capacity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReservedCapacityResponse) -> dict:
    out: dict = {}
    if "reserved_capacity_arn" in value:
        out["ReservedCapacityArn"] = value["reserved_capacity_arn"]
    if "reserved_capacity_type" in value:
        import capo_sagemaker.types.reserved_capacity_type

        out["ReservedCapacityType"] = (
            capo_sagemaker.types.reserved_capacity_type.serialize_aws_json_1_1(
                value["reserved_capacity_type"]
            )
        )
    if "status" in value:
        import capo_sagemaker.types.reserved_capacity_status

        out["Status"] = (
            capo_sagemaker.types.reserved_capacity_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "duration_hours" in value:
        out["DurationHours"] = value["duration_hours"]
    if "duration_minutes" in value:
        out["DurationMinutes"] = value["duration_minutes"]
    if "start_time" in value:
        import capo_sagemaker.types.timestamp

        out["StartTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_sagemaker.types.timestamp

        out["EndTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "instance_type" in value:
        import capo_sagemaker.types.reserved_capacity_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.reserved_capacity_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "total_instance_count" in value:
        out["TotalInstanceCount"] = value["total_instance_count"]
    if "available_instance_count" in value:
        out["AvailableInstanceCount"] = value["available_instance_count"]
    if "in_use_instance_count" in value:
        out["InUseInstanceCount"] = value["in_use_instance_count"]
    if "ultra_server_summary" in value:
        import capo_sagemaker.types.ultra_server_summary

        out["UltraServerSummary"] = (
            capo_sagemaker.types.ultra_server_summary.serialize_aws_json_1_1(
                value["ultra_server_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReservedCapacityResponse:
    out: DescribeReservedCapacityResponse = {}  # type: ignore[typeddict-item]
    if "ReservedCapacityArn" in data:
        out["reserved_capacity_arn"] = data["ReservedCapacityArn"]
    if "ReservedCapacityType" in data:
        import capo_sagemaker.types.reserved_capacity_type

        out["reserved_capacity_type"] = (
            capo_sagemaker.types.reserved_capacity_type.deserialize_aws_json_1_1(
                data["ReservedCapacityType"]
            )
        )
    if "Status" in data:
        import capo_sagemaker.types.reserved_capacity_status

        out["status"] = (
            capo_sagemaker.types.reserved_capacity_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "DurationHours" in data:
        out["duration_hours"] = data["DurationHours"]
    if "DurationMinutes" in data:
        out["duration_minutes"] = data["DurationMinutes"]
    if "StartTime" in data:
        import capo_sagemaker.types.timestamp

        out["start_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_sagemaker.types.timestamp

        out["end_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "InstanceType" in data:
        import capo_sagemaker.types.reserved_capacity_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.reserved_capacity_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "TotalInstanceCount" in data:
        out["total_instance_count"] = data["TotalInstanceCount"]
    if "AvailableInstanceCount" in data:
        out["available_instance_count"] = data["AvailableInstanceCount"]
    if "InUseInstanceCount" in data:
        out["in_use_instance_count"] = data["InUseInstanceCount"]
    if "UltraServerSummary" in data:
        import capo_sagemaker.types.ultra_server_summary

        out["ultra_server_summary"] = (
            capo_sagemaker.types.ultra_server_summary.deserialize_aws_json_1_1(
                data["UltraServerSummary"]
            )
        )
    return out
