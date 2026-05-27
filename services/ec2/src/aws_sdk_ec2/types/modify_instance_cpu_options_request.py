"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceCpuOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.nested_virtualization_specification


class ModifyInstanceCpuOptionsRequest(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance to update.</p>"""
    core_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of CPU cores to activate for the specified instance.</p>"""
    threads_per_core: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of threads to run for each CPU core.</p>"""
    nested_virtualization: NotRequired[
        "aws_sdk_ec2.types.nested_virtualization_specification.NestedVirtualizationSpecification"
    ]
    """<p>Indicates whether to enable or disable nested virtualization for the instance. When nested virtualization is enabled, Virtual Secure Mode (VSM) is automatically disabled for the instance.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
