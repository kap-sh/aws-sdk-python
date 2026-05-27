"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceCpuOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.nested_virtualization_specification


class ModifyInstanceCpuOptionsResult(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance that was updated.</p>"""
    core_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of CPU cores that are running for the specified instance after the update.</p>"""
    threads_per_core: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of threads that are running per CPU core for the specified instance after the update.</p>"""
    nested_virtualization: NotRequired[
        "aws_sdk_ec2.types.nested_virtualization_specification.NestedVirtualizationSpecification"
    ]
    """<p>Indicates whether nested virtualization has been enabled or disabled.</p>"""
