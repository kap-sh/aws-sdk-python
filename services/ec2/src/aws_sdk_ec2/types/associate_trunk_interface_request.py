"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateTrunkInterfaceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.string


class AssociateTrunkInterfaceRequest(TypedDict):
    branch_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the branch network interface.</p>"""
    trunk_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the trunk network interface.</p>"""
    vlan_id: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The ID of the VLAN. This applies to the VLAN protocol.</p>"""
    gre_key: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The application key. This applies to the GRE protocol.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
