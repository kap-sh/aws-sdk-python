"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnConnectionDeviceSampleConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpn_connection_device_type_id
    import aws_sdk_ec2.types.vpn_connection_id


class GetVpnConnectionDeviceSampleConfigurationRequest(TypedDict):
    vpn_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_id.VpnConnectionId"
    ]
    """<p>The <code>VpnConnectionId</code> specifies the Site-to-Site VPN connection used for the sample configuration.</p>"""
    vpn_connection_device_type_id: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_device_type_id.VpnConnectionDeviceTypeId"
    ]
    """<p>Device identifier provided by the <code>GetVpnConnectionDeviceTypes</code> API.</p>"""
    internet_key_exchange_version: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IKE version to be used in the sample configuration file for your customer gateway device. You can specify one of the following versions: <code>ikev1</code> or <code>ikev2</code>.</p>"""
    sample_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of sample configuration to generate. Valid values are \"compatibility\" (includes IKEv1) or \"recommended\" (throws UnsupportedOperationException for IKEv1).</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
