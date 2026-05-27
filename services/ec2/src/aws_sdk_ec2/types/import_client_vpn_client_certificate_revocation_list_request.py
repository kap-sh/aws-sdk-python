"""Generated from Smithy shape ``com.amazonaws.ec2#ImportClientVpnClientCertificateRevocationListRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_vpn_endpoint_id
    import aws_sdk_ec2.types.string


class ImportClientVpnClientCertificateRevocationListRequest(TypedDict):
    client_vpn_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint to which the client certificate revocation list applies.</p>"""
    certificate_revocation_list: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The client certificate revocation list file. For more information, see <a href=\"https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-certificates.html#cvpn-working-certificates-generate\">Generate a Client Certificate Revocation List</a> in the <i>Client VPN Administrator Guide</i>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
