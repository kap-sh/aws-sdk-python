"""Generated from Smithy shape ``com.amazonaws.costexplorer#EC2ResourceUtilization``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.disk_resource_utilization
    import aws_sdk_cost_explorer.types.ebs_resource_utilization
    import aws_sdk_cost_explorer.types.generic_string
    import aws_sdk_cost_explorer.types.network_resource_utilization


class EC2ResourceUtilization(TypedDict):
    max_cpu_utilization_percentage: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum observed or expected CPU utilization of the instance.</p>"""
    max_memory_utilization_percentage: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum observed or expected memory utilization of the instance.</p>"""
    max_storage_utilization_percentage: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The maximum observed or expected storage utilization of the instance. This doesn't include EBS storage.</p>"""
    ebs_resource_utilization: NotRequired[
        "aws_sdk_cost_explorer.types.ebs_resource_utilization.EBSResourceUtilization"
    ]
    """<p>The EBS field that contains a list of EBS metrics that are associated with the current instance. </p>"""
    disk_resource_utilization: NotRequired[
        "aws_sdk_cost_explorer.types.disk_resource_utilization.DiskResourceUtilization"
    ]
    """<p>The field that contains a list of disk (local storage) metrics that are associated with the current instance. </p>"""
    network_resource_utilization: NotRequired[
        "aws_sdk_cost_explorer.types.network_resource_utilization.NetworkResourceUtilization"
    ]
    """<p>The network field that contains a list of network metrics that are associated with the current instance. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2ResourceUtilization) -> dict:
    out: dict = {}
    if "max_cpu_utilization_percentage" in value:
        out["MaxCpuUtilizationPercentage"] = value["max_cpu_utilization_percentage"]
    if "max_memory_utilization_percentage" in value:
        out["MaxMemoryUtilizationPercentage"] = value[
            "max_memory_utilization_percentage"
        ]
    if "max_storage_utilization_percentage" in value:
        out["MaxStorageUtilizationPercentage"] = value[
            "max_storage_utilization_percentage"
        ]
    if "ebs_resource_utilization" in value:
        import aws_sdk_cost_explorer.types.ebs_resource_utilization

        out["EBSResourceUtilization"] = (
            aws_sdk_cost_explorer.types.ebs_resource_utilization.serialize_aws_json_1_1(
                value["ebs_resource_utilization"]
            )
        )
    if "disk_resource_utilization" in value:
        import aws_sdk_cost_explorer.types.disk_resource_utilization

        out["DiskResourceUtilization"] = (
            aws_sdk_cost_explorer.types.disk_resource_utilization.serialize_aws_json_1_1(
                value["disk_resource_utilization"]
            )
        )
    if "network_resource_utilization" in value:
        import aws_sdk_cost_explorer.types.network_resource_utilization

        out["NetworkResourceUtilization"] = (
            aws_sdk_cost_explorer.types.network_resource_utilization.serialize_aws_json_1_1(
                value["network_resource_utilization"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2ResourceUtilization:
    out: EC2ResourceUtilization = {}  # type: ignore[typeddict-item]
    if "MaxCpuUtilizationPercentage" in data:
        out["max_cpu_utilization_percentage"] = data["MaxCpuUtilizationPercentage"]
    if "MaxMemoryUtilizationPercentage" in data:
        out["max_memory_utilization_percentage"] = data[
            "MaxMemoryUtilizationPercentage"
        ]
    if "MaxStorageUtilizationPercentage" in data:
        out["max_storage_utilization_percentage"] = data[
            "MaxStorageUtilizationPercentage"
        ]
    if "EBSResourceUtilization" in data:
        import aws_sdk_cost_explorer.types.ebs_resource_utilization

        out["ebs_resource_utilization"] = (
            aws_sdk_cost_explorer.types.ebs_resource_utilization.deserialize_aws_json_1_1(
                data["EBSResourceUtilization"]
            )
        )
    if "DiskResourceUtilization" in data:
        import aws_sdk_cost_explorer.types.disk_resource_utilization

        out["disk_resource_utilization"] = (
            aws_sdk_cost_explorer.types.disk_resource_utilization.deserialize_aws_json_1_1(
                data["DiskResourceUtilization"]
            )
        )
    if "NetworkResourceUtilization" in data:
        import aws_sdk_cost_explorer.types.network_resource_utilization

        out["network_resource_utilization"] = (
            aws_sdk_cost_explorer.types.network_resource_utilization.deserialize_aws_json_1_1(
                data["NetworkResourceUtilization"]
            )
        )
    return out
