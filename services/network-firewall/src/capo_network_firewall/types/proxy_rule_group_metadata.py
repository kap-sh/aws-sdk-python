"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRuleGroupMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class ProxyRuleGroupMetadata(TypedDict, closed=True):
    name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p>"""
    arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of a proxy rule group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRuleGroupMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProxyRuleGroupMetadata:
    out: ProxyRuleGroupMetadata = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
