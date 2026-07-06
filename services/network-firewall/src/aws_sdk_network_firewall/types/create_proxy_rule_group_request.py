"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateProxyRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.description
    import aws_sdk_network_firewall.types.proxy_rules_by_request_phase
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.tag_list


class CreateProxyRuleGroupRequest(TypedDict, closed=True):
    proxy_rule_group_name: "aws_sdk_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p>"""
    description: NotRequired["aws_sdk_network_firewall.types.description.Description"]
    """<p>A description of the proxy rule group. </p>"""
    rules: NotRequired[
        "aws_sdk_network_firewall.types.proxy_rules_by_request_phase.ProxyRulesByRequestPhase"
    ]
    """<p>Individual rules that define match conditions and actions for application-layer traffic. Rules specify what to inspect (domains, headers, methods) and what action to take (allow, deny, alert). </p>"""
    tags: NotRequired["aws_sdk_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProxyRuleGroupRequest) -> dict:
    out: dict = {}
    out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "rules" in value:
        import aws_sdk_network_firewall.types.proxy_rules_by_request_phase

        out["Rules"] = (
            aws_sdk_network_firewall.types.proxy_rules_by_request_phase.serialize_aws_json_1_0(
                value["rules"]
            )
        )
    if "tags" in value:
        import aws_sdk_network_firewall.types.tag_list

        out["Tags"] = aws_sdk_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProxyRuleGroupRequest:
    out: CreateProxyRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroupName" in data:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    else:
        raise DeserializationError(
            "CreateProxyRuleGroupRequest.proxy_rule_group_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Rules" in data:
        import aws_sdk_network_firewall.types.proxy_rules_by_request_phase

        out["rules"] = (
            aws_sdk_network_firewall.types.proxy_rules_by_request_phase.deserialize_aws_json_1_0(
                data["Rules"]
            )
        )
    if "Tags" in data:
        import aws_sdk_network_firewall.types.tag_list

        out["tags"] = aws_sdk_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
