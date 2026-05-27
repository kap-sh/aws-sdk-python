"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayMeteringPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.transit_gateway_attachment_id_string_list
    import aws_sdk_ec2.types.transit_gateway_metering_policy_id


class ModifyTransitGatewayMeteringPolicyRequest(TypedDict):
    transit_gateway_metering_policy_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_id.TransitGatewayMeteringPolicyId"
    ]
    """<p>The ID of the transit gateway metering policy to modify.</p>"""
    add_middlebox_attachment_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id_string_list.TransitGatewayAttachmentIdStringList"
    ]
    """<p>The IDs of middlebox attachments to add to the metering policy.</p>"""
    remove_middlebox_attachment_ids: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id_string_list.TransitGatewayAttachmentIdStringList"
    ]
    """<p>The IDs of middlebox attachments to remove from the metering policy.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
