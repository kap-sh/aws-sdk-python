"""Generated from Smithy shape ``com.amazonaws.ec2#CreditSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CreditSpecificationRequest(TypedDict):
    cpu_credits: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The credit option for CPU usage of a T instance.</p> <p>Valid values: <code>standard</code> | <code>unlimited</code> </p>"""
