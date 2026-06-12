"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PolicyVariables``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.ip_sets


class PolicyVariables(TypedDict):
    rule_variables: NotRequired["aws_sdk_network_firewall.types.ip_sets.IPSets"]
    """<p>The IPv4 or IPv6 addresses in CIDR notation to use for the Suricata <code>HOME_NET</code> variable. If your firewall uses an inspection VPC, you might want to override the <code>HOME_NET</code> variable with the CIDRs of your home networks. If you don't override <code>HOME_NET</code> with your own CIDRs, Network Firewall by default uses the CIDR of your inspection VPC.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyVariables) -> dict:
    out: dict = {}
    if "rule_variables" in value:
        import aws_sdk_network_firewall.types.ip_sets

        out["RuleVariables"] = (
            aws_sdk_network_firewall.types.ip_sets.serialize_aws_json_1_0(
                value["rule_variables"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PolicyVariables:
    out: PolicyVariables = {}  # type: ignore[typeddict-item]
    if "RuleVariables" in data:
        import aws_sdk_network_firewall.types.ip_sets

        out["rule_variables"] = (
            aws_sdk_network_firewall.types.ip_sets.deserialize_aws_json_1_0(
                data["RuleVariables"]
            )
        )
    return out
