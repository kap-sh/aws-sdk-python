"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFlowLogsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.flow_log_id_list


class DeleteFlowLogsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    flow_log_ids: NotRequired["aws_sdk_ec2.types.flow_log_id_list.FlowLogIdList"]
    """<p>One or more flow log IDs.</p> <p>Constraint: Maximum of 1000 flow log IDs.</p>"""
