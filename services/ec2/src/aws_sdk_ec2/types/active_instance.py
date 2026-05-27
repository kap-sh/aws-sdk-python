"""Generated from Smithy shape ``com.amazonaws.ec2#ActiveInstance``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_health_status
    import aws_sdk_ec2.types.string


class ActiveInstance(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type.</p>"""
    spot_instance_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Spot Instance request.</p>"""
    instance_health: NotRequired[
        "aws_sdk_ec2.types.instance_health_status.InstanceHealthStatus"
    ]
    """<p>The health status of the instance. If the status of either the instance status check or the system status check is <code>impaired</code>, the health status of the instance is <code>unhealthy</code>. Otherwise, the health status is <code>healthy</code>.</p>"""
