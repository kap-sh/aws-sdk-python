"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.create_time
    import aws_sdk_network_firewall.types.delete_time
    import aws_sdk_network_firewall.types.description
    import aws_sdk_network_firewall.types.proxy_config_default_rule_phase_actions_request
    import aws_sdk_network_firewall.types.proxy_config_rule_group_set
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.tag_list


class ProxyConfiguration(TypedDict, closed=True):
    proxy_configuration_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p>"""
    proxy_configuration_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy configuration.</p>"""
    description: NotRequired["aws_sdk_network_firewall.types.description.Description"]
    """<p>A description of the proxy configuration. </p>"""
    create_time: NotRequired["aws_sdk_network_firewall.types.create_time.CreateTime"]
    """<p>Time the Proxy Configuration was created. </p>"""
    delete_time: NotRequired["aws_sdk_network_firewall.types.delete_time.DeleteTime"]
    """<p>Time the Proxy Configuration was deleted. </p>"""
    rule_groups: NotRequired[
        "aws_sdk_network_firewall.types.proxy_config_rule_group_set.ProxyConfigRuleGroupSet"
    ]
    """<p>Proxy rule groups within the proxy configuration. </p>"""
    default_rule_phase_actions: NotRequired[
        "aws_sdk_network_firewall.types.proxy_config_default_rule_phase_actions_request.ProxyConfigDefaultRulePhaseActionsRequest"
    ]
    """<p>Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied. </p> <p>Pre-DNS - before domain resolution.</p> <p>Pre-Request - after DNS, before request.</p> <p>Post-Response - after receiving response.</p>"""
    tags: NotRequired["aws_sdk_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyConfiguration) -> dict:
    out: dict = {}
    if "proxy_configuration_name" in value:
        out["ProxyConfigurationName"] = value["proxy_configuration_name"]
    if "proxy_configuration_arn" in value:
        out["ProxyConfigurationArn"] = value["proxy_configuration_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "create_time" in value:
        import aws_sdk_network_firewall.types.create_time

        out["CreateTime"] = (
            aws_sdk_network_firewall.types.create_time.serialize_aws_json_1_0(
                value["create_time"]
            )
        )
    if "delete_time" in value:
        import aws_sdk_network_firewall.types.delete_time

        out["DeleteTime"] = (
            aws_sdk_network_firewall.types.delete_time.serialize_aws_json_1_0(
                value["delete_time"]
            )
        )
    if "rule_groups" in value:
        import aws_sdk_network_firewall.types.proxy_config_rule_group_set

        out["RuleGroups"] = (
            aws_sdk_network_firewall.types.proxy_config_rule_group_set.serialize_aws_json_1_0(
                value["rule_groups"]
            )
        )
    if "default_rule_phase_actions" in value:
        import aws_sdk_network_firewall.types.proxy_config_default_rule_phase_actions_request

        out["DefaultRulePhaseActions"] = (
            aws_sdk_network_firewall.types.proxy_config_default_rule_phase_actions_request.serialize_aws_json_1_0(
                value["default_rule_phase_actions"]
            )
        )
    if "tags" in value:
        import aws_sdk_network_firewall.types.tag_list

        out["Tags"] = aws_sdk_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProxyConfiguration:
    out: ProxyConfiguration = {}  # type: ignore[typeddict-item]
    if "ProxyConfigurationName" in data:
        out["proxy_configuration_name"] = data["ProxyConfigurationName"]
    if "ProxyConfigurationArn" in data:
        out["proxy_configuration_arn"] = data["ProxyConfigurationArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreateTime" in data:
        import aws_sdk_network_firewall.types.create_time

        out["create_time"] = (
            aws_sdk_network_firewall.types.create_time.deserialize_aws_json_1_0(
                data["CreateTime"]
            )
        )
    if "DeleteTime" in data:
        import aws_sdk_network_firewall.types.delete_time

        out["delete_time"] = (
            aws_sdk_network_firewall.types.delete_time.deserialize_aws_json_1_0(
                data["DeleteTime"]
            )
        )
    if "RuleGroups" in data:
        import aws_sdk_network_firewall.types.proxy_config_rule_group_set

        out["rule_groups"] = (
            aws_sdk_network_firewall.types.proxy_config_rule_group_set.deserialize_aws_json_1_0(
                data["RuleGroups"]
            )
        )
    if "DefaultRulePhaseActions" in data:
        import aws_sdk_network_firewall.types.proxy_config_default_rule_phase_actions_request

        out["default_rule_phase_actions"] = (
            aws_sdk_network_firewall.types.proxy_config_default_rule_phase_actions_request.deserialize_aws_json_1_0(
                data["DefaultRulePhaseActions"]
            )
        )
    if "Tags" in data:
        import aws_sdk_network_firewall.types.tag_list

        out["tags"] = aws_sdk_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
