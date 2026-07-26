"""Generated from Smithy shape ``com.amazonaws.sagemaker#UltraServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.availability_zone
    import capo_sagemaker.types.available_instance_count
    import capo_sagemaker.types.available_spare_instance_count
    import capo_sagemaker.types.configured_spare_instance_count
    import capo_sagemaker.types.in_use_instance_count
    import capo_sagemaker.types.non_empty_string256
    import capo_sagemaker.types.reserved_capacity_instance_type
    import capo_sagemaker.types.total_instance_count
    import capo_sagemaker.types.ultra_server_health_status
    import capo_sagemaker.types.ultra_server_type
    import capo_sagemaker.types.unhealthy_instance_count


class UltraServer(TypedDict, closed=True):
    ultra_server_id: NotRequired[
        "capo_sagemaker.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The unique identifier for the UltraServer.</p>"""
    ultra_server_type: NotRequired[
        "capo_sagemaker.types.ultra_server_type.UltraServerType"
    ]
    """<p>The type of UltraServer, such as ml.u-p6e-gb200x72.</p>"""
    availability_zone: NotRequired[
        "capo_sagemaker.types.availability_zone.AvailabilityZone"
    ]
    """<p>The name of the Availability Zone where the UltraServer is provisioned.</p>"""
    instance_type: NotRequired[
        "capo_sagemaker.types.reserved_capacity_instance_type.ReservedCapacityInstanceType"
    ]
    """<p>The Amazon EC2 instance type used in the UltraServer.</p>"""
    total_instance_count: NotRequired[
        "capo_sagemaker.types.total_instance_count.TotalInstanceCount"
    ]
    """<p>The total number of instances in this UltraServer.</p>"""
    configured_spare_instance_count: NotRequired[
        "capo_sagemaker.types.configured_spare_instance_count.ConfiguredSpareInstanceCount"
    ]
    """<p>The number of spare instances configured for this UltraServer to provide enhanced resiliency.</p>"""
    available_instance_count: NotRequired[
        "capo_sagemaker.types.available_instance_count.AvailableInstanceCount"
    ]
    """<p>The number of instances currently available for use in this UltraServer.</p>"""
    in_use_instance_count: NotRequired[
        "capo_sagemaker.types.in_use_instance_count.InUseInstanceCount"
    ]
    """<p>The number of instances currently in use in this UltraServer.</p>"""
    available_spare_instance_count: NotRequired[
        "capo_sagemaker.types.available_spare_instance_count.AvailableSpareInstanceCount"
    ]
    """<p>The number of available spare instances in the UltraServer.</p>"""
    unhealthy_instance_count: NotRequired[
        "capo_sagemaker.types.unhealthy_instance_count.UnhealthyInstanceCount"
    ]
    """<p>The number of instances in this UltraServer that are currently in an unhealthy state.</p>"""
    health_status: NotRequired[
        "capo_sagemaker.types.ultra_server_health_status.UltraServerHealthStatus"
    ]
    """<p>The overall health status of the UltraServer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UltraServer) -> dict:
    out: dict = {}
    if "ultra_server_id" in value:
        out["UltraServerId"] = value["ultra_server_id"]
    if "ultra_server_type" in value:
        out["UltraServerType"] = value["ultra_server_type"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "instance_type" in value:
        import capo_sagemaker.types.reserved_capacity_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.reserved_capacity_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "total_instance_count" in value:
        out["TotalInstanceCount"] = value["total_instance_count"]
    if "configured_spare_instance_count" in value:
        out["ConfiguredSpareInstanceCount"] = value["configured_spare_instance_count"]
    if "available_instance_count" in value:
        out["AvailableInstanceCount"] = value["available_instance_count"]
    if "in_use_instance_count" in value:
        out["InUseInstanceCount"] = value["in_use_instance_count"]
    if "available_spare_instance_count" in value:
        out["AvailableSpareInstanceCount"] = value["available_spare_instance_count"]
    if "unhealthy_instance_count" in value:
        out["UnhealthyInstanceCount"] = value["unhealthy_instance_count"]
    if "health_status" in value:
        import capo_sagemaker.types.ultra_server_health_status

        out["HealthStatus"] = (
            capo_sagemaker.types.ultra_server_health_status.serialize_aws_json_1_1(
                value["health_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UltraServer:
    out: UltraServer = {}  # type: ignore[typeddict-item]
    if "UltraServerId" in data:
        out["ultra_server_id"] = data["UltraServerId"]
    if "UltraServerType" in data:
        out["ultra_server_type"] = data["UltraServerType"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "InstanceType" in data:
        import capo_sagemaker.types.reserved_capacity_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.reserved_capacity_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "TotalInstanceCount" in data:
        out["total_instance_count"] = data["TotalInstanceCount"]
    if "ConfiguredSpareInstanceCount" in data:
        out["configured_spare_instance_count"] = data["ConfiguredSpareInstanceCount"]
    if "AvailableInstanceCount" in data:
        out["available_instance_count"] = data["AvailableInstanceCount"]
    if "InUseInstanceCount" in data:
        out["in_use_instance_count"] = data["InUseInstanceCount"]
    if "AvailableSpareInstanceCount" in data:
        out["available_spare_instance_count"] = data["AvailableSpareInstanceCount"]
    if "UnhealthyInstanceCount" in data:
        out["unhealthy_instance_count"] = data["UnhealthyInstanceCount"]
    if "HealthStatus" in data:
        import capo_sagemaker.types.ultra_server_health_status

        out["health_status"] = (
            capo_sagemaker.types.ultra_server_health_status.deserialize_aws_json_1_1(
                data["HealthStatus"]
            )
        )
    return out
