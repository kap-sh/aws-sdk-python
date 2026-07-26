"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataInstanceRequirementsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_accelerator_count_details
    import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_accelerator_total_memory_mi_b_details
    import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_baseline_ebs_bandwidth_mbps_details
    import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_memory_gi_b_per_v_cpu_details
    import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_memory_mi_b_details
    import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_network_interface_count_details
    import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_total_local_storage_gb_details
    import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_v_cpu_count_details
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsEc2LaunchTemplateDataInstanceRequirementsDetails(TypedDict, closed=True):
    accelerator_count: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_accelerator_count_details.AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails"
    ]
    """<p> The minimum and maximum number of accelerators (GPUs, FPGAs, or Amazon Web Services Inferentia chips) on an instance. </p>"""
    accelerator_manufacturers: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>Indicates whether instance types must have accelerators by specific manufacturers. </p>"""
    accelerator_names: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> The accelerators that must be on the instance type. </p>"""
    accelerator_total_memory_mi_b: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_accelerator_total_memory_mi_b_details.AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails"
    ]
    """<p> The minimum and maximum amount of total accelerator memory, in MiB. </p>"""
    accelerator_types: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The accelerator types that must be on the instance type. </p>"""
    bare_metal: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates whether bare metal instance types must be included, excluded, or required. </p>"""
    baseline_ebs_bandwidth_mbps: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_baseline_ebs_bandwidth_mbps_details.AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails"
    ]
    r"""<p> The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html\">Amazon EBS optimized instances</a> in the <i>Amazon EC2 User Guide</i>. </p>"""
    burstable_performance: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p> Indicates whether burstable performance T instance types are included, excluded, or required. For more information, <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html\">Burstable performance instances</a> in the <i>Amazon EC2 User Guide</i>. </p>"""
    cpu_manufacturers: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> The CPU manufacturers to include. </p>"""
    excluded_instance_types: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> The instance types to exclude. </p>"""
    instance_generations: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> Indicates whether current or previous generation instance types are included. </p>"""
    local_storage: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    r"""<p> Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html\">Amazon EC2 instance store</a> in the <i>Amazon EC2 User Guide</i>. </p>"""
    local_storage_types: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p> The type of local storage that is required. </p>"""
    memory_gi_b_per_v_cpu: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_memory_gi_b_per_v_cpu_details.AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails"
    ]
    """<p> The minimum and maximum amount of memory per vCPU, in GiB. </p>"""
    memory_mi_b: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_memory_mi_b_details.AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails"
    ]
    """<p> The minimum and maximum amount of memory, in MiB. </p>"""
    network_interface_count: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_network_interface_count_details.AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails"
    ]
    """<p> The minimum and maximum number of network interfaces. </p>"""
    on_demand_max_price_percentage_over_lowest_price: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p> The price protection threshold for On-Demand Instances. This is the maximum you'll pay for an On-Demand Instance, expressed as a percentage above the least expensive current generation M, C, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it excludes instance types priced above your threshold.</p> <p>The parameter accepts an integer, which Amazon EC2 interprets as a percentage.</p> <p>A high value, such as <code>999999</code>, turns off price protection.</p>"""
    require_hibernate_support: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether instance types must support hibernation for On-Demand Instances. </p>"""
    spot_max_price_percentage_over_lowest_price: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p> The price protection threshold for Spot Instances. This is the maximum you'll pay for a Spot Instance, expressed as a percentage above the least expensive current generation M, C, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it excludes instance types priced above your threshold. </p> <p>The parameter accepts an integer, which Amazon EC2 interprets as a percentage.</p> <p>A high value, such as <code>999999</code>, turns off price protection.</p>"""
    total_local_storage_gb: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_total_local_storage_gb_details.AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails"
    ]
    """<p> The minimum and maximum amount of total local storage, in GB. </p>"""
    v_cpu_count: NotRequired[
        "capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_v_cpu_count_details.AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails"
    ]
    """<p> The minimum and maximum number of vCPUs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataInstanceRequirementsDetails) -> dict:
    out: dict = {}
    if "accelerator_count" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_accelerator_count_details

        out["AcceleratorCount"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_accelerator_count_details.serialize_json(
                value["accelerator_count"]
            )
        )
    if "accelerator_manufacturers" in value:
        import capo_securityhub.types.non_empty_string_list

        out["AcceleratorManufacturers"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["accelerator_manufacturers"]
            )
        )
    if "accelerator_names" in value:
        import capo_securityhub.types.non_empty_string_list

        out["AcceleratorNames"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["accelerator_names"]
            )
        )
    if "accelerator_total_memory_mi_b" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_accelerator_total_memory_mi_b_details

        out["AcceleratorTotalMemoryMiB"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_accelerator_total_memory_mi_b_details.serialize_json(
                value["accelerator_total_memory_mi_b"]
            )
        )
    if "accelerator_types" in value:
        import capo_securityhub.types.non_empty_string_list

        out["AcceleratorTypes"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["accelerator_types"]
            )
        )
    if "bare_metal" in value:
        out["BareMetal"] = value["bare_metal"]
    if "baseline_ebs_bandwidth_mbps" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_baseline_ebs_bandwidth_mbps_details

        out["BaselineEbsBandwidthMbps"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_baseline_ebs_bandwidth_mbps_details.serialize_json(
                value["baseline_ebs_bandwidth_mbps"]
            )
        )
    if "burstable_performance" in value:
        out["BurstablePerformance"] = value["burstable_performance"]
    if "cpu_manufacturers" in value:
        import capo_securityhub.types.non_empty_string_list

        out["CpuManufacturers"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["cpu_manufacturers"]
            )
        )
    if "excluded_instance_types" in value:
        import capo_securityhub.types.non_empty_string_list

        out["ExcludedInstanceTypes"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["excluded_instance_types"]
            )
        )
    if "instance_generations" in value:
        import capo_securityhub.types.non_empty_string_list

        out["InstanceGenerations"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["instance_generations"]
            )
        )
    if "local_storage" in value:
        out["LocalStorage"] = value["local_storage"]
    if "local_storage_types" in value:
        import capo_securityhub.types.non_empty_string_list

        out["LocalStorageTypes"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["local_storage_types"]
            )
        )
    if "memory_gi_b_per_v_cpu" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_memory_gi_b_per_v_cpu_details

        out["MemoryGiBPerVCpu"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_memory_gi_b_per_v_cpu_details.serialize_json(
                value["memory_gi_b_per_v_cpu"]
            )
        )
    if "memory_mi_b" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_memory_mi_b_details

        out["MemoryMiB"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_memory_mi_b_details.serialize_json(
                value["memory_mi_b"]
            )
        )
    if "network_interface_count" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_network_interface_count_details

        out["NetworkInterfaceCount"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_network_interface_count_details.serialize_json(
                value["network_interface_count"]
            )
        )
    if "on_demand_max_price_percentage_over_lowest_price" in value:
        out["OnDemandMaxPricePercentageOverLowestPrice"] = value[
            "on_demand_max_price_percentage_over_lowest_price"
        ]
    if "require_hibernate_support" in value:
        out["RequireHibernateSupport"] = value["require_hibernate_support"]
    if "spot_max_price_percentage_over_lowest_price" in value:
        out["SpotMaxPricePercentageOverLowestPrice"] = value[
            "spot_max_price_percentage_over_lowest_price"
        ]
    if "total_local_storage_gb" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_total_local_storage_gb_details

        out["TotalLocalStorageGB"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_total_local_storage_gb_details.serialize_json(
                value["total_local_storage_gb"]
            )
        )
    if "v_cpu_count" in value:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_v_cpu_count_details

        out["VCpuCount"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_v_cpu_count_details.serialize_json(
                value["v_cpu_count"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEc2LaunchTemplateDataInstanceRequirementsDetails:
    out: AwsEc2LaunchTemplateDataInstanceRequirementsDetails = {}  # type: ignore[typeddict-item]
    if "AcceleratorCount" in data:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_accelerator_count_details

        out["accelerator_count"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_accelerator_count_details.deserialize_json(
                data["AcceleratorCount"]
            )
        )
    if "AcceleratorManufacturers" in data:
        import capo_securityhub.types.non_empty_string_list

        out["accelerator_manufacturers"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["AcceleratorManufacturers"]
            )
        )
    if "AcceleratorNames" in data:
        import capo_securityhub.types.non_empty_string_list

        out["accelerator_names"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["AcceleratorNames"]
            )
        )
    if "AcceleratorTotalMemoryMiB" in data:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_accelerator_total_memory_mi_b_details

        out["accelerator_total_memory_mi_b"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_accelerator_total_memory_mi_b_details.deserialize_json(
                data["AcceleratorTotalMemoryMiB"]
            )
        )
    if "AcceleratorTypes" in data:
        import capo_securityhub.types.non_empty_string_list

        out["accelerator_types"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["AcceleratorTypes"]
            )
        )
    if "BareMetal" in data:
        out["bare_metal"] = data["BareMetal"]
    if "BaselineEbsBandwidthMbps" in data:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_baseline_ebs_bandwidth_mbps_details

        out["baseline_ebs_bandwidth_mbps"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_baseline_ebs_bandwidth_mbps_details.deserialize_json(
                data["BaselineEbsBandwidthMbps"]
            )
        )
    if "BurstablePerformance" in data:
        out["burstable_performance"] = data["BurstablePerformance"]
    if "CpuManufacturers" in data:
        import capo_securityhub.types.non_empty_string_list

        out["cpu_manufacturers"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["CpuManufacturers"]
            )
        )
    if "ExcludedInstanceTypes" in data:
        import capo_securityhub.types.non_empty_string_list

        out["excluded_instance_types"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["ExcludedInstanceTypes"]
            )
        )
    if "InstanceGenerations" in data:
        import capo_securityhub.types.non_empty_string_list

        out["instance_generations"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["InstanceGenerations"]
            )
        )
    if "LocalStorage" in data:
        out["local_storage"] = data["LocalStorage"]
    if "LocalStorageTypes" in data:
        import capo_securityhub.types.non_empty_string_list

        out["local_storage_types"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["LocalStorageTypes"]
            )
        )
    if "MemoryGiBPerVCpu" in data:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_memory_gi_b_per_v_cpu_details

        out["memory_gi_b_per_v_cpu"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_memory_gi_b_per_v_cpu_details.deserialize_json(
                data["MemoryGiBPerVCpu"]
            )
        )
    if "MemoryMiB" in data:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_memory_mi_b_details

        out["memory_mi_b"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_memory_mi_b_details.deserialize_json(
                data["MemoryMiB"]
            )
        )
    if "NetworkInterfaceCount" in data:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_network_interface_count_details

        out["network_interface_count"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_network_interface_count_details.deserialize_json(
                data["NetworkInterfaceCount"]
            )
        )
    if "OnDemandMaxPricePercentageOverLowestPrice" in data:
        out["on_demand_max_price_percentage_over_lowest_price"] = data[
            "OnDemandMaxPricePercentageOverLowestPrice"
        ]
    if "RequireHibernateSupport" in data:
        out["require_hibernate_support"] = data["RequireHibernateSupport"]
    if "SpotMaxPricePercentageOverLowestPrice" in data:
        out["spot_max_price_percentage_over_lowest_price"] = data[
            "SpotMaxPricePercentageOverLowestPrice"
        ]
    if "TotalLocalStorageGB" in data:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_total_local_storage_gb_details

        out["total_local_storage_gb"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_total_local_storage_gb_details.deserialize_json(
                data["TotalLocalStorageGB"]
            )
        )
    if "VCpuCount" in data:
        import capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_v_cpu_count_details

        out["v_cpu_count"] = (
            capo_securityhub.types.aws_ec2_launch_template_data_instance_requirements_v_cpu_count_details.deserialize_json(
                data["VCpuCount"]
            )
        )
    return out
