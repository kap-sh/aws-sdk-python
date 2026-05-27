"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesIamInstanceProfile``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ScheduledInstancesIamInstanceProfile(TypedDict):
    arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN).</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name.</p>"""
