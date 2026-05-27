"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateInstanceEventWindowRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_event_window_disassociation_request
    import aws_sdk_ec2.types.instance_event_window_id


class DisassociateInstanceEventWindowRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_event_window_id: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_id.InstanceEventWindowId"
    ]
    """<p>The ID of the event window.</p>"""
    association_target: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_disassociation_request.InstanceEventWindowDisassociationRequest"
    ]
    """<p>One or more targets to disassociate from the specified event window.</p>"""
