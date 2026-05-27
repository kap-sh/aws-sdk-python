"""Generated from Smithy shape ``com.amazonaws.ec2#VCpuInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.core_count
    import aws_sdk_ec2.types.core_count_list
    import aws_sdk_ec2.types.threads_per_core
    import aws_sdk_ec2.types.threads_per_core_list
    import aws_sdk_ec2.types.v_cpu_count


class VCpuInfo(TypedDict):
    default_v_cpus: NotRequired["aws_sdk_ec2.types.v_cpu_count.VCpuCount"]
    """<p>The default number of vCPUs for the instance type.</p>"""
    default_cores: NotRequired["aws_sdk_ec2.types.core_count.CoreCount"]
    """<p>The default number of cores for the instance type.</p>"""
    default_threads_per_core: NotRequired[
        "aws_sdk_ec2.types.threads_per_core.ThreadsPerCore"
    ]
    """<p>The default number of threads per core for the instance type.</p>"""
    valid_cores: NotRequired["aws_sdk_ec2.types.core_count_list.CoreCountList"]
    """<p>The valid number of cores that can be configured for the instance type.</p>"""
    valid_threads_per_core: NotRequired[
        "aws_sdk_ec2.types.threads_per_core_list.ThreadsPerCoreList"
    ]
    """<p>The valid number of threads per core that can be configured for the instance type.</p>"""
