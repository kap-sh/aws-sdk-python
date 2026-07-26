"""Generated from Smithy shape ``com.amazonaws.securityhub#Network``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.network_direction
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.port_range


class Network(TypedDict, closed=True):
    direction: NotRequired["capo_securityhub.types.network_direction.NetworkDirection"]
    """<p>The direction of network traffic associated with a finding.</p>"""
    protocol: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The protocol of network-related information about a finding.</p> <p>Length Constraints: Minimum of 1. Maximum of 16.</p>"""
    open_port_range: NotRequired["capo_securityhub.types.port_range.PortRange"]
    """<p>The range of open ports that is present on the network.</p>"""
    source_ip_v4: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The source IPv4 address of network-related information about a finding.</p>"""
    source_ip_v6: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The source IPv6 address of network-related information about a finding.</p>"""
    source_port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The source port of network-related information about a finding.</p>"""
    source_domain: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The source domain of network-related information about a finding.</p> <p>Length Constraints: Minimum of 1. Maximum of 128.</p>"""
    source_mac: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The source media access control (MAC) address of network-related information about a finding.</p>"""
    destination_ip_v4: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The destination IPv4 address of network-related information about a finding.</p>"""
    destination_ip_v6: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The destination IPv6 address of network-related information about a finding.</p>"""
    destination_port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The destination port of network-related information about a finding.</p>"""
    destination_domain: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The destination domain of network-related information about a finding.</p> <p>Length Constraints: Minimum of 1. Maximum of 128.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Network) -> dict:
    out: dict = {}
    if "direction" in value:
        import capo_securityhub.types.network_direction

        out["Direction"] = capo_securityhub.types.network_direction.serialize_json(
            value["direction"]
        )
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "open_port_range" in value:
        import capo_securityhub.types.port_range

        out["OpenPortRange"] = capo_securityhub.types.port_range.serialize_json(
            value["open_port_range"]
        )
    if "source_ip_v4" in value:
        out["SourceIpV4"] = value["source_ip_v4"]
    if "source_ip_v6" in value:
        out["SourceIpV6"] = value["source_ip_v6"]
    if "source_port" in value:
        out["SourcePort"] = value["source_port"]
    if "source_domain" in value:
        out["SourceDomain"] = value["source_domain"]
    if "source_mac" in value:
        out["SourceMac"] = value["source_mac"]
    if "destination_ip_v4" in value:
        out["DestinationIpV4"] = value["destination_ip_v4"]
    if "destination_ip_v6" in value:
        out["DestinationIpV6"] = value["destination_ip_v6"]
    if "destination_port" in value:
        out["DestinationPort"] = value["destination_port"]
    if "destination_domain" in value:
        out["DestinationDomain"] = value["destination_domain"]
    return out


def deserialize_json(data: dict) -> Network:
    out: Network = {}  # type: ignore[typeddict-item]
    if "Direction" in data:
        import capo_securityhub.types.network_direction

        out["direction"] = capo_securityhub.types.network_direction.deserialize_json(
            data["Direction"]
        )
    if "Protocol" in data:
        out["protocol"] = data["Protocol"]
    if "OpenPortRange" in data:
        import capo_securityhub.types.port_range

        out["open_port_range"] = capo_securityhub.types.port_range.deserialize_json(
            data["OpenPortRange"]
        )
    if "SourceIpV4" in data:
        out["source_ip_v4"] = data["SourceIpV4"]
    if "SourceIpV6" in data:
        out["source_ip_v6"] = data["SourceIpV6"]
    if "SourcePort" in data:
        out["source_port"] = data["SourcePort"]
    if "SourceDomain" in data:
        out["source_domain"] = data["SourceDomain"]
    if "SourceMac" in data:
        out["source_mac"] = data["SourceMac"]
    if "DestinationIpV4" in data:
        out["destination_ip_v4"] = data["DestinationIpV4"]
    if "DestinationIpV6" in data:
        out["destination_ip_v6"] = data["DestinationIpV6"]
    if "DestinationPort" in data:
        out["destination_port"] = data["DestinationPort"]
    if "DestinationDomain" in data:
        out["destination_domain"] = data["DestinationDomain"]
    return out
