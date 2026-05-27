"""Generated from Smithy shape ``com.amazonaws.ec2#TunnelOption``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ike_versions_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.phase1_dh_group_numbers_list
    import aws_sdk_ec2.types.phase1_encryption_algorithms_list
    import aws_sdk_ec2.types.phase1_integrity_algorithms_list
    import aws_sdk_ec2.types.phase2_dh_group_numbers_list
    import aws_sdk_ec2.types.phase2_encryption_algorithms_list
    import aws_sdk_ec2.types.phase2_integrity_algorithms_list
    import aws_sdk_ec2.types.pre_shared_key
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpn_tunnel_log_options


class TunnelOption(TypedDict):
    outside_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The external IP address of the VPN tunnel.</p>"""
    tunnel_inside_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The range of inside IPv4 addresses for the tunnel.</p>"""
    tunnel_inside_ipv6_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The range of inside IPv6 addresses for the tunnel.</p>"""
    pre_shared_key: NotRequired["aws_sdk_ec2.types.pre_shared_key.preSharedKey"]
    """<p>The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and the customer gateway.</p>"""
    phase1_lifetime_seconds: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The lifetime for phase 1 of the IKE negotiation, in seconds.</p>"""
    phase2_lifetime_seconds: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The lifetime for phase 2 of the IKE negotiation, in seconds.</p>"""
    rekey_margin_time_seconds: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The margin time, in seconds, before the phase 2 lifetime expires, during which the Amazon Web Services side of the VPN connection performs an IKE rekey.</p>"""
    rekey_fuzz_percentage: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The percentage of the rekey window determined by <code>RekeyMarginTimeSeconds</code> during which the rekey time is randomly selected.</p>"""
    replay_window_size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of packets in an IKE replay window.</p>"""
    dpd_timeout_seconds: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of seconds after which a DPD timeout occurs.</p>"""
    dpd_timeout_action: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The action to take after a DPD timeout occurs.</p>"""
    phase1_encryption_algorithms: NotRequired[
        "aws_sdk_ec2.types.phase1_encryption_algorithms_list.Phase1EncryptionAlgorithmsList"
    ]
    """<p>The permitted encryption algorithms for the VPN tunnel for phase 1 IKE negotiations.</p>"""
    phase2_encryption_algorithms: NotRequired[
        "aws_sdk_ec2.types.phase2_encryption_algorithms_list.Phase2EncryptionAlgorithmsList"
    ]
    """<p>The permitted encryption algorithms for the VPN tunnel for phase 2 IKE negotiations.</p>"""
    phase1_integrity_algorithms: NotRequired[
        "aws_sdk_ec2.types.phase1_integrity_algorithms_list.Phase1IntegrityAlgorithmsList"
    ]
    """<p>The permitted integrity algorithms for the VPN tunnel for phase 1 IKE negotiations.</p>"""
    phase2_integrity_algorithms: NotRequired[
        "aws_sdk_ec2.types.phase2_integrity_algorithms_list.Phase2IntegrityAlgorithmsList"
    ]
    """<p>The permitted integrity algorithms for the VPN tunnel for phase 2 IKE negotiations.</p>"""
    phase1_dh_group_numbers: NotRequired[
        "aws_sdk_ec2.types.phase1_dh_group_numbers_list.Phase1DHGroupNumbersList"
    ]
    """<p>The permitted Diffie-Hellman group numbers for the VPN tunnel for phase 1 IKE negotiations.</p>"""
    phase2_dh_group_numbers: NotRequired[
        "aws_sdk_ec2.types.phase2_dh_group_numbers_list.Phase2DHGroupNumbersList"
    ]
    """<p>The permitted Diffie-Hellman group numbers for the VPN tunnel for phase 2 IKE negotiations.</p>"""
    ike_versions: NotRequired["aws_sdk_ec2.types.ike_versions_list.IKEVersionsList"]
    """<p>The IKE versions that are permitted for the VPN tunnel.</p>"""
    startup_action: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The action to take when the establishing the VPN tunnels for a VPN connection.</p>"""
    log_options: NotRequired[
        "aws_sdk_ec2.types.vpn_tunnel_log_options.VpnTunnelLogOptions"
    ]
    """<p>Options for logging VPN tunnel activity.</p>"""
    enable_tunnel_lifecycle_control: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Status of tunnel endpoint lifecycle control feature.</p>"""
