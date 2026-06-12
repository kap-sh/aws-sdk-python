"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteProxyRulesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.proxy_rule_group


class DeleteProxyRulesResponse(TypedDict):
    proxy_rule_group: NotRequired[
        "aws_sdk_network_firewall.types.proxy_rule_group.ProxyRuleGroup"
    ]
    """<p>The properties that define the proxy rule group with the newly created proxy rule(s). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteProxyRulesResponse) -> dict:
    out: dict = {}
    if "proxy_rule_group" in value:
        import aws_sdk_network_firewall.types.proxy_rule_group

        out["ProxyRuleGroup"] = (
            aws_sdk_network_firewall.types.proxy_rule_group.serialize_aws_json_1_0(
                value["proxy_rule_group"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteProxyRulesResponse:
    out: DeleteProxyRulesResponse = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroup" in data:
        import aws_sdk_network_firewall.types.proxy_rule_group

        out["proxy_rule_group"] = (
            aws_sdk_network_firewall.types.proxy_rule_group.deserialize_aws_json_1_0(
                data["ProxyRuleGroup"]
            )
        )
    return out
