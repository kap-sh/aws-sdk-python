"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceCreditSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.string


class InstanceCreditSpecificationRequest(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    cpu_credits: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The credit option for CPU usage of the instance.</p> <p>Valid values: <code>standard</code> | <code>unlimited</code> </p> <p>T3 instances with <code>host</code> tenancy do not support the <code>unlimited</code> CPU credit option.</p>"""
