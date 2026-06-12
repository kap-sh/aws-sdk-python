"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateProxyRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.create_proxy_rules_by_request_phase
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name


class CreateProxyRulesRequest(TypedDict):
    proxy_rule_group_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_rule_group_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    rules: "aws_sdk_network_firewall.types.create_proxy_rules_by_request_phase.CreateProxyRulesByRequestPhase"
    """<p>Individual rules that define match conditions and actions for application-layer traffic. Rules specify what to inspect (domains, headers, methods) and what action to take (allow, deny, alert). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProxyRulesRequest) -> dict:
    out: dict = {}
    if "proxy_rule_group_arn" in value:
        out["ProxyRuleGroupArn"] = value["proxy_rule_group_arn"]
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    import aws_sdk_network_firewall.types.create_proxy_rules_by_request_phase

    out["Rules"] = (
        aws_sdk_network_firewall.types.create_proxy_rules_by_request_phase.serialize_aws_json_1_0(
            value["rules"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProxyRulesRequest:
    out: CreateProxyRulesRequest = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroupArn" in data:
        out["proxy_rule_group_arn"] = data["ProxyRuleGroupArn"]
    if "ProxyRuleGroupName" in data:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if "Rules" in data:
        import aws_sdk_network_firewall.types.create_proxy_rules_by_request_phase

        out["rules"] = (
            aws_sdk_network_firewall.types.create_proxy_rules_by_request_phase.deserialize_aws_json_1_0(
                data["Rules"]
            )
        )
    else:
        raise DeserializationError("CreateProxyRulesRequest.rules required")
    return out
