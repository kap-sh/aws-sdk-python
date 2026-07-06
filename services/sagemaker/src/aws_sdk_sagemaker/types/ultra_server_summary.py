"""Generated from Smithy shape ``com.amazonaws.sagemaker#UltraServerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.available_spare_instance_count
    import aws_sdk_sagemaker.types.reserved_capacity_instance_type
    import aws_sdk_sagemaker.types.ultra_server_count
    import aws_sdk_sagemaker.types.ultra_server_type
    import aws_sdk_sagemaker.types.unhealthy_instance_count


class UltraServerSummary(TypedDict, closed=True):
    ultra_server_type: NotRequired[
        "aws_sdk_sagemaker.types.ultra_server_type.UltraServerType"
    ]
    """<p>The type of UltraServer, such as ml.u-p6e-gb200x72.</p>"""
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.reserved_capacity_instance_type.ReservedCapacityInstanceType"
    ]
    """<p>The Amazon EC2 instance type used in the UltraServer.</p>"""
    ultra_server_count: NotRequired[
        "aws_sdk_sagemaker.types.ultra_server_count.UltraServerCount"
    ]
    """<p>The number of UltraServers of this type.</p>"""
    available_spare_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.available_spare_instance_count.AvailableSpareInstanceCount"
    ]
    """<p>The number of available spare instances in the UltraServers.</p>"""
    unhealthy_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.unhealthy_instance_count.UnhealthyInstanceCount"
    ]
    """<p>The total number of instances across all UltraServers of this type that are currently in an unhealthy state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UltraServerSummary) -> dict:
    out: dict = {}
    if "ultra_server_type" in value:
        out["UltraServerType"] = value["ultra_server_type"]
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.reserved_capacity_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.reserved_capacity_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "ultra_server_count" in value:
        out["UltraServerCount"] = value["ultra_server_count"]
    if "available_spare_instance_count" in value:
        out["AvailableSpareInstanceCount"] = value["available_spare_instance_count"]
    if "unhealthy_instance_count" in value:
        out["UnhealthyInstanceCount"] = value["unhealthy_instance_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UltraServerSummary:
    out: UltraServerSummary = {}  # type: ignore[typeddict-item]
    if "UltraServerType" in data:
        out["ultra_server_type"] = data["UltraServerType"]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.reserved_capacity_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.reserved_capacity_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "UltraServerCount" in data:
        out["ultra_server_count"] = data["UltraServerCount"]
    if "AvailableSpareInstanceCount" in data:
        out["available_spare_instance_count"] = data["AvailableSpareInstanceCount"]
    if "UnhealthyInstanceCount" in data:
        out["unhealthy_instance_count"] = data["UnhealthyInstanceCount"]
    return out
