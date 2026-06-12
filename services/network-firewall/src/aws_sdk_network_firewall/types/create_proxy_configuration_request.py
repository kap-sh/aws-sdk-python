"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateProxyConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.description
    import aws_sdk_network_firewall.types.proxy_config_default_rule_phase_actions_request
    import aws_sdk_network_firewall.types.resource_arn_list
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.resource_name_list
    import aws_sdk_network_firewall.types.tag_list


class CreateProxyConfigurationRequest(TypedDict):
    proxy_configuration_name: (
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    )
    """<p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p>"""
    description: NotRequired["aws_sdk_network_firewall.types.description.Description"]
    """<p>A description of the proxy configuration. </p>"""
    rule_group_names: NotRequired[
        "aws_sdk_network_firewall.types.resource_name_list.ResourceNameList"
    ]
    """<p>The proxy rule group name(s) to attach to the proxy configuration.</p> <p>You must specify the ARNs or the names, and you can specify both. </p>"""
    rule_group_arns: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn_list.ResourceArnList"
    ]
    """<p>The proxy rule group arn(s) to attach to the proxy configuration.</p> <p>You must specify the ARNs or the names, and you can specify both. </p>"""
    default_rule_phase_actions: "aws_sdk_network_firewall.types.proxy_config_default_rule_phase_actions_request.ProxyConfigDefaultRulePhaseActionsRequest"
    """<p>Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied. </p>"""
    tags: NotRequired["aws_sdk_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProxyConfigurationRequest) -> dict:
    out: dict = {}
    out["ProxyConfigurationName"] = value["proxy_configuration_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "rule_group_names" in value:
        import aws_sdk_network_firewall.types.resource_name_list

        out["RuleGroupNames"] = (
            aws_sdk_network_firewall.types.resource_name_list.serialize_aws_json_1_0(
                value["rule_group_names"]
            )
        )
    if "rule_group_arns" in value:
        import aws_sdk_network_firewall.types.resource_arn_list

        out["RuleGroupArns"] = (
            aws_sdk_network_firewall.types.resource_arn_list.serialize_aws_json_1_0(
                value["rule_group_arns"]
            )
        )
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


def deserialize_aws_json_1_0(data: dict) -> CreateProxyConfigurationRequest:
    out: CreateProxyConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ProxyConfigurationName" in data:
        out["proxy_configuration_name"] = data["ProxyConfigurationName"]
    else:
        raise DeserializationError(
            "CreateProxyConfigurationRequest.proxy_configuration_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "RuleGroupNames" in data:
        import aws_sdk_network_firewall.types.resource_name_list

        out["rule_group_names"] = (
            aws_sdk_network_firewall.types.resource_name_list.deserialize_aws_json_1_0(
                data["RuleGroupNames"]
            )
        )
    if "RuleGroupArns" in data:
        import aws_sdk_network_firewall.types.resource_arn_list

        out["rule_group_arns"] = (
            aws_sdk_network_firewall.types.resource_arn_list.deserialize_aws_json_1_0(
                data["RuleGroupArns"]
            )
        )
    if "DefaultRulePhaseActions" in data:
        import aws_sdk_network_firewall.types.proxy_config_default_rule_phase_actions_request

        out["default_rule_phase_actions"] = (
            aws_sdk_network_firewall.types.proxy_config_default_rule_phase_actions_request.deserialize_aws_json_1_0(
                data["DefaultRulePhaseActions"]
            )
        )
    else:
        raise DeserializationError(
            "CreateProxyConfigurationRequest.default_rule_phase_actions required"
        )
    if "Tags" in data:
        import aws_sdk_network_firewall.types.tag_list

        out["tags"] = aws_sdk_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
