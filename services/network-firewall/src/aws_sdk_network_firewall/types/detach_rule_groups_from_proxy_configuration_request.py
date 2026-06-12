"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DetachRuleGroupsFromProxyConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_arn_list
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.resource_name_list
    import aws_sdk_network_firewall.types.update_token


class DetachRuleGroupsFromProxyConfigurationRequest(TypedDict):
    proxy_configuration_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_configuration_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    rule_group_names: NotRequired[
        "aws_sdk_network_firewall.types.resource_name_list.ResourceNameList"
    ]
    """<p>The proxy rule group names to detach from the proxy configuration</p>"""
    rule_group_arns: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn_list.ResourceArnList"
    ]
    """<p>The proxy rule group arns to detach from the proxy configuration</p>"""
    update_token: "aws_sdk_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy configuration. The token marks the state of the proxy configuration resource at the time of the request. </p> <p>To make changes to the proxy configuration, you provide the token in your request. Network Firewall uses the token to ensure that the proxy configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: DetachRuleGroupsFromProxyConfigurationRequest,
) -> dict:
    out: dict = {}
    if "proxy_configuration_name" in value:
        out["ProxyConfigurationName"] = value["proxy_configuration_name"]
    if "proxy_configuration_arn" in value:
        out["ProxyConfigurationArn"] = value["proxy_configuration_arn"]
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
    out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> DetachRuleGroupsFromProxyConfigurationRequest:
    out: DetachRuleGroupsFromProxyConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ProxyConfigurationName" in data:
        out["proxy_configuration_name"] = data["ProxyConfigurationName"]
    if "ProxyConfigurationArn" in data:
        out["proxy_configuration_arn"] = data["ProxyConfigurationArn"]
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
    if "UpdateToken" in data:
        out["update_token"] = data["UpdateToken"]
    else:
        raise DeserializationError(
            "DetachRuleGroupsFromProxyConfigurationRequest.update_token required"
        )
    return out
