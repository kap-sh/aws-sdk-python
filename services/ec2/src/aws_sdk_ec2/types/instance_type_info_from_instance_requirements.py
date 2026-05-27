"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeInfoFromInstanceRequirements``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class InstanceTypeInfoFromInstanceRequirements(TypedDict):
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The matching instance type.</p>"""
