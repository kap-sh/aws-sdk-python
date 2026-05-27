"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateIamInstanceProfileSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class LaunchTemplateIamInstanceProfileSpecification(TypedDict):
    arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the instance profile.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the instance profile.</p>"""
