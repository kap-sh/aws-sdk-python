"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRuleGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.create_time
    import capo_network_firewall.types.delete_time
    import capo_network_firewall.types.description
    import capo_network_firewall.types.proxy_rules_by_request_phase
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.tag_list


class ProxyRuleGroup(TypedDict, closed=True):
    proxy_rule_group_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p>"""
    proxy_rule_group_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy rule group.</p>"""
    create_time: NotRequired["capo_network_firewall.types.create_time.CreateTime"]
    """<p>Time the Proxy Rule Group was created. </p>"""
    delete_time: NotRequired["capo_network_firewall.types.delete_time.DeleteTime"]
    """<p>Time the Proxy Rule Group was deleted. </p>"""
    rules: NotRequired[
        "capo_network_firewall.types.proxy_rules_by_request_phase.ProxyRulesByRequestPhase"
    ]
    """<p>Individual rules that define match conditions and actions for application-layer traffic. Rules specify what to inspect (domains, headers, methods) and what action to take (allow, deny, alert). </p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the proxy rule group. </p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRuleGroup) -> dict:
    out: dict = {}
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    if "proxy_rule_group_arn" in value:
        out["ProxyRuleGroupArn"] = value["proxy_rule_group_arn"]
    if "create_time" in value:
        import capo_network_firewall.types.create_time

        out["CreateTime"] = (
            capo_network_firewall.types.create_time.serialize_aws_json_1_0(
                value["create_time"]
            )
        )
    if "delete_time" in value:
        import capo_network_firewall.types.delete_time

        out["DeleteTime"] = (
            capo_network_firewall.types.delete_time.serialize_aws_json_1_0(
                value["delete_time"]
            )
        )
    if "rules" in value:
        import capo_network_firewall.types.proxy_rules_by_request_phase

        out["Rules"] = (
            capo_network_firewall.types.proxy_rules_by_request_phase.serialize_aws_json_1_0(
                value["rules"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProxyRuleGroup:
    out: ProxyRuleGroup = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroupName" in data:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if "ProxyRuleGroupArn" in data:
        out["proxy_rule_group_arn"] = data["ProxyRuleGroupArn"]
    if "CreateTime" in data:
        import capo_network_firewall.types.create_time

        out["create_time"] = (
            capo_network_firewall.types.create_time.deserialize_aws_json_1_0(
                data["CreateTime"]
            )
        )
    if "DeleteTime" in data:
        import capo_network_firewall.types.delete_time

        out["delete_time"] = (
            capo_network_firewall.types.delete_time.deserialize_aws_json_1_0(
                data["DeleteTime"]
            )
        )
    if "Rules" in data:
        import capo_network_firewall.types.proxy_rules_by_request_phase

        out["rules"] = (
            capo_network_firewall.types.proxy_rules_by_request_phase.deserialize_aws_json_1_0(
                data["Rules"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
