"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRuleGroupPriority``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.insert_position
    import aws_sdk_network_firewall.types.resource_name


class ProxyRuleGroupPriority(TypedDict, closed=True):
    proxy_rule_group_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p>"""
    new_position: NotRequired[
        "aws_sdk_network_firewall.types.insert_position.InsertPosition"
    ]
    """<p>Where to move a proxy rule group in a proxy configuration. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRuleGroupPriority) -> dict:
    out: dict = {}
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    if "new_position" in value:
        out["NewPosition"] = value["new_position"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProxyRuleGroupPriority:
    out: ProxyRuleGroupPriority = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroupName" in data:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if "NewPosition" in data:
        out["new_position"] = data["NewPosition"]
    return out
