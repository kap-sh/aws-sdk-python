"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRuleGroupAttachment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.insert_position
    import aws_sdk_network_firewall.types.resource_name


class ProxyRuleGroupAttachment(TypedDict):
    proxy_rule_group_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p>"""
    insert_position: NotRequired[
        "aws_sdk_network_firewall.types.insert_position.InsertPosition"
    ]
    """<p>Where to insert a proxy rule group in a proxy configuration. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRuleGroupAttachment) -> dict:
    out: dict = {}
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    if "insert_position" in value:
        out["InsertPosition"] = value["insert_position"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProxyRuleGroupAttachment:
    out: ProxyRuleGroupAttachment = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroupName" in data:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if "InsertPosition" in data:
        out["insert_position"] = data["InsertPosition"]
    return out
