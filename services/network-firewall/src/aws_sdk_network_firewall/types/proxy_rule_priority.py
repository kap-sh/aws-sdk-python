"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRulePriority``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.insert_position
    import aws_sdk_network_firewall.types.resource_name


class ProxyRulePriority(TypedDict):
    proxy_rule_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule. You can't change the name of a proxy rule after you create it.</p>"""
    new_position: NotRequired[
        "aws_sdk_network_firewall.types.insert_position.InsertPosition"
    ]
    """<p>Where to move a proxy rule in a proxy rule group. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRulePriority) -> dict:
    out: dict = {}
    if "proxy_rule_name" in value:
        out["ProxyRuleName"] = value["proxy_rule_name"]
    if "new_position" in value:
        out["NewPosition"] = value["new_position"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProxyRulePriority:
    out: ProxyRulePriority = {}  # type: ignore[typeddict-item]
    if "ProxyRuleName" in data:
        out["proxy_rule_name"] = data["ProxyRuleName"]
    if "NewPosition" in data:
        out["new_position"] = data["NewPosition"]
    return out
