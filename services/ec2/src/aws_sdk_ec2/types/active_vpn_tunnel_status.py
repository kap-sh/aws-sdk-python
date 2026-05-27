"""Generated from Smithy shape ``com.amazonaws.ec2#ActiveVpnTunnelStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpn_tunnel_provisioning_status


class ActiveVpnTunnelStatus(TypedDict):
    phase1_encryption_algorithm: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The encryption algorithm negotiated in Phase 1 IKE negotiations.</p>"""
    phase2_encryption_algorithm: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The encryption algorithm negotiated in Phase 2 IKE negotiations.</p>"""
    phase1_integrity_algorithm: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The integrity algorithm negotiated in Phase 1 IKE negotiations.</p>"""
    phase2_integrity_algorithm: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The integrity algorithm negotiated in Phase 2 IKE negotiations.</p>"""
    phase1_dh_group: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The Diffie-Hellman group number being used in Phase 1 IKE negotiations.</p>"""
    phase2_dh_group: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The Diffie-Hellman group number being used in Phase 2 IKE negotiations.</p>"""
    ike_version: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The version of the Internet Key Exchange (IKE) protocol being used.</p>"""
    provisioning_status: NotRequired[
        "aws_sdk_ec2.types.vpn_tunnel_provisioning_status.VpnTunnelProvisioningStatus"
    ]
    """<p>The current provisioning status of the VPN tunnel.</p>"""
    provisioning_status_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the current provisioning status.</p>"""
