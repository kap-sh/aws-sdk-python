"""Generated from Smithy shape ``com.amazonaws.sagemaker#ComputeQuotaResourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.accelerator_partition_config
    import aws_sdk_sagemaker.types.accelerators_amount
    import aws_sdk_sagemaker.types.cluster_instance_type
    import aws_sdk_sagemaker.types.instance_count
    import aws_sdk_sagemaker.types.memory_in_gi_b_amount
    import aws_sdk_sagemaker.types.v_cpu_amount


class ComputeQuotaResourceConfig(TypedDict, closed=True):
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_type.ClusterInstanceType"
    ]
    """<p>The instance type of the instance group for the cluster.</p>"""
    count: NotRequired["aws_sdk_sagemaker.types.instance_count.InstanceCount"]
    """<p>The number of instances to add to the instance group of a SageMaker HyperPod cluster.</p>"""
    accelerators: NotRequired[
        "aws_sdk_sagemaker.types.accelerators_amount.AcceleratorsAmount"
    ]
    """<p>The number of accelerators to allocate. If you don't specify a value for vCPU and MemoryInGiB, SageMaker AI automatically allocates ratio-based values for those parameters based on the number of accelerators you provide. For example, if you allocate 16 out of 32 total accelerators, SageMaker AI uses the ratio of 0.5 and allocates values to vCPU and MemoryInGiB.</p>"""
    v_cpu: NotRequired["aws_sdk_sagemaker.types.v_cpu_amount.VCpuAmount"]
    """<p>The number of vCPU to allocate. If you specify a value only for vCPU, SageMaker AI automatically allocates ratio-based values for MemoryInGiB based on this vCPU parameter. For example, if you allocate 20 out of 40 total vCPU, SageMaker AI uses the ratio of 0.5 and allocates values to MemoryInGiB. Accelerators are set to 0.</p>"""
    memory_in_gi_b: NotRequired[
        "aws_sdk_sagemaker.types.memory_in_gi_b_amount.MemoryInGiBAmount"
    ]
    """<p>The amount of memory in GiB to allocate. If you specify a value only for this parameter, SageMaker AI automatically allocates a ratio-based value for vCPU based on this memory that you provide. For example, if you allocate 200 out of 400 total memory in GiB, SageMaker AI uses the ratio of 0.5 and allocates values to vCPU. Accelerators are set to 0.</p>"""
    accelerator_partition: NotRequired[
        "aws_sdk_sagemaker.types.accelerator_partition_config.AcceleratorPartitionConfig"
    ]
    """<p>The accelerator partition configuration for fractional GPU allocation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeQuotaResourceConfig) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.cluster_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.cluster_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "count" in value:
        out["Count"] = value["count"]
    if "accelerators" in value:
        out["Accelerators"] = value["accelerators"]
    if "v_cpu" in value:
        out["VCpu"] = value["v_cpu"]
    if "memory_in_gi_b" in value:
        out["MemoryInGiB"] = value["memory_in_gi_b"]
    if "accelerator_partition" in value:
        import aws_sdk_sagemaker.types.accelerator_partition_config

        out["AcceleratorPartition"] = (
            aws_sdk_sagemaker.types.accelerator_partition_config.serialize_aws_json_1_1(
                value["accelerator_partition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeQuotaResourceConfig:
    out: ComputeQuotaResourceConfig = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.cluster_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.cluster_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "Count" in data:
        out["count"] = data["Count"]
    if "Accelerators" in data:
        out["accelerators"] = data["Accelerators"]
    if "VCpu" in data:
        out["v_cpu"] = data["VCpu"]
    if "MemoryInGiB" in data:
        out["memory_in_gi_b"] = data["MemoryInGiB"]
    if "AcceleratorPartition" in data:
        import aws_sdk_sagemaker.types.accelerator_partition_config

        out["accelerator_partition"] = (
            aws_sdk_sagemaker.types.accelerator_partition_config.deserialize_aws_json_1_1(
                data["AcceleratorPartition"]
            )
        )
    return out
