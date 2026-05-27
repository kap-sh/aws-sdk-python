"""Generated from Smithy shape ``com.amazonaws.ec2#RunScheduledInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_id_set


class RunScheduledInstancesResult(TypedDict):
    instance_id_set: NotRequired["aws_sdk_ec2.types.instance_id_set.InstanceIdSet"]
    """<p>The IDs of the newly launched instances.</p>"""
