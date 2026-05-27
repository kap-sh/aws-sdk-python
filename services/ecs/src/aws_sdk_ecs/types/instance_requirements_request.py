"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceRequirementsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.accelerator_count_request
    import aws_sdk_ecs.types.accelerator_manufacturer_set
    import aws_sdk_ecs.types.accelerator_name_set
    import aws_sdk_ecs.types.accelerator_total_memory_mi_b_request
    import aws_sdk_ecs.types.accelerator_type_set
    import aws_sdk_ecs.types.allowed_instance_type_set
    import aws_sdk_ecs.types.bare_metal
    import aws_sdk_ecs.types.baseline_ebs_bandwidth_mbps_request
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.burstable_performance
    import aws_sdk_ecs.types.cpu_manufacturer_set
    import aws_sdk_ecs.types.excluded_instance_type_set
    import aws_sdk_ecs.types.instance_generation_set
    import aws_sdk_ecs.types.local_storage
    import aws_sdk_ecs.types.local_storage_type_set
    import aws_sdk_ecs.types.memory_gi_b_per_v_cpu_request
    import aws_sdk_ecs.types.memory_mi_b_request
    import aws_sdk_ecs.types.network_bandwidth_gbps_request
    import aws_sdk_ecs.types.network_interface_count_request
    import aws_sdk_ecs.types.total_local_storage_gb_request
    import aws_sdk_ecs.types.v_cpu_count_range_request


class InstanceRequirementsRequest(TypedDict):
    v_cpu_count: "aws_sdk_ecs.types.v_cpu_count_range_request.VCpuCountRangeRequest"
    """<p>The minimum and maximum number of vCPUs for the instance types. Amazon ECS selects instance types that have vCPU counts within this range.</p>"""
    memory_mi_b: "aws_sdk_ecs.types.memory_mi_b_request.MemoryMiBRequest"
    """<p>The minimum and maximum amount of memory in mebibytes (MiB) for the instance types. Amazon ECS selects instance types that have memory within this range.</p>"""
    cpu_manufacturers: NotRequired[
        "aws_sdk_ecs.types.cpu_manufacturer_set.CpuManufacturerSet"
    ]
    """<p>The CPU manufacturers to include or exclude. You can specify <code>intel</code>, <code>amd</code>, or <code>amazon-web-services</code> to control which CPU types are used for your workloads.</p>"""
    memory_gi_b_per_v_cpu: NotRequired[
        "aws_sdk_ecs.types.memory_gi_b_per_v_cpu_request.MemoryGiBPerVCpuRequest"
    ]
    """<p>The minimum and maximum amount of memory per vCPU in gibibytes (GiB). This helps ensure that instance types have the appropriate memory-to-CPU ratio for your workloads.</p>"""
    excluded_instance_types: NotRequired[
        "aws_sdk_ecs.types.excluded_instance_type_set.ExcludedInstanceTypeSet"
    ]
    """<p>The instance types to exclude from selection. Use this to prevent Amazon ECS from selecting specific instance types that may not be suitable for your workloads.</p>"""
    instance_generations: NotRequired[
        "aws_sdk_ecs.types.instance_generation_set.InstanceGenerationSet"
    ]
    """<p>The instance generations to include. You can specify <code>current</code> to use the latest generation instances, or <code>previous</code> to include previous generation instances for cost optimization.</p>"""
    spot_max_price_percentage_over_lowest_price: NotRequired[
        "aws_sdk_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The maximum price for Spot instances as a percentage over the lowest priced On-Demand instance. This helps control Spot instance costs while maintaining access to capacity.</p>"""
    on_demand_max_price_percentage_over_lowest_price: NotRequired[
        "aws_sdk_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon ECS selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.</p>"""
    bare_metal: NotRequired["aws_sdk_ecs.types.bare_metal.BareMetal"]
    """<p>Indicates whether to include bare metal instance types. Set to <code>included</code> to allow bare metal instances, <code>excluded</code> to exclude them, or <code>required</code> to use only bare metal instances.</p>"""
    burstable_performance: NotRequired[
        "aws_sdk_ecs.types.burstable_performance.BurstablePerformance"
    ]
    """<p>Indicates whether to include burstable performance instance types (T2, T3, T3a, T4g). Set to <code>included</code> to allow burstable instances, <code>excluded</code> to exclude them, or <code>required</code> to use only burstable instances.</p>"""
    require_hibernate_support: NotRequired[
        "aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Indicates whether the instance types must support hibernation. When set to <code>true</code>, only instance types that support hibernation are selected.</p>"""
    network_interface_count: NotRequired[
        "aws_sdk_ecs.types.network_interface_count_request.NetworkInterfaceCountRequest"
    ]
    """<p>The minimum and maximum number of network interfaces for the instance types. This is useful for workloads that require multiple network interfaces.</p>"""
    local_storage: NotRequired["aws_sdk_ecs.types.local_storage.LocalStorage"]
    """<p>Indicates whether to include instance types with local storage. Set to <code>included</code> to allow local storage, <code>excluded</code> to exclude it, or <code>required</code> to use only instances with local storage.</p>"""
    local_storage_types: NotRequired[
        "aws_sdk_ecs.types.local_storage_type_set.LocalStorageTypeSet"
    ]
    """<p>The local storage types to include. You can specify <code>hdd</code> for hard disk drives, <code>ssd</code> for solid state drives, or both.</p>"""
    total_local_storage_gb: NotRequired[
        "aws_sdk_ecs.types.total_local_storage_gb_request.TotalLocalStorageGBRequest"
    ]
    """<p>The minimum and maximum total local storage in gigabytes (GB) for instance types with local storage.</p>"""
    baseline_ebs_bandwidth_mbps: NotRequired[
        "aws_sdk_ecs.types.baseline_ebs_bandwidth_mbps_request.BaselineEbsBandwidthMbpsRequest"
    ]
    """<p>The minimum and maximum baseline Amazon EBS bandwidth in megabits per second (Mbps). This is important for workloads with high storage I/O requirements.</p>"""
    accelerator_types: NotRequired[
        "aws_sdk_ecs.types.accelerator_type_set.AcceleratorTypeSet"
    ]
    """<p>The accelerator types to include. You can specify <code>gpu</code> for graphics processing units, <code>fpga</code> for field programmable gate arrays, or <code>inference</code> for machine learning inference accelerators.</p>"""
    accelerator_count: NotRequired[
        "aws_sdk_ecs.types.accelerator_count_request.AcceleratorCountRequest"
    ]
    """<p>The minimum and maximum number of accelerators for the instance types. This is used when you need instances with specific numbers of GPUs or other accelerators.</p>"""
    accelerator_manufacturers: NotRequired[
        "aws_sdk_ecs.types.accelerator_manufacturer_set.AcceleratorManufacturerSet"
    ]
    """<p>The accelerator manufacturers to include. You can specify <code>nvidia</code>, <code>amd</code>, <code>amazon-web-services</code>, or <code>xilinx</code> depending on your accelerator requirements.</p>"""
    accelerator_names: NotRequired[
        "aws_sdk_ecs.types.accelerator_name_set.AcceleratorNameSet"
    ]
    """<p>The specific accelerator names to include. For example, you can specify <code>a100</code>, <code>v100</code>, <code>k80</code>, or other specific accelerator models.</p>"""
    accelerator_total_memory_mi_b: NotRequired[
        "aws_sdk_ecs.types.accelerator_total_memory_mi_b_request.AcceleratorTotalMemoryMiBRequest"
    ]
    """<p>The minimum and maximum total accelerator memory in mebibytes (MiB). This is important for GPU workloads that require specific amounts of video memory.</p>"""
    network_bandwidth_gbps: NotRequired[
        "aws_sdk_ecs.types.network_bandwidth_gbps_request.NetworkBandwidthGbpsRequest"
    ]
    """<p>The minimum and maximum network bandwidth in gigabits per second (Gbps). This is crucial for network-intensive workloads that require high throughput.</p>"""
    allowed_instance_types: NotRequired[
        "aws_sdk_ecs.types.allowed_instance_type_set.AllowedInstanceTypeSet"
    ]
    """<p>The instance types to include in the selection. When specified, Amazon ECS only considers these instance types, subject to the other requirements specified.</p>"""
    max_spot_price_as_percentage_of_optimal_on_demand_price: NotRequired[
        "aws_sdk_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The maximum price for Spot instances as a percentage of the optimal On-Demand price. This provides more precise cost control for Spot instance selection.</p>"""
