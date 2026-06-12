"""Generated from Smithy shape ``com.amazonaws.costexplorer#EC2ResourceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class EC2ResourceDetails(TypedDict):
    hourly_on_demand_rate: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The hourly public On-Demand rate for the instance type.</p>"""
    instance_type: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The type of Amazon Web Services instance.</p>"""
    platform: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The platform of the Amazon Web Services instance. The platform is the specific combination of operating system, license model, and software on an instance.</p>"""
    region: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The Amazon Web Services Region of the instance.</p>"""
    sku: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The SKU of the product.</p>"""
    memory: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The memory capacity of the Amazon Web Services instance.</p>"""
    network_performance: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The network performance capacity of the Amazon Web Services instance.</p>"""
    storage: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The disk storage of the Amazon Web Services instance. This doesn't include EBS storage.</p>"""
    vcpu: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The number of VCPU cores in the Amazon Web Services instance type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2ResourceDetails) -> dict:
    out: dict = {}
    if "hourly_on_demand_rate" in value:
        out["HourlyOnDemandRate"] = value["hourly_on_demand_rate"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "platform" in value:
        out["Platform"] = value["platform"]
    if "region" in value:
        out["Region"] = value["region"]
    if "sku" in value:
        out["Sku"] = value["sku"]
    if "memory" in value:
        out["Memory"] = value["memory"]
    if "network_performance" in value:
        out["NetworkPerformance"] = value["network_performance"]
    if "storage" in value:
        out["Storage"] = value["storage"]
    if "vcpu" in value:
        out["Vcpu"] = value["vcpu"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2ResourceDetails:
    out: EC2ResourceDetails = {}  # type: ignore[typeddict-item]
    if "HourlyOnDemandRate" in data:
        out["hourly_on_demand_rate"] = data["HourlyOnDemandRate"]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "Platform" in data:
        out["platform"] = data["Platform"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "Sku" in data:
        out["sku"] = data["Sku"]
    if "Memory" in data:
        out["memory"] = data["Memory"]
    if "NetworkPerformance" in data:
        out["network_performance"] = data["NetworkPerformance"]
    if "Storage" in data:
        out["storage"] = data["Storage"]
    if "Vcpu" in data:
        out["vcpu"] = data["Vcpu"]
    return out
