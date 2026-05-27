"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceCreditSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class InstanceCreditSpecification(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    cpu_credits: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The credit option for CPU usage of the instance.</p> <p>Valid values: <code>standard</code> | <code>unlimited</code> </p>"""
