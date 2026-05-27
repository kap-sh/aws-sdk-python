"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStatusDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.status_name
    import aws_sdk_ec2.types.status_type


class InstanceStatusDetails(TypedDict):
    impaired_since: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time when a status check failed. For an instance that was launched and impaired, this is the time when the instance was launched.</p>"""
    name: NotRequired["aws_sdk_ec2.types.status_name.StatusName"]
    """<p>The type of instance status.</p>"""
    status: NotRequired["aws_sdk_ec2.types.status_type.StatusType"]
    """<p>The status.</p>"""
