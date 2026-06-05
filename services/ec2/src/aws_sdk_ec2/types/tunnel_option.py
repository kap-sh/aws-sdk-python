"""Generated from Smithy shape ``com.amazonaws.ec2#TunnelOption``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TunnelOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "outside_ip_address" in value:
        pairs.append((f"{prefix}.OutsideIpAddress", str(value["outside_ip_address"])))
    if "tunnel_inside_cidr" in value:
        pairs.append((f"{prefix}.TunnelInsideCidr", str(value["tunnel_inside_cidr"])))
    if "tunnel_inside_ipv6_cidr" in value:
        pairs.append(
            (f"{prefix}.TunnelInsideIpv6Cidr", str(value["tunnel_inside_ipv6_cidr"]))
        )
    if "pre_shared_key" in value:
        pairs.append((f"{prefix}.PreSharedKey", str(value["pre_shared_key"])))
    if "phase1_lifetime_seconds" in value:
        pairs.append(
            (f"{prefix}.Phase1LifetimeSeconds", str(value["phase1_lifetime_seconds"]))
        )
    if "phase2_lifetime_seconds" in value:
        pairs.append(
            (f"{prefix}.Phase2LifetimeSeconds", str(value["phase2_lifetime_seconds"]))
        )
    if "rekey_margin_time_seconds" in value:
        pairs.append(
            (
                f"{prefix}.RekeyMarginTimeSeconds",
                str(value["rekey_margin_time_seconds"]),
            )
        )
    if "rekey_fuzz_percentage" in value:
        pairs.append(
            (f"{prefix}.RekeyFuzzPercentage", str(value["rekey_fuzz_percentage"]))
        )
    if "replay_window_size" in value:
        pairs.append((f"{prefix}.ReplayWindowSize", str(value["replay_window_size"])))
    if "dpd_timeout_seconds" in value:
        pairs.append((f"{prefix}.DpdTimeoutSeconds", str(value["dpd_timeout_seconds"])))
    if "dpd_timeout_action" in value:
        pairs.append((f"{prefix}.DpdTimeoutAction", str(value["dpd_timeout_action"])))
    if "phase1_encryption_algorithms" in value:
        import aws_sdk_ec2.types.phase1_encryption_algorithms_list

        aws_sdk_ec2.types.phase1_encryption_algorithms_list.serialize_ec2_query(
            value["phase1_encryption_algorithms"],
            pairs,
            f"{prefix}.Phase1EncryptionAlgorithmSet",
        )
    if "phase2_encryption_algorithms" in value:
        import aws_sdk_ec2.types.phase2_encryption_algorithms_list

        aws_sdk_ec2.types.phase2_encryption_algorithms_list.serialize_ec2_query(
            value["phase2_encryption_algorithms"],
            pairs,
            f"{prefix}.Phase2EncryptionAlgorithmSet",
        )
    if "phase1_integrity_algorithms" in value:
        import aws_sdk_ec2.types.phase1_integrity_algorithms_list

        aws_sdk_ec2.types.phase1_integrity_algorithms_list.serialize_ec2_query(
            value["phase1_integrity_algorithms"],
            pairs,
            f"{prefix}.Phase1IntegrityAlgorithmSet",
        )
    if "phase2_integrity_algorithms" in value:
        import aws_sdk_ec2.types.phase2_integrity_algorithms_list

        aws_sdk_ec2.types.phase2_integrity_algorithms_list.serialize_ec2_query(
            value["phase2_integrity_algorithms"],
            pairs,
            f"{prefix}.Phase2IntegrityAlgorithmSet",
        )
    if "phase1_dh_group_numbers" in value:
        import aws_sdk_ec2.types.phase1_dh_group_numbers_list

        aws_sdk_ec2.types.phase1_dh_group_numbers_list.serialize_ec2_query(
            value["phase1_dh_group_numbers"], pairs, f"{prefix}.Phase1DHGroupNumberSet"
        )
    if "phase2_dh_group_numbers" in value:
        import aws_sdk_ec2.types.phase2_dh_group_numbers_list

        aws_sdk_ec2.types.phase2_dh_group_numbers_list.serialize_ec2_query(
            value["phase2_dh_group_numbers"], pairs, f"{prefix}.Phase2DHGroupNumberSet"
        )
    if "ike_versions" in value:
        import aws_sdk_ec2.types.ike_versions_list

        aws_sdk_ec2.types.ike_versions_list.serialize_ec2_query(
            value["ike_versions"], pairs, f"{prefix}.IkeVersionSet"
        )
    if "startup_action" in value:
        pairs.append((f"{prefix}.StartupAction", str(value["startup_action"])))
    if "log_options" in value:
        import aws_sdk_ec2.types.vpn_tunnel_log_options

        aws_sdk_ec2.types.vpn_tunnel_log_options.serialize_ec2_query(
            value["log_options"], pairs, f"{prefix}.LogOptions"
        )
    if "enable_tunnel_lifecycle_control" in value:
        pairs.append(
            (
                f"{prefix}.EnableTunnelLifecycleControl",
                "true" if value["enable_tunnel_lifecycle_control"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> TunnelOption:
    out: TunnelOption = {}  # type: ignore[typeddict-item]
    child_outside_ip_address = el.find("OutsideIpAddress")
    if child_outside_ip_address is not None:
        out["outside_ip_address"] = str(child_outside_ip_address.text or "")
    child_tunnel_inside_cidr = el.find("TunnelInsideCidr")
    if child_tunnel_inside_cidr is not None:
        out["tunnel_inside_cidr"] = str(child_tunnel_inside_cidr.text or "")
    child_tunnel_inside_ipv6_cidr = el.find("TunnelInsideIpv6Cidr")
    if child_tunnel_inside_ipv6_cidr is not None:
        out["tunnel_inside_ipv6_cidr"] = str(child_tunnel_inside_ipv6_cidr.text or "")
    child_pre_shared_key = el.find("PreSharedKey")
    if child_pre_shared_key is not None:
        out["pre_shared_key"] = str(child_pre_shared_key.text or "")
    child_phase1_lifetime_seconds = el.find("Phase1LifetimeSeconds")
    if child_phase1_lifetime_seconds is not None:
        out["phase1_lifetime_seconds"] = int(child_phase1_lifetime_seconds.text or "")
    child_phase2_lifetime_seconds = el.find("Phase2LifetimeSeconds")
    if child_phase2_lifetime_seconds is not None:
        out["phase2_lifetime_seconds"] = int(child_phase2_lifetime_seconds.text or "")
    child_rekey_margin_time_seconds = el.find("RekeyMarginTimeSeconds")
    if child_rekey_margin_time_seconds is not None:
        out["rekey_margin_time_seconds"] = int(
            child_rekey_margin_time_seconds.text or ""
        )
    child_rekey_fuzz_percentage = el.find("RekeyFuzzPercentage")
    if child_rekey_fuzz_percentage is not None:
        out["rekey_fuzz_percentage"] = int(child_rekey_fuzz_percentage.text or "")
    child_replay_window_size = el.find("ReplayWindowSize")
    if child_replay_window_size is not None:
        out["replay_window_size"] = int(child_replay_window_size.text or "")
    child_dpd_timeout_seconds = el.find("DpdTimeoutSeconds")
    if child_dpd_timeout_seconds is not None:
        out["dpd_timeout_seconds"] = int(child_dpd_timeout_seconds.text or "")
    child_dpd_timeout_action = el.find("DpdTimeoutAction")
    if child_dpd_timeout_action is not None:
        out["dpd_timeout_action"] = str(child_dpd_timeout_action.text or "")
    if el.find("Phase1EncryptionAlgorithmSet") is not None:
        import aws_sdk_ec2.types.phase1_encryption_algorithms_list

        out["phase1_encryption_algorithms"] = (
            aws_sdk_ec2.types.phase1_encryption_algorithms_list.deserialize_ec2_query(
                el, "Phase1EncryptionAlgorithmSet"
            )
        )
    if el.find("Phase2EncryptionAlgorithmSet") is not None:
        import aws_sdk_ec2.types.phase2_encryption_algorithms_list

        out["phase2_encryption_algorithms"] = (
            aws_sdk_ec2.types.phase2_encryption_algorithms_list.deserialize_ec2_query(
                el, "Phase2EncryptionAlgorithmSet"
            )
        )
    if el.find("Phase1IntegrityAlgorithmSet") is not None:
        import aws_sdk_ec2.types.phase1_integrity_algorithms_list

        out["phase1_integrity_algorithms"] = (
            aws_sdk_ec2.types.phase1_integrity_algorithms_list.deserialize_ec2_query(
                el, "Phase1IntegrityAlgorithmSet"
            )
        )
    if el.find("Phase2IntegrityAlgorithmSet") is not None:
        import aws_sdk_ec2.types.phase2_integrity_algorithms_list

        out["phase2_integrity_algorithms"] = (
            aws_sdk_ec2.types.phase2_integrity_algorithms_list.deserialize_ec2_query(
                el, "Phase2IntegrityAlgorithmSet"
            )
        )
    if el.find("Phase1DHGroupNumberSet") is not None:
        import aws_sdk_ec2.types.phase1_dh_group_numbers_list

        out["phase1_dh_group_numbers"] = (
            aws_sdk_ec2.types.phase1_dh_group_numbers_list.deserialize_ec2_query(
                el, "Phase1DHGroupNumberSet"
            )
        )
    if el.find("Phase2DHGroupNumberSet") is not None:
        import aws_sdk_ec2.types.phase2_dh_group_numbers_list

        out["phase2_dh_group_numbers"] = (
            aws_sdk_ec2.types.phase2_dh_group_numbers_list.deserialize_ec2_query(
                el, "Phase2DHGroupNumberSet"
            )
        )
    if el.find("IkeVersionSet") is not None:
        import aws_sdk_ec2.types.ike_versions_list

        out["ike_versions"] = aws_sdk_ec2.types.ike_versions_list.deserialize_ec2_query(
            el, "IkeVersionSet"
        )
    child_startup_action = el.find("StartupAction")
    if child_startup_action is not None:
        out["startup_action"] = str(child_startup_action.text or "")
    child_log_options = el.find("LogOptions")
    if child_log_options is not None:
        import aws_sdk_ec2.types.vpn_tunnel_log_options

        out["log_options"] = (
            aws_sdk_ec2.types.vpn_tunnel_log_options.deserialize_ec2_query(
                child_log_options
            )
        )
    child_enable_tunnel_lifecycle_control = el.find("EnableTunnelLifecycleControl")
    if child_enable_tunnel_lifecycle_control is not None:
        out["enable_tunnel_lifecycle_control"] = (
            child_enable_tunnel_lifecycle_control.text or ""
        ).lower() == "true"
    return out
