"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceRequirementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.accelerator_count_request
    import capo_ecs.types.accelerator_manufacturer_set
    import capo_ecs.types.accelerator_name_set
    import capo_ecs.types.accelerator_total_memory_mi_b_request
    import capo_ecs.types.accelerator_type_set
    import capo_ecs.types.allowed_instance_type_set
    import capo_ecs.types.bare_metal
    import capo_ecs.types.baseline_ebs_bandwidth_mbps_request
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.burstable_performance
    import capo_ecs.types.cpu_manufacturer_set
    import capo_ecs.types.excluded_instance_type_set
    import capo_ecs.types.instance_generation_set
    import capo_ecs.types.local_storage
    import capo_ecs.types.local_storage_type_set
    import capo_ecs.types.memory_gi_b_per_v_cpu_request
    import capo_ecs.types.memory_mi_b_request
    import capo_ecs.types.network_bandwidth_gbps_request
    import capo_ecs.types.network_interface_count_request
    import capo_ecs.types.total_local_storage_gb_request
    import capo_ecs.types.v_cpu_count_range_request


class InstanceRequirementsRequest(TypedDict, closed=True):
    v_cpu_count: "capo_ecs.types.v_cpu_count_range_request.VCpuCountRangeRequest"
    """<p>The minimum and maximum number of vCPUs for the instance types. Amazon ECS selects instance types that have vCPU counts within this range.</p>"""
    memory_mi_b: "capo_ecs.types.memory_mi_b_request.MemoryMiBRequest"
    """<p>The minimum and maximum amount of memory in mebibytes (MiB) for the instance types. Amazon ECS selects instance types that have memory within this range.</p>"""
    cpu_manufacturers: NotRequired[
        "capo_ecs.types.cpu_manufacturer_set.CpuManufacturerSet"
    ]
    """<p>The CPU manufacturers to include or exclude. You can specify <code>intel</code>, <code>amd</code>, or <code>amazon-web-services</code> to control which CPU types are used for your workloads.</p>"""
    memory_gi_b_per_v_cpu: NotRequired[
        "capo_ecs.types.memory_gi_b_per_v_cpu_request.MemoryGiBPerVCpuRequest"
    ]
    """<p>The minimum and maximum amount of memory per vCPU in gibibytes (GiB). This helps ensure that instance types have the appropriate memory-to-CPU ratio for your workloads.</p>"""
    excluded_instance_types: NotRequired[
        "capo_ecs.types.excluded_instance_type_set.ExcludedInstanceTypeSet"
    ]
    """<p>The instance types to exclude from selection. Use this to prevent Amazon ECS from selecting specific instance types that may not be suitable for your workloads.</p>"""
    instance_generations: NotRequired[
        "capo_ecs.types.instance_generation_set.InstanceGenerationSet"
    ]
    """<p>The instance generations to include. You can specify <code>current</code> to use the latest generation instances, or <code>previous</code> to include previous generation instances for cost optimization.</p>"""
    spot_max_price_percentage_over_lowest_price: NotRequired[
        "capo_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The maximum price for Spot instances as a percentage over the lowest priced On-Demand instance. This helps control Spot instance costs while maintaining access to capacity.</p>"""
    on_demand_max_price_percentage_over_lowest_price: NotRequired[
        "capo_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon ECS selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.</p>"""
    bare_metal: NotRequired["capo_ecs.types.bare_metal.BareMetal"]
    """<p>Indicates whether to include bare metal instance types. Set to <code>included</code> to allow bare metal instances, <code>excluded</code> to exclude them, or <code>required</code> to use only bare metal instances.</p>"""
    burstable_performance: NotRequired[
        "capo_ecs.types.burstable_performance.BurstablePerformance"
    ]
    """<p>Indicates whether to include burstable performance instance types (T2, T3, T3a, T4g). Set to <code>included</code> to allow burstable instances, <code>excluded</code> to exclude them, or <code>required</code> to use only burstable instances.</p>"""
    require_hibernate_support: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether the instance types must support hibernation. When set to <code>true</code>, only instance types that support hibernation are selected.</p>"""
    network_interface_count: NotRequired[
        "capo_ecs.types.network_interface_count_request.NetworkInterfaceCountRequest"
    ]
    """<p>The minimum and maximum number of network interfaces for the instance types. This is useful for workloads that require multiple network interfaces.</p>"""
    local_storage: NotRequired["capo_ecs.types.local_storage.LocalStorage"]
    """<p>Indicates whether to include instance types with local storage. Set to <code>included</code> to allow local storage, <code>excluded</code> to exclude it, or <code>required</code> to use only instances with local storage.</p>"""
    local_storage_types: NotRequired[
        "capo_ecs.types.local_storage_type_set.LocalStorageTypeSet"
    ]
    """<p>The local storage types to include. You can specify <code>hdd</code> for hard disk drives, <code>ssd</code> for solid state drives, or both.</p>"""
    total_local_storage_gb: NotRequired[
        "capo_ecs.types.total_local_storage_gb_request.TotalLocalStorageGBRequest"
    ]
    """<p>The minimum and maximum total local storage in gigabytes (GB) for instance types with local storage.</p>"""
    baseline_ebs_bandwidth_mbps: NotRequired[
        "capo_ecs.types.baseline_ebs_bandwidth_mbps_request.BaselineEbsBandwidthMbpsRequest"
    ]
    """<p>The minimum and maximum baseline Amazon EBS bandwidth in megabits per second (Mbps). This is important for workloads with high storage I/O requirements.</p>"""
    accelerator_types: NotRequired[
        "capo_ecs.types.accelerator_type_set.AcceleratorTypeSet"
    ]
    """<p>The accelerator types to include. You can specify <code>gpu</code> for graphics processing units, <code>fpga</code> for field programmable gate arrays, or <code>inference</code> for machine learning inference accelerators.</p>"""
    accelerator_count: NotRequired[
        "capo_ecs.types.accelerator_count_request.AcceleratorCountRequest"
    ]
    """<p>The minimum and maximum number of accelerators for the instance types. This is used when you need instances with specific numbers of GPUs or other accelerators.</p>"""
    accelerator_manufacturers: NotRequired[
        "capo_ecs.types.accelerator_manufacturer_set.AcceleratorManufacturerSet"
    ]
    """<p>The accelerator manufacturers to include. You can specify <code>nvidia</code>, <code>amd</code>, <code>amazon-web-services</code>, or <code>xilinx</code> depending on your accelerator requirements.</p>"""
    accelerator_names: NotRequired[
        "capo_ecs.types.accelerator_name_set.AcceleratorNameSet"
    ]
    """<p>The specific accelerator names to include. For example, you can specify <code>a100</code>, <code>v100</code>, <code>k80</code>, or other specific accelerator models.</p>"""
    accelerator_total_memory_mi_b: NotRequired[
        "capo_ecs.types.accelerator_total_memory_mi_b_request.AcceleratorTotalMemoryMiBRequest"
    ]
    """<p>The minimum and maximum total accelerator memory in mebibytes (MiB). This is important for GPU workloads that require specific amounts of video memory.</p>"""
    network_bandwidth_gbps: NotRequired[
        "capo_ecs.types.network_bandwidth_gbps_request.NetworkBandwidthGbpsRequest"
    ]
    """<p>The minimum and maximum network bandwidth in gigabits per second (Gbps). This is crucial for network-intensive workloads that require high throughput.</p>"""
    allowed_instance_types: NotRequired[
        "capo_ecs.types.allowed_instance_type_set.AllowedInstanceTypeSet"
    ]
    """<p>The instance types to include in the selection. When specified, Amazon ECS only considers these instance types, subject to the other requirements specified.</p>"""
    max_spot_price_as_percentage_of_optimal_on_demand_price: NotRequired[
        "capo_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The maximum price for Spot instances as a percentage of the optimal On-Demand price. This provides more precise cost control for Spot instance selection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceRequirementsRequest) -> dict:
    out: dict = {}
    import capo_ecs.types.v_cpu_count_range_request

    out["vCpuCount"] = capo_ecs.types.v_cpu_count_range_request.serialize_aws_json_1_1(
        value["v_cpu_count"]
    )
    import capo_ecs.types.memory_mi_b_request

    out["memoryMiB"] = capo_ecs.types.memory_mi_b_request.serialize_aws_json_1_1(
        value["memory_mi_b"]
    )
    if "cpu_manufacturers" in value:
        import capo_ecs.types.cpu_manufacturer_set

        out["cpuManufacturers"] = (
            capo_ecs.types.cpu_manufacturer_set.serialize_aws_json_1_1(
                value["cpu_manufacturers"]
            )
        )
    if "memory_gi_b_per_v_cpu" in value:
        import capo_ecs.types.memory_gi_b_per_v_cpu_request

        out["memoryGiBPerVCpu"] = (
            capo_ecs.types.memory_gi_b_per_v_cpu_request.serialize_aws_json_1_1(
                value["memory_gi_b_per_v_cpu"]
            )
        )
    if "excluded_instance_types" in value:
        import capo_ecs.types.excluded_instance_type_set

        out["excludedInstanceTypes"] = (
            capo_ecs.types.excluded_instance_type_set.serialize_aws_json_1_1(
                value["excluded_instance_types"]
            )
        )
    if "instance_generations" in value:
        import capo_ecs.types.instance_generation_set

        out["instanceGenerations"] = (
            capo_ecs.types.instance_generation_set.serialize_aws_json_1_1(
                value["instance_generations"]
            )
        )
    if "spot_max_price_percentage_over_lowest_price" in value:
        out["spotMaxPricePercentageOverLowestPrice"] = value[
            "spot_max_price_percentage_over_lowest_price"
        ]
    if "on_demand_max_price_percentage_over_lowest_price" in value:
        out["onDemandMaxPricePercentageOverLowestPrice"] = value[
            "on_demand_max_price_percentage_over_lowest_price"
        ]
    if "bare_metal" in value:
        import capo_ecs.types.bare_metal

        out["bareMetal"] = capo_ecs.types.bare_metal.serialize_aws_json_1_1(
            value["bare_metal"]
        )
    if "burstable_performance" in value:
        import capo_ecs.types.burstable_performance

        out["burstablePerformance"] = (
            capo_ecs.types.burstable_performance.serialize_aws_json_1_1(
                value["burstable_performance"]
            )
        )
    if "require_hibernate_support" in value:
        out["requireHibernateSupport"] = value["require_hibernate_support"]
    if "network_interface_count" in value:
        import capo_ecs.types.network_interface_count_request

        out["networkInterfaceCount"] = (
            capo_ecs.types.network_interface_count_request.serialize_aws_json_1_1(
                value["network_interface_count"]
            )
        )
    if "local_storage" in value:
        import capo_ecs.types.local_storage

        out["localStorage"] = capo_ecs.types.local_storage.serialize_aws_json_1_1(
            value["local_storage"]
        )
    if "local_storage_types" in value:
        import capo_ecs.types.local_storage_type_set

        out["localStorageTypes"] = (
            capo_ecs.types.local_storage_type_set.serialize_aws_json_1_1(
                value["local_storage_types"]
            )
        )
    if "total_local_storage_gb" in value:
        import capo_ecs.types.total_local_storage_gb_request

        out["totalLocalStorageGB"] = (
            capo_ecs.types.total_local_storage_gb_request.serialize_aws_json_1_1(
                value["total_local_storage_gb"]
            )
        )
    if "baseline_ebs_bandwidth_mbps" in value:
        import capo_ecs.types.baseline_ebs_bandwidth_mbps_request

        out["baselineEbsBandwidthMbps"] = (
            capo_ecs.types.baseline_ebs_bandwidth_mbps_request.serialize_aws_json_1_1(
                value["baseline_ebs_bandwidth_mbps"]
            )
        )
    if "accelerator_types" in value:
        import capo_ecs.types.accelerator_type_set

        out["acceleratorTypes"] = (
            capo_ecs.types.accelerator_type_set.serialize_aws_json_1_1(
                value["accelerator_types"]
            )
        )
    if "accelerator_count" in value:
        import capo_ecs.types.accelerator_count_request

        out["acceleratorCount"] = (
            capo_ecs.types.accelerator_count_request.serialize_aws_json_1_1(
                value["accelerator_count"]
            )
        )
    if "accelerator_manufacturers" in value:
        import capo_ecs.types.accelerator_manufacturer_set

        out["acceleratorManufacturers"] = (
            capo_ecs.types.accelerator_manufacturer_set.serialize_aws_json_1_1(
                value["accelerator_manufacturers"]
            )
        )
    if "accelerator_names" in value:
        import capo_ecs.types.accelerator_name_set

        out["acceleratorNames"] = (
            capo_ecs.types.accelerator_name_set.serialize_aws_json_1_1(
                value["accelerator_names"]
            )
        )
    if "accelerator_total_memory_mi_b" in value:
        import capo_ecs.types.accelerator_total_memory_mi_b_request

        out["acceleratorTotalMemoryMiB"] = (
            capo_ecs.types.accelerator_total_memory_mi_b_request.serialize_aws_json_1_1(
                value["accelerator_total_memory_mi_b"]
            )
        )
    if "network_bandwidth_gbps" in value:
        import capo_ecs.types.network_bandwidth_gbps_request

        out["networkBandwidthGbps"] = (
            capo_ecs.types.network_bandwidth_gbps_request.serialize_aws_json_1_1(
                value["network_bandwidth_gbps"]
            )
        )
    if "allowed_instance_types" in value:
        import capo_ecs.types.allowed_instance_type_set

        out["allowedInstanceTypes"] = (
            capo_ecs.types.allowed_instance_type_set.serialize_aws_json_1_1(
                value["allowed_instance_types"]
            )
        )
    if "max_spot_price_as_percentage_of_optimal_on_demand_price" in value:
        out["maxSpotPriceAsPercentageOfOptimalOnDemandPrice"] = value[
            "max_spot_price_as_percentage_of_optimal_on_demand_price"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceRequirementsRequest:
    out: InstanceRequirementsRequest = {}  # type: ignore[typeddict-item]
    if "vCpuCount" in data:
        import capo_ecs.types.v_cpu_count_range_request

        out["v_cpu_count"] = (
            capo_ecs.types.v_cpu_count_range_request.deserialize_aws_json_1_1(
                data["vCpuCount"]
            )
        )
    else:
        raise DeserializationError("InstanceRequirementsRequest.v_cpu_count required")
    if "memoryMiB" in data:
        import capo_ecs.types.memory_mi_b_request

        out["memory_mi_b"] = (
            capo_ecs.types.memory_mi_b_request.deserialize_aws_json_1_1(
                data["memoryMiB"]
            )
        )
    else:
        raise DeserializationError("InstanceRequirementsRequest.memory_mi_b required")
    if "cpuManufacturers" in data:
        import capo_ecs.types.cpu_manufacturer_set

        out["cpu_manufacturers"] = (
            capo_ecs.types.cpu_manufacturer_set.deserialize_aws_json_1_1(
                data["cpuManufacturers"]
            )
        )
    if "memoryGiBPerVCpu" in data:
        import capo_ecs.types.memory_gi_b_per_v_cpu_request

        out["memory_gi_b_per_v_cpu"] = (
            capo_ecs.types.memory_gi_b_per_v_cpu_request.deserialize_aws_json_1_1(
                data["memoryGiBPerVCpu"]
            )
        )
    if "excludedInstanceTypes" in data:
        import capo_ecs.types.excluded_instance_type_set

        out["excluded_instance_types"] = (
            capo_ecs.types.excluded_instance_type_set.deserialize_aws_json_1_1(
                data["excludedInstanceTypes"]
            )
        )
    if "instanceGenerations" in data:
        import capo_ecs.types.instance_generation_set

        out["instance_generations"] = (
            capo_ecs.types.instance_generation_set.deserialize_aws_json_1_1(
                data["instanceGenerations"]
            )
        )
    if "spotMaxPricePercentageOverLowestPrice" in data:
        out["spot_max_price_percentage_over_lowest_price"] = data[
            "spotMaxPricePercentageOverLowestPrice"
        ]
    if "onDemandMaxPricePercentageOverLowestPrice" in data:
        out["on_demand_max_price_percentage_over_lowest_price"] = data[
            "onDemandMaxPricePercentageOverLowestPrice"
        ]
    if "bareMetal" in data:
        import capo_ecs.types.bare_metal

        out["bare_metal"] = capo_ecs.types.bare_metal.deserialize_aws_json_1_1(
            data["bareMetal"]
        )
    if "burstablePerformance" in data:
        import capo_ecs.types.burstable_performance

        out["burstable_performance"] = (
            capo_ecs.types.burstable_performance.deserialize_aws_json_1_1(
                data["burstablePerformance"]
            )
        )
    if "requireHibernateSupport" in data:
        out["require_hibernate_support"] = data["requireHibernateSupport"]
    if "networkInterfaceCount" in data:
        import capo_ecs.types.network_interface_count_request

        out["network_interface_count"] = (
            capo_ecs.types.network_interface_count_request.deserialize_aws_json_1_1(
                data["networkInterfaceCount"]
            )
        )
    if "localStorage" in data:
        import capo_ecs.types.local_storage

        out["local_storage"] = capo_ecs.types.local_storage.deserialize_aws_json_1_1(
            data["localStorage"]
        )
    if "localStorageTypes" in data:
        import capo_ecs.types.local_storage_type_set

        out["local_storage_types"] = (
            capo_ecs.types.local_storage_type_set.deserialize_aws_json_1_1(
                data["localStorageTypes"]
            )
        )
    if "totalLocalStorageGB" in data:
        import capo_ecs.types.total_local_storage_gb_request

        out["total_local_storage_gb"] = (
            capo_ecs.types.total_local_storage_gb_request.deserialize_aws_json_1_1(
                data["totalLocalStorageGB"]
            )
        )
    if "baselineEbsBandwidthMbps" in data:
        import capo_ecs.types.baseline_ebs_bandwidth_mbps_request

        out["baseline_ebs_bandwidth_mbps"] = (
            capo_ecs.types.baseline_ebs_bandwidth_mbps_request.deserialize_aws_json_1_1(
                data["baselineEbsBandwidthMbps"]
            )
        )
    if "acceleratorTypes" in data:
        import capo_ecs.types.accelerator_type_set

        out["accelerator_types"] = (
            capo_ecs.types.accelerator_type_set.deserialize_aws_json_1_1(
                data["acceleratorTypes"]
            )
        )
    if "acceleratorCount" in data:
        import capo_ecs.types.accelerator_count_request

        out["accelerator_count"] = (
            capo_ecs.types.accelerator_count_request.deserialize_aws_json_1_1(
                data["acceleratorCount"]
            )
        )
    if "acceleratorManufacturers" in data:
        import capo_ecs.types.accelerator_manufacturer_set

        out["accelerator_manufacturers"] = (
            capo_ecs.types.accelerator_manufacturer_set.deserialize_aws_json_1_1(
                data["acceleratorManufacturers"]
            )
        )
    if "acceleratorNames" in data:
        import capo_ecs.types.accelerator_name_set

        out["accelerator_names"] = (
            capo_ecs.types.accelerator_name_set.deserialize_aws_json_1_1(
                data["acceleratorNames"]
            )
        )
    if "acceleratorTotalMemoryMiB" in data:
        import capo_ecs.types.accelerator_total_memory_mi_b_request

        out["accelerator_total_memory_mi_b"] = (
            capo_ecs.types.accelerator_total_memory_mi_b_request.deserialize_aws_json_1_1(
                data["acceleratorTotalMemoryMiB"]
            )
        )
    if "networkBandwidthGbps" in data:
        import capo_ecs.types.network_bandwidth_gbps_request

        out["network_bandwidth_gbps"] = (
            capo_ecs.types.network_bandwidth_gbps_request.deserialize_aws_json_1_1(
                data["networkBandwidthGbps"]
            )
        )
    if "allowedInstanceTypes" in data:
        import capo_ecs.types.allowed_instance_type_set

        out["allowed_instance_types"] = (
            capo_ecs.types.allowed_instance_type_set.deserialize_aws_json_1_1(
                data["allowedInstanceTypes"]
            )
        )
    if "maxSpotPriceAsPercentageOfOptimalOnDemandPrice" in data:
        out["max_spot_price_as_percentage_of_optimal_on_demand_price"] = data[
            "maxSpotPriceAsPercentageOfOptimalOnDemandPrice"
        ]
    return out
