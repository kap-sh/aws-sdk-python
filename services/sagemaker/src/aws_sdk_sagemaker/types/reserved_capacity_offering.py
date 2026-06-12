"""Generated from Smithy shape ``com.amazonaws.sagemaker#ReservedCapacityOffering``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.availability_zone
    import aws_sdk_sagemaker.types.reserved_capacity_duration_hours
    import aws_sdk_sagemaker.types.reserved_capacity_duration_minutes
    import aws_sdk_sagemaker.types.reserved_capacity_instance_count
    import aws_sdk_sagemaker.types.reserved_capacity_instance_type
    import aws_sdk_sagemaker.types.reserved_capacity_type
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.ultra_server_count
    import aws_sdk_sagemaker.types.ultra_server_type


class ReservedCapacityOffering(TypedDict):
    reserved_capacity_type: NotRequired[
        "aws_sdk_sagemaker.types.reserved_capacity_type.ReservedCapacityType"
    ]
    """<p>The type of reserved capacity offering.</p>"""
    ultra_server_type: NotRequired[
        "aws_sdk_sagemaker.types.ultra_server_type.UltraServerType"
    ]
    """<p>The type of UltraServer included in this reserved capacity offering, such as ml.u-p6e-gb200x72.</p>"""
    ultra_server_count: NotRequired[
        "aws_sdk_sagemaker.types.ultra_server_count.UltraServerCount"
    ]
    """<p>The number of UltraServers included in this reserved capacity offering.</p>"""
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.reserved_capacity_instance_type.ReservedCapacityInstanceType"
    ]
    """<p>The instance type for the reserved capacity offering.</p>"""
    instance_count: NotRequired[
        "aws_sdk_sagemaker.types.reserved_capacity_instance_count.ReservedCapacityInstanceCount"
    ]
    """<p>The number of instances in the reserved capacity offering.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_sagemaker.types.availability_zone.AvailabilityZone"
    ]
    """<p>The availability zone for the reserved capacity offering.</p>"""
    duration_hours: NotRequired[
        "aws_sdk_sagemaker.types.reserved_capacity_duration_hours.ReservedCapacityDurationHours"
    ]
    """<p>The number of whole hours in the total duration for this reserved capacity offering.</p>"""
    duration_minutes: NotRequired[
        "aws_sdk_sagemaker.types.reserved_capacity_duration_minutes.ReservedCapacityDurationMinutes"
    ]
    """<p>The additional minutes beyond whole hours in the total duration for this reserved capacity offering.</p>"""
    start_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The start time of the reserved capacity offering.</p>"""
    end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The end time of the reserved capacity offering.</p>"""
    extension_start_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The start time of the extension for the reserved capacity offering.</p>"""
    extension_end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The end time of the extension for the reserved capacity offering.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservedCapacityOffering) -> dict:
    out: dict = {}
    if "reserved_capacity_type" in value:
        import aws_sdk_sagemaker.types.reserved_capacity_type

        out["ReservedCapacityType"] = (
            aws_sdk_sagemaker.types.reserved_capacity_type.serialize_aws_json_1_1(
                value["reserved_capacity_type"]
            )
        )
    if "ultra_server_type" in value:
        out["UltraServerType"] = value["ultra_server_type"]
    if "ultra_server_count" in value:
        out["UltraServerCount"] = value["ultra_server_count"]
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.reserved_capacity_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.reserved_capacity_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "duration_hours" in value:
        out["DurationHours"] = value["duration_hours"]
    if "duration_minutes" in value:
        out["DurationMinutes"] = value["duration_minutes"]
    if "start_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["StartTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["EndTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "extension_start_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["ExtensionStartTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["extension_start_time"]
            )
        )
    if "extension_end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["ExtensionEndTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["extension_end_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservedCapacityOffering:
    out: ReservedCapacityOffering = {}  # type: ignore[typeddict-item]
    if "ReservedCapacityType" in data:
        import aws_sdk_sagemaker.types.reserved_capacity_type

        out["reserved_capacity_type"] = (
            aws_sdk_sagemaker.types.reserved_capacity_type.deserialize_aws_json_1_1(
                data["ReservedCapacityType"]
            )
        )
    if "UltraServerType" in data:
        out["ultra_server_type"] = data["UltraServerType"]
    if "UltraServerCount" in data:
        out["ultra_server_count"] = data["UltraServerCount"]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.reserved_capacity_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.reserved_capacity_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "DurationHours" in data:
        out["duration_hours"] = data["DurationHours"]
    if "DurationMinutes" in data:
        out["duration_minutes"] = data["DurationMinutes"]
    if "StartTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["start_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["end_time"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "ExtensionStartTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["extension_start_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["ExtensionStartTime"]
            )
        )
    if "ExtensionEndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["extension_end_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["ExtensionEndTime"]
            )
        )
    return out
