"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteQueuedReservedInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.delete_queued_reserved_instances_id_list


class DeleteQueuedReservedInstancesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    reserved_instances_ids: NotRequired[
        "aws_sdk_ec2.types.delete_queued_reserved_instances_id_list.DeleteQueuedReservedInstancesIdList"
    ]
    """<p>The IDs of the Reserved Instances.</p>"""
