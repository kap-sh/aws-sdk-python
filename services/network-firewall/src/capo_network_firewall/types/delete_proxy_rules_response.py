"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteProxyRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_rule_group


class DeleteProxyRulesResponse(TypedDict, closed=True):
    proxy_rule_group: NotRequired[
        "capo_network_firewall.types.proxy_rule_group.ProxyRuleGroup"
    ]
    """<p>The properties that define the proxy rule group with the newly created proxy rule(s). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteProxyRulesResponse) -> dict:
    out: dict = {}
    if "proxy_rule_group" in value:
        import capo_network_firewall.types.proxy_rule_group

        out["ProxyRuleGroup"] = (
            capo_network_firewall.types.proxy_rule_group.serialize_aws_json_1_0(
                value["proxy_rule_group"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteProxyRulesResponse:
    out: DeleteProxyRulesResponse = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroup" in data:
        import capo_network_firewall.types.proxy_rule_group

        out["proxy_rule_group"] = (
            capo_network_firewall.types.proxy_rule_group.deserialize_aws_json_1_0(
                data["ProxyRuleGroup"]
            )
        )
    return out
