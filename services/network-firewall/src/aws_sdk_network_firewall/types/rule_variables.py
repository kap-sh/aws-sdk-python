"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleVariables``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.ip_sets
    import aws_sdk_network_firewall.types.port_sets


class RuleVariables(TypedDict):
    ip_sets: NotRequired["aws_sdk_network_firewall.types.ip_sets.IPSets"]
    """<p>A list of IP addresses and address ranges, in CIDR notation. </p>"""
    port_sets: NotRequired["aws_sdk_network_firewall.types.port_sets.PortSets"]
    """<p>A list of port ranges. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleVariables) -> dict:
    out: dict = {}
    if "ip_sets" in value:
        import aws_sdk_network_firewall.types.ip_sets

        out["IPSets"] = aws_sdk_network_firewall.types.ip_sets.serialize_aws_json_1_0(
            value["ip_sets"]
        )
    if "port_sets" in value:
        import aws_sdk_network_firewall.types.port_sets

        out["PortSets"] = (
            aws_sdk_network_firewall.types.port_sets.serialize_aws_json_1_0(
                value["port_sets"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleVariables:
    out: RuleVariables = {}  # type: ignore[typeddict-item]
    if "IPSets" in data:
        import aws_sdk_network_firewall.types.ip_sets

        out["ip_sets"] = (
            aws_sdk_network_firewall.types.ip_sets.deserialize_aws_json_1_0(
                data["IPSets"]
            )
        )
    if "PortSets" in data:
        import aws_sdk_network_firewall.types.port_sets

        out["port_sets"] = (
            aws_sdk_network_firewall.types.port_sets.deserialize_aws_json_1_0(
                data["PortSets"]
            )
        )
    return out
