"""Generated from Smithy shape ``com.amazonaws.ec2#GpuDeviceInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.gpu_device_count
    import aws_sdk_ec2.types.gpu_device_manufacturer_name
    import aws_sdk_ec2.types.gpu_device_memory_info
    import aws_sdk_ec2.types.gpu_device_name
    import aws_sdk_ec2.types.gpu_partition_size
    import aws_sdk_ec2.types.logical_gpu_count
    import aws_sdk_ec2.types.workloads_list


class GpuDeviceInfo(TypedDict):
    name: NotRequired["aws_sdk_ec2.types.gpu_device_name.GpuDeviceName"]
    """<p>The name of the GPU accelerator.</p>"""
    manufacturer: NotRequired[
        "aws_sdk_ec2.types.gpu_device_manufacturer_name.GpuDeviceManufacturerName"
    ]
    """<p>The manufacturer of the GPU accelerator.</p>"""
    count: NotRequired["aws_sdk_ec2.types.gpu_device_count.GpuDeviceCount"]
    """<p>The number of GPUs for the instance type.</p>"""
    logical_gpu_count: NotRequired[
        "aws_sdk_ec2.types.logical_gpu_count.LogicalGpuCount"
    ]
    """<p>Total number of GPU devices of this type.</p>"""
    gpu_partition_size: NotRequired[
        "aws_sdk_ec2.types.gpu_partition_size.GpuPartitionSize"
    ]
    """<p>The size of each GPU as a fraction of a full GPU, between 0 (excluded) and 1 (included).</p>"""
    workloads: NotRequired["aws_sdk_ec2.types.workloads_list.WorkloadsList"]
    """<p>A list of workload types this GPU supports.</p>"""
    memory_info: NotRequired[
        "aws_sdk_ec2.types.gpu_device_memory_info.GpuDeviceMemoryInfo"
    ]
    """<p>Describes the memory available to the GPU accelerator.</p>"""
