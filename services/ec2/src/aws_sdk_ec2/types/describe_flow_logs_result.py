"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFlowLogsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.flow_log_set
    import aws_sdk_ec2.types.string


class DescribeFlowLogsResult(TypedDict):
    flow_logs: NotRequired["aws_sdk_ec2.types.flow_log_set.FlowLogSet"]
    """<p>Information about the flow logs.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to request the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
