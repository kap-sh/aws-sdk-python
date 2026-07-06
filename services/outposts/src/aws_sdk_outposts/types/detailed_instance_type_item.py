"""Generated from Smithy shape ``com.amazonaws.outposts#DetailedInstanceTypeItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.form_factor_config_list
    import aws_sdk_outposts.types.instance_type
    import aws_sdk_outposts.types.memory_in_mib
    import aws_sdk_outposts.types.network_performance
    import aws_sdk_outposts.types.vcpu_count


class DetailedInstanceTypeItem(TypedDict, closed=True):
    instance_type: NotRequired["aws_sdk_outposts.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    vcp_us: NotRequired["aws_sdk_outposts.types.vcpu_count.VCPUCount"]
    """<p>The number of default VCPUs in the instance type.</p>"""
    memory_in_mib: "aws_sdk_outposts.types.memory_in_mib.MemoryInMib"
    """<p>The memory size of the instance type, in MiB.</p>"""
    network_performance: NotRequired[
        "aws_sdk_outposts.types.network_performance.NetworkPerformance"
    ]
    """<p>The network performance of the instance type.</p>"""
    form_factor_configs: NotRequired[
        "aws_sdk_outposts.types.form_factor_config_list.FormFactorConfigList"
    ]
    """<p>The supported form factor and Outpost generation configurations for the instance type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetailedInstanceTypeItem) -> dict:
    out: dict = {}
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "vcp_us" in value:
        out["VCPUs"] = value["vcp_us"]
    out["MemoryInMib"] = value.get("memory_in_mib", 0)
    if "network_performance" in value:
        out["NetworkPerformance"] = value["network_performance"]
    if "form_factor_configs" in value:
        import aws_sdk_outposts.types.form_factor_config_list

        out["FormFactorConfigs"] = (
            aws_sdk_outposts.types.form_factor_config_list.serialize_json(
                value["form_factor_configs"]
            )
        )
    return out


def deserialize_json(data: dict) -> DetailedInstanceTypeItem:
    out: DetailedInstanceTypeItem = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "VCPUs" in data:
        out["vcp_us"] = data["VCPUs"]
    if "MemoryInMib" in data:
        out["memory_in_mib"] = data["MemoryInMib"]
    else:
        out["memory_in_mib"] = 0
    if "NetworkPerformance" in data:
        out["network_performance"] = data["NetworkPerformance"]
    if "FormFactorConfigs" in data:
        import aws_sdk_outposts.types.form_factor_config_list

        out["form_factor_configs"] = (
            aws_sdk_outposts.types.form_factor_config_list.deserialize_json(
                data["FormFactorConfigs"]
            )
        )
    return out
