"""Generated from Smithy shape ``com.amazonaws.ec2#VpnTunnelOptionsSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ike_versions_request_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.phase1_dh_group_numbers_request_list
    import aws_sdk_ec2.types.phase1_encryption_algorithms_request_list
    import aws_sdk_ec2.types.phase1_integrity_algorithms_request_list
    import aws_sdk_ec2.types.phase2_dh_group_numbers_request_list
    import aws_sdk_ec2.types.phase2_encryption_algorithms_request_list
    import aws_sdk_ec2.types.phase2_integrity_algorithms_request_list
    import aws_sdk_ec2.types.pre_shared_key
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpn_tunnel_log_options_specification


class VpnTunnelOptionsSpecification(TypedDict):
    tunnel_inside_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The range of inside IPv4 addresses for the tunnel. Any specified CIDR blocks must be unique across all VPN connections that use the same virtual private gateway. </p> <p>Constraints: A size /30 CIDR block from the <code>169.254.0.0/16</code> range. The following CIDR blocks are reserved and cannot be used:</p> <ul> <li> <p> <code>169.254.0.0/30</code> </p> </li> <li> <p> <code>169.254.1.0/30</code> </p> </li> <li> <p> <code>169.254.2.0/30</code> </p> </li> <li> <p> <code>169.254.3.0/30</code> </p> </li> <li> <p> <code>169.254.4.0/30</code> </p> </li> <li> <p> <code>169.254.5.0/30</code> </p> </li> <li> <p> <code>169.254.169.252/30</code> </p> </li> </ul>"""
    tunnel_inside_ipv6_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The range of inside IPv6 addresses for the tunnel. Any specified CIDR blocks must be unique across all VPN connections that use the same transit gateway.</p> <p>Constraints: A size /126 CIDR block from the local <code>fd00::/8</code> range.</p>"""
    pre_shared_key: NotRequired["aws_sdk_ec2.types.pre_shared_key.preSharedKey"]
    """<p>The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and customer gateway.</p> <p>Constraints: Allowed characters are alphanumeric characters, periods (.), and underscores (_). Must be between 8 and 64 characters in length and cannot start with zero (0).</p>"""
    phase1_lifetime_seconds: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The lifetime for phase 1 of the IKE negotiation, in seconds.</p> <p>Constraints: A value between 900 and 28,800.</p> <p>Default: <code>28800</code> </p>"""
    phase2_lifetime_seconds: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The lifetime for phase 2 of the IKE negotiation, in seconds.</p> <p>Constraints: A value between 900 and 3,600. The value must be less than the value for <code>Phase1LifetimeSeconds</code>.</p> <p>Default: <code>3600</code> </p>"""
    rekey_margin_time_seconds: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The margin time, in seconds, before the phase 2 lifetime expires, during which the Amazon Web Services side of the VPN connection performs an IKE rekey. The exact time of the rekey is randomly selected based on the value for <code>RekeyFuzzPercentage</code>.</p> <p>Constraints: A value between 60 and half of <code>Phase2LifetimeSeconds</code>.</p> <p>Default: <code>270</code> </p>"""
    rekey_fuzz_percentage: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The percentage of the rekey window (determined by <code>RekeyMarginTimeSeconds</code>) during which the rekey time is randomly selected.</p> <p>Constraints: A value between 0 and 100.</p> <p>Default: <code>100</code> </p>"""
    replay_window_size: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of packets in an IKE replay window.</p> <p>Constraints: A value between 64 and 2048.</p> <p>Default: <code>1024</code> </p>"""
    dpd_timeout_seconds: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of seconds after which a DPD timeout occurs.</p> <p>Constraints: A value greater than or equal to 30.</p> <p>Default: <code>30</code> </p>"""
    dpd_timeout_action: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The action to take after DPD timeout occurs. Specify <code>restart</code> to restart the IKE initiation. Specify <code>clear</code> to end the IKE session.</p> <p>Valid Values: <code>clear</code> | <code>none</code> | <code>restart</code> </p> <p>Default: <code>clear</code> </p>"""
    phase1_encryption_algorithms: NotRequired[
        "aws_sdk_ec2.types.phase1_encryption_algorithms_request_list.Phase1EncryptionAlgorithmsRequestList"
    ]
    """<p>One or more encryption algorithms that are permitted for the VPN tunnel for phase 1 IKE negotiations.</p> <p>Valid values: <code>AES128</code> | <code>AES256</code> | <code>AES128-GCM-16</code> | <code>AES256-GCM-16</code> </p>"""
    phase2_encryption_algorithms: NotRequired[
        "aws_sdk_ec2.types.phase2_encryption_algorithms_request_list.Phase2EncryptionAlgorithmsRequestList"
    ]
    """<p>One or more encryption algorithms that are permitted for the VPN tunnel for phase 2 IKE negotiations.</p> <p>Valid values: <code>AES128</code> | <code>AES256</code> | <code>AES128-GCM-16</code> | <code>AES256-GCM-16</code> </p>"""
    phase1_integrity_algorithms: NotRequired[
        "aws_sdk_ec2.types.phase1_integrity_algorithms_request_list.Phase1IntegrityAlgorithmsRequestList"
    ]
    """<p>One or more integrity algorithms that are permitted for the VPN tunnel for phase 1 IKE negotiations.</p> <p>Valid values: <code>SHA1</code> | <code>SHA2-256</code> | <code>SHA2-384</code> | <code>SHA2-512</code> </p>"""
    phase2_integrity_algorithms: NotRequired[
        "aws_sdk_ec2.types.phase2_integrity_algorithms_request_list.Phase2IntegrityAlgorithmsRequestList"
    ]
    """<p>One or more integrity algorithms that are permitted for the VPN tunnel for phase 2 IKE negotiations.</p> <p>Valid values: <code>SHA1</code> | <code>SHA2-256</code> | <code>SHA2-384</code> | <code>SHA2-512</code> </p>"""
    phase1_dh_group_numbers: NotRequired[
        "aws_sdk_ec2.types.phase1_dh_group_numbers_request_list.Phase1DHGroupNumbersRequestList"
    ]
    """<p>One or more Diffie-Hellman group numbers that are permitted for the VPN tunnel for phase 1 IKE negotiations.</p> <p>Valid values: <code>2</code> | <code>14</code> | <code>15</code> | <code>16</code> | <code>17</code> | <code>18</code> | <code>19</code> | <code>20</code> | <code>21</code> | <code>22</code> | <code>23</code> | <code>24</code> </p>"""
    phase2_dh_group_numbers: NotRequired[
        "aws_sdk_ec2.types.phase2_dh_group_numbers_request_list.Phase2DHGroupNumbersRequestList"
    ]
    """<p>One or more Diffie-Hellman group numbers that are permitted for the VPN tunnel for phase 2 IKE negotiations.</p> <p>Valid values: <code>2</code> | <code>5</code> | <code>14</code> | <code>15</code> | <code>16</code> | <code>17</code> | <code>18</code> | <code>19</code> | <code>20</code> | <code>21</code> | <code>22</code> | <code>23</code> | <code>24</code> </p>"""
    ike_versions: NotRequired[
        "aws_sdk_ec2.types.ike_versions_request_list.IKEVersionsRequestList"
    ]
    """<p>The IKE versions that are permitted for the VPN tunnel.</p> <p>Valid values: <code>ikev1</code> | <code>ikev2</code> </p>"""
    startup_action: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The action to take when the establishing the tunnel for the VPN connection. By default, your customer gateway device must initiate the IKE negotiation and bring up the tunnel. Specify <code>start</code> for Amazon Web Services to initiate the IKE negotiation.</p> <p>Valid Values: <code>add</code> | <code>start</code> </p> <p>Default: <code>add</code> </p>"""
    log_options: NotRequired[
        "aws_sdk_ec2.types.vpn_tunnel_log_options_specification.VpnTunnelLogOptionsSpecification"
    ]
    """<p>Options for logging VPN tunnel activity.</p>"""
    enable_tunnel_lifecycle_control: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Turn on or off tunnel endpoint lifecycle control feature.</p>"""
