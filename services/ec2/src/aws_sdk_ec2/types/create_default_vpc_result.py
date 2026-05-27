"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDefaultVpcResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc


class CreateDefaultVpcResult(TypedDict):
    vpc: NotRequired["aws_sdk_ec2.types.vpc.Vpc"]
    """<p>Information about the VPC.</p>"""
