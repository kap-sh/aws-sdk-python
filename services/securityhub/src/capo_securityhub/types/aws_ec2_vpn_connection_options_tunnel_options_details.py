"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpnConnectionOptionsTunnelOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.integer_list
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsEc2VpnConnectionOptionsTunnelOptionsDetails(TypedDict, closed=True):
    dpd_timeout_seconds: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of seconds after which a Dead Peer Detection (DPD) timeout occurs.</p>"""
    ike_versions: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The Internet Key Exchange (IKE) versions that are permitted for the VPN tunnel.</p>"""
    outside_ip_address: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The external IP address of the VPN tunnel.</p>"""
    phase1_dh_group_numbers: NotRequired[
        "capo_securityhub.types.integer_list.IntegerList"
    ]
    """<p>The permitted Diffie-Hellman group numbers for the VPN tunnel for phase 1 IKE negotiations.</p>"""
    phase1_encryption_algorithms: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The permitted encryption algorithms for the VPN tunnel for phase 1 IKE negotiations.</p>"""
    phase1_integrity_algorithms: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The permitted integrity algorithms for the VPN tunnel for phase 1 IKE negotiations.</p>"""
    phase1_lifetime_seconds: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The lifetime for phase 1 of the IKE negotiation, in seconds.</p>"""
    phase2_dh_group_numbers: NotRequired[
        "capo_securityhub.types.integer_list.IntegerList"
    ]
    """<p>The permitted Diffie-Hellman group numbers for the VPN tunnel for phase 2 IKE negotiations.</p>"""
    phase2_encryption_algorithms: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The permitted encryption algorithms for the VPN tunnel for phase 2 IKE negotiations.</p>"""
    phase2_integrity_algorithms: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The permitted integrity algorithms for the VPN tunnel for phase 2 IKE negotiations.</p>"""
    phase2_lifetime_seconds: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The lifetime for phase 2 of the IKE negotiation, in seconds.</p>"""
    pre_shared_key: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The preshared key to establish initial authentication between the virtual private gateway and the customer gateway.</p>"""
    rekey_fuzz_percentage: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The percentage of the rekey window, which is determined by <code>RekeyMarginTimeSeconds</code> during which the rekey time is randomly selected.</p>"""
    rekey_margin_time_seconds: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The margin time, in seconds, before the phase 2 lifetime expires, during which the Amazon Web Services side of the VPN connection performs an IKE rekey.</p>"""
    replay_window_size: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of packets in an IKE replay window.</p>"""
    tunnel_inside_cidr: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The range of inside IPv4 addresses for the tunnel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpnConnectionOptionsTunnelOptionsDetails) -> dict:
    out: dict = {}
    if "dpd_timeout_seconds" in value:
        out["DpdTimeoutSeconds"] = value["dpd_timeout_seconds"]
    if "ike_versions" in value:
        import capo_securityhub.types.non_empty_string_list

        out["IkeVersions"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["ike_versions"]
            )
        )
    if "outside_ip_address" in value:
        out["OutsideIpAddress"] = value["outside_ip_address"]
    if "phase1_dh_group_numbers" in value:
        import capo_securityhub.types.integer_list

        out["Phase1DhGroupNumbers"] = (
            capo_securityhub.types.integer_list.serialize_json(
                value["phase1_dh_group_numbers"]
            )
        )
    if "phase1_encryption_algorithms" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Phase1EncryptionAlgorithms"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["phase1_encryption_algorithms"]
            )
        )
    if "phase1_integrity_algorithms" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Phase1IntegrityAlgorithms"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["phase1_integrity_algorithms"]
            )
        )
    if "phase1_lifetime_seconds" in value:
        out["Phase1LifetimeSeconds"] = value["phase1_lifetime_seconds"]
    if "phase2_dh_group_numbers" in value:
        import capo_securityhub.types.integer_list

        out["Phase2DhGroupNumbers"] = (
            capo_securityhub.types.integer_list.serialize_json(
                value["phase2_dh_group_numbers"]
            )
        )
    if "phase2_encryption_algorithms" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Phase2EncryptionAlgorithms"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["phase2_encryption_algorithms"]
            )
        )
    if "phase2_integrity_algorithms" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Phase2IntegrityAlgorithms"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["phase2_integrity_algorithms"]
            )
        )
    if "phase2_lifetime_seconds" in value:
        out["Phase2LifetimeSeconds"] = value["phase2_lifetime_seconds"]
    if "pre_shared_key" in value:
        out["PreSharedKey"] = value["pre_shared_key"]
    if "rekey_fuzz_percentage" in value:
        out["RekeyFuzzPercentage"] = value["rekey_fuzz_percentage"]
    if "rekey_margin_time_seconds" in value:
        out["RekeyMarginTimeSeconds"] = value["rekey_margin_time_seconds"]
    if "replay_window_size" in value:
        out["ReplayWindowSize"] = value["replay_window_size"]
    if "tunnel_inside_cidr" in value:
        out["TunnelInsideCidr"] = value["tunnel_inside_cidr"]
    return out


def deserialize_json(data: dict) -> AwsEc2VpnConnectionOptionsTunnelOptionsDetails:
    out: AwsEc2VpnConnectionOptionsTunnelOptionsDetails = {}  # type: ignore[typeddict-item]
    if "DpdTimeoutSeconds" in data:
        out["dpd_timeout_seconds"] = data["DpdTimeoutSeconds"]
    if "IkeVersions" in data:
        import capo_securityhub.types.non_empty_string_list

        out["ike_versions"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["IkeVersions"]
            )
        )
    if "OutsideIpAddress" in data:
        out["outside_ip_address"] = data["OutsideIpAddress"]
    if "Phase1DhGroupNumbers" in data:
        import capo_securityhub.types.integer_list

        out["phase1_dh_group_numbers"] = (
            capo_securityhub.types.integer_list.deserialize_json(
                data["Phase1DhGroupNumbers"]
            )
        )
    if "Phase1EncryptionAlgorithms" in data:
        import capo_securityhub.types.non_empty_string_list

        out["phase1_encryption_algorithms"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["Phase1EncryptionAlgorithms"]
            )
        )
    if "Phase1IntegrityAlgorithms" in data:
        import capo_securityhub.types.non_empty_string_list

        out["phase1_integrity_algorithms"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["Phase1IntegrityAlgorithms"]
            )
        )
    if "Phase1LifetimeSeconds" in data:
        out["phase1_lifetime_seconds"] = data["Phase1LifetimeSeconds"]
    if "Phase2DhGroupNumbers" in data:
        import capo_securityhub.types.integer_list

        out["phase2_dh_group_numbers"] = (
            capo_securityhub.types.integer_list.deserialize_json(
                data["Phase2DhGroupNumbers"]
            )
        )
    if "Phase2EncryptionAlgorithms" in data:
        import capo_securityhub.types.non_empty_string_list

        out["phase2_encryption_algorithms"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["Phase2EncryptionAlgorithms"]
            )
        )
    if "Phase2IntegrityAlgorithms" in data:
        import capo_securityhub.types.non_empty_string_list

        out["phase2_integrity_algorithms"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["Phase2IntegrityAlgorithms"]
            )
        )
    if "Phase2LifetimeSeconds" in data:
        out["phase2_lifetime_seconds"] = data["Phase2LifetimeSeconds"]
    if "PreSharedKey" in data:
        out["pre_shared_key"] = data["PreSharedKey"]
    if "RekeyFuzzPercentage" in data:
        out["rekey_fuzz_percentage"] = data["RekeyFuzzPercentage"]
    if "RekeyMarginTimeSeconds" in data:
        out["rekey_margin_time_seconds"] = data["RekeyMarginTimeSeconds"]
    if "ReplayWindowSize" in data:
        out["replay_window_size"] = data["ReplayWindowSize"]
    if "TunnelInsideCidr" in data:
        out["tunnel_inside_cidr"] = data["TunnelInsideCidr"]
    return out
