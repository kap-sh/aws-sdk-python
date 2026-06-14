"""Generated from Smithy shape ``com.amazonaws.wafv2#WebACL``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.application_config
    import aws_sdk_wafv2.types.association_config
    import aws_sdk_wafv2.types.boolean
    import aws_sdk_wafv2.types.captcha_config
    import aws_sdk_wafv2.types.challenge_config
    import aws_sdk_wafv2.types.consumed_capacity
    import aws_sdk_wafv2.types.custom_response_bodies
    import aws_sdk_wafv2.types.data_protection_config
    import aws_sdk_wafv2.types.default_action
    import aws_sdk_wafv2.types.entity_description
    import aws_sdk_wafv2.types.entity_id
    import aws_sdk_wafv2.types.entity_name
    import aws_sdk_wafv2.types.firewall_manager_rule_groups
    import aws_sdk_wafv2.types.label_name
    import aws_sdk_wafv2.types.on_source_d_do_s_protection_config
    import aws_sdk_wafv2.types.resource_arn
    import aws_sdk_wafv2.types.rules
    import aws_sdk_wafv2.types.token_domains
    import aws_sdk_wafv2.types.visibility_config


class WebACL(TypedDict):
    name: "aws_sdk_wafv2.types.entity_name.EntityName"
    """<p>The name of the web ACL. You cannot change the name of a web ACL after you create it.</p>"""
    id: "aws_sdk_wafv2.types.entity_id.EntityId"
    """<p>A unique identifier for the <code>WebACL</code>. This ID is returned in the responses to create and list commands. You use this ID to do things like get, update, and delete a <code>WebACL</code>.</p>"""
    arn: "aws_sdk_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web ACL that you want to associate with the resource.</p>"""
    default_action: "aws_sdk_wafv2.types.default_action.DefaultAction"
    """<p>The action to perform if none of the <code>Rules</code> contained in the <code>WebACL</code> match. </p>"""
    description: NotRequired["aws_sdk_wafv2.types.entity_description.EntityDescription"]
    """<p>A description of the web ACL that helps with identification. </p>"""
    rules: NotRequired["aws_sdk_wafv2.types.rules.Rules"]
    """<p>The <a>Rule</a> statements used to identify the web requests that you want to manage. Each rule includes one top-level statement that WAF uses to identify matching web requests, and parameters that govern how WAF handles them. </p>"""
    visibility_config: "aws_sdk_wafv2.types.visibility_config.VisibilityConfig"
    """<p>Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>"""
    data_protection_config: NotRequired[
        "aws_sdk_wafv2.types.data_protection_config.DataProtectionConfig"
    ]
    """<p>Specifies data protection to apply to the web request data for the web ACL. This is a web ACL level data protection option. </p> <p>The data protection that you configure for the web ACL alters the data that's available for any other data collection activity, including your WAF logging destinations, web ACL request sampling, and Amazon Security Lake data collection and management. Your other option for data protection is in the logging configuration, which only affects logging. </p>"""
    capacity: "aws_sdk_wafv2.types.consumed_capacity.ConsumedCapacity"
    r"""<p>The web ACL capacity units (WCUs) currently being used by this web ACL. </p> <p>WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html\">WAF web ACL capacity units (WCU)</a> in the <i>WAF Developer Guide</i>. </p>"""
    pre_process_firewall_manager_rule_groups: NotRequired[
        "aws_sdk_wafv2.types.firewall_manager_rule_groups.FirewallManagerRuleGroups"
    ]
    """<p>The first set of rules for WAF to process in the web ACL. This is defined in an Firewall Manager WAF policy and contains only rule group references. You can't alter these. Any rules and rule groups that you define for the web ACL are prioritized after these. </p> <p>In the Firewall Manager WAF policy, the Firewall Manager administrator can define a set of rule groups to run first in the web ACL and a set of rule groups to run last. Within each set, the administrator prioritizes the rule groups, to determine their relative processing order.</p>"""
    post_process_firewall_manager_rule_groups: NotRequired[
        "aws_sdk_wafv2.types.firewall_manager_rule_groups.FirewallManagerRuleGroups"
    ]
    """<p>The last set of rules for WAF to process in the web ACL. This is defined in an Firewall Manager WAF policy and contains only rule group references. You can't alter these. Any rules and rule groups that you define for the web ACL are prioritized before these. </p> <p>In the Firewall Manager WAF policy, the Firewall Manager administrator can define a set of rule groups to run first in the web ACL and a set of rule groups to run last. Within each set, the administrator prioritizes the rule groups, to determine their relative processing order.</p>"""
    managed_by_firewall_manager: "aws_sdk_wafv2.types.boolean.Boolean"
    """<p>Indicates whether this web ACL was created by Firewall Manager and is being managed by Firewall Manager. If true, then only Firewall Manager can delete the web ACL or any Firewall Manager rule groups in the web ACL. See also the properties <code>RetrofittedByFirewallManager</code>, <code>PreProcessFirewallManagerRuleGroups</code>, and <code>PostProcessFirewallManagerRuleGroups</code>. </p>"""
    label_namespace: NotRequired["aws_sdk_wafv2.types.label_name.LabelName"]
    """<p>The label namespace prefix for this web ACL. All labels added by rules in this web ACL have this prefix. </p> <ul> <li> <p>The syntax for the label namespace prefix for a web ACL is the following: </p> <p> <code>awswaf:<account ID>:webacl:<web ACL name>:</code> </p> </li> <li> <p>When a rule with a label matches a web request, WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon: </p> <p> <code><label namespace>:<label from rule></code> </p> </li> </ul>"""
    custom_response_bodies: NotRequired[
        "aws_sdk_wafv2.types.custom_response_bodies.CustomResponseBodies"
    ]
    r"""<p>A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the web ACL, and then use them in the rules and default actions that you define in the web ACL. </p> <p>For information about customizing web requests and responses, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html\">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide</i>. </p> <p>For information about the limits on count and size for custom request and response settings, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/limits.html\">WAF quotas</a> in the <i>WAF Developer Guide</i>. </p>"""
    captcha_config: NotRequired["aws_sdk_wafv2.types.captcha_config.CaptchaConfig"]
    """<p>Specifies how WAF should handle <code>CAPTCHA</code> evaluations for rules that don't have their own <code>CaptchaConfig</code> settings. If you don't specify this, WAF uses its default settings for <code>CaptchaConfig</code>. </p>"""
    challenge_config: NotRequired[
        "aws_sdk_wafv2.types.challenge_config.ChallengeConfig"
    ]
    """<p>Specifies how WAF should handle challenge evaluations for rules that don't have their own <code>ChallengeConfig</code> settings. If you don't specify this, WAF uses its default settings for <code>ChallengeConfig</code>. </p>"""
    token_domains: NotRequired["aws_sdk_wafv2.types.token_domains.TokenDomains"]
    """<p>Specifies the domains that WAF should accept in a web request token. This enables the use of tokens across multiple protected websites. When WAF provides a token, it uses the domain of the Amazon Web Services resource that the web ACL is protecting. If you don't specify a list of token domains, WAF accepts tokens only for the domain of the protected resource. With a token domain list, WAF accepts the resource's host domain plus all domains in the token domain list, including their prefixed subdomains.</p>"""
    association_config: NotRequired[
        "aws_sdk_wafv2.types.association_config.AssociationConfig"
    ]
    r"""<p>Specifies custom configurations for the associations between the web ACL and protected resources. </p> <p>Use this to customize the maximum size of the request body that your protected resources forward to WAF for inspection. You can customize this setting for CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access resources. The default setting is 16 KB (16,384 bytes). </p> <note> <p>You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see <a href=\"http://aws.amazon.com/waf/pricing/\">WAF Pricing</a>.</p> </note> <p>For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).</p>"""
    retrofitted_by_firewall_manager: "aws_sdk_wafv2.types.boolean.Boolean"
    """<p>Indicates whether this web ACL was created by a customer account and then retrofitted by Firewall Manager. If true, then the web ACL is currently being managed by a Firewall Manager WAF policy, and only Firewall Manager can manage any Firewall Manager rule groups in the web ACL. See also the properties <code>ManagedByFirewallManager</code>, <code>PreProcessFirewallManagerRuleGroups</code>, and <code>PostProcessFirewallManagerRuleGroups</code>. </p>"""
    on_source_d_do_s_protection_config: NotRequired[
        "aws_sdk_wafv2.types.on_source_d_do_s_protection_config.OnSourceDDoSProtectionConfig"
    ]
    """<p>Configures the level of DDoS protection that applies to web ACLs associated with Application Load Balancers.</p>"""
    application_config: NotRequired[
        "aws_sdk_wafv2.types.application_config.ApplicationConfig"
    ]
    """<p>Returns a list of <code>ApplicationAttribute</code>s.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebACL) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    out["ARN"] = value["arn"]
    import aws_sdk_wafv2.types.default_action

    out["DefaultAction"] = aws_sdk_wafv2.types.default_action.serialize_aws_json_1_1(
        value["default_action"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "rules" in value:
        import aws_sdk_wafv2.types.rules

        out["Rules"] = aws_sdk_wafv2.types.rules.serialize_aws_json_1_1(value["rules"])
    import aws_sdk_wafv2.types.visibility_config

    out["VisibilityConfig"] = (
        aws_sdk_wafv2.types.visibility_config.serialize_aws_json_1_1(
            value["visibility_config"]
        )
    )
    if "data_protection_config" in value:
        import aws_sdk_wafv2.types.data_protection_config

        out["DataProtectionConfig"] = (
            aws_sdk_wafv2.types.data_protection_config.serialize_aws_json_1_1(
                value["data_protection_config"]
            )
        )
    out["Capacity"] = value.get("capacity", 0)
    if "pre_process_firewall_manager_rule_groups" in value:
        import aws_sdk_wafv2.types.firewall_manager_rule_groups

        out["PreProcessFirewallManagerRuleGroups"] = (
            aws_sdk_wafv2.types.firewall_manager_rule_groups.serialize_aws_json_1_1(
                value["pre_process_firewall_manager_rule_groups"]
            )
        )
    if "post_process_firewall_manager_rule_groups" in value:
        import aws_sdk_wafv2.types.firewall_manager_rule_groups

        out["PostProcessFirewallManagerRuleGroups"] = (
            aws_sdk_wafv2.types.firewall_manager_rule_groups.serialize_aws_json_1_1(
                value["post_process_firewall_manager_rule_groups"]
            )
        )
    out["ManagedByFirewallManager"] = value.get("managed_by_firewall_manager", False)
    if "label_namespace" in value:
        out["LabelNamespace"] = value["label_namespace"]
    if "custom_response_bodies" in value:
        import aws_sdk_wafv2.types.custom_response_bodies

        out["CustomResponseBodies"] = (
            aws_sdk_wafv2.types.custom_response_bodies.serialize_aws_json_1_1(
                value["custom_response_bodies"]
            )
        )
    if "captcha_config" in value:
        import aws_sdk_wafv2.types.captcha_config

        out["CaptchaConfig"] = (
            aws_sdk_wafv2.types.captcha_config.serialize_aws_json_1_1(
                value["captcha_config"]
            )
        )
    if "challenge_config" in value:
        import aws_sdk_wafv2.types.challenge_config

        out["ChallengeConfig"] = (
            aws_sdk_wafv2.types.challenge_config.serialize_aws_json_1_1(
                value["challenge_config"]
            )
        )
    if "token_domains" in value:
        import aws_sdk_wafv2.types.token_domains

        out["TokenDomains"] = aws_sdk_wafv2.types.token_domains.serialize_aws_json_1_1(
            value["token_domains"]
        )
    if "association_config" in value:
        import aws_sdk_wafv2.types.association_config

        out["AssociationConfig"] = (
            aws_sdk_wafv2.types.association_config.serialize_aws_json_1_1(
                value["association_config"]
            )
        )
    out["RetrofittedByFirewallManager"] = value.get(
        "retrofitted_by_firewall_manager", False
    )
    if "on_source_d_do_s_protection_config" in value:
        import aws_sdk_wafv2.types.on_source_d_do_s_protection_config

        out["OnSourceDDoSProtectionConfig"] = (
            aws_sdk_wafv2.types.on_source_d_do_s_protection_config.serialize_aws_json_1_1(
                value["on_source_d_do_s_protection_config"]
            )
        )
    if "application_config" in value:
        import aws_sdk_wafv2.types.application_config

        out["ApplicationConfig"] = (
            aws_sdk_wafv2.types.application_config.serialize_aws_json_1_1(
                value["application_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WebACL:
    out: WebACL = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("WebACL.name required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("WebACL.id required")
    if "ARN" in data:
        out["arn"] = data["ARN"]
    else:
        raise DeserializationError("WebACL.arn required")
    if "DefaultAction" in data:
        import aws_sdk_wafv2.types.default_action

        out["default_action"] = (
            aws_sdk_wafv2.types.default_action.deserialize_aws_json_1_1(
                data["DefaultAction"]
            )
        )
    else:
        raise DeserializationError("WebACL.default_action required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Rules" in data:
        import aws_sdk_wafv2.types.rules

        out["rules"] = aws_sdk_wafv2.types.rules.deserialize_aws_json_1_1(data["Rules"])
    if "VisibilityConfig" in data:
        import aws_sdk_wafv2.types.visibility_config

        out["visibility_config"] = (
            aws_sdk_wafv2.types.visibility_config.deserialize_aws_json_1_1(
                data["VisibilityConfig"]
            )
        )
    else:
        raise DeserializationError("WebACL.visibility_config required")
    if "DataProtectionConfig" in data:
        import aws_sdk_wafv2.types.data_protection_config

        out["data_protection_config"] = (
            aws_sdk_wafv2.types.data_protection_config.deserialize_aws_json_1_1(
                data["DataProtectionConfig"]
            )
        )
    if "Capacity" in data:
        out["capacity"] = data["Capacity"]
    else:
        out["capacity"] = 0
    if "PreProcessFirewallManagerRuleGroups" in data:
        import aws_sdk_wafv2.types.firewall_manager_rule_groups

        out["pre_process_firewall_manager_rule_groups"] = (
            aws_sdk_wafv2.types.firewall_manager_rule_groups.deserialize_aws_json_1_1(
                data["PreProcessFirewallManagerRuleGroups"]
            )
        )
    if "PostProcessFirewallManagerRuleGroups" in data:
        import aws_sdk_wafv2.types.firewall_manager_rule_groups

        out["post_process_firewall_manager_rule_groups"] = (
            aws_sdk_wafv2.types.firewall_manager_rule_groups.deserialize_aws_json_1_1(
                data["PostProcessFirewallManagerRuleGroups"]
            )
        )
    if "ManagedByFirewallManager" in data:
        out["managed_by_firewall_manager"] = data["ManagedByFirewallManager"]
    else:
        out["managed_by_firewall_manager"] = False
    if "LabelNamespace" in data:
        out["label_namespace"] = data["LabelNamespace"]
    if "CustomResponseBodies" in data:
        import aws_sdk_wafv2.types.custom_response_bodies

        out["custom_response_bodies"] = (
            aws_sdk_wafv2.types.custom_response_bodies.deserialize_aws_json_1_1(
                data["CustomResponseBodies"]
            )
        )
    if "CaptchaConfig" in data:
        import aws_sdk_wafv2.types.captcha_config

        out["captcha_config"] = (
            aws_sdk_wafv2.types.captcha_config.deserialize_aws_json_1_1(
                data["CaptchaConfig"]
            )
        )
    if "ChallengeConfig" in data:
        import aws_sdk_wafv2.types.challenge_config

        out["challenge_config"] = (
            aws_sdk_wafv2.types.challenge_config.deserialize_aws_json_1_1(
                data["ChallengeConfig"]
            )
        )
    if "TokenDomains" in data:
        import aws_sdk_wafv2.types.token_domains

        out["token_domains"] = (
            aws_sdk_wafv2.types.token_domains.deserialize_aws_json_1_1(
                data["TokenDomains"]
            )
        )
    if "AssociationConfig" in data:
        import aws_sdk_wafv2.types.association_config

        out["association_config"] = (
            aws_sdk_wafv2.types.association_config.deserialize_aws_json_1_1(
                data["AssociationConfig"]
            )
        )
    if "RetrofittedByFirewallManager" in data:
        out["retrofitted_by_firewall_manager"] = data["RetrofittedByFirewallManager"]
    else:
        out["retrofitted_by_firewall_manager"] = False
    if "OnSourceDDoSProtectionConfig" in data:
        import aws_sdk_wafv2.types.on_source_d_do_s_protection_config

        out["on_source_d_do_s_protection_config"] = (
            aws_sdk_wafv2.types.on_source_d_do_s_protection_config.deserialize_aws_json_1_1(
                data["OnSourceDDoSProtectionConfig"]
            )
        )
    if "ApplicationConfig" in data:
        import aws_sdk_wafv2.types.application_config

        out["application_config"] = (
            aws_sdk_wafv2.types.application_config.deserialize_aws_json_1_1(
                data["ApplicationConfig"]
            )
        )
    return out
