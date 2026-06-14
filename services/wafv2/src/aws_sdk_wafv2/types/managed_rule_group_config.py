"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedRuleGroupConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.aws_managed_rules_acfp_rule_set
    import aws_sdk_wafv2.types.aws_managed_rules_anti_d_do_s_rule_set
    import aws_sdk_wafv2.types.aws_managed_rules_atp_rule_set
    import aws_sdk_wafv2.types.aws_managed_rules_bot_control_rule_set
    import aws_sdk_wafv2.types.login_path_string
    import aws_sdk_wafv2.types.password_field
    import aws_sdk_wafv2.types.payload_type
    import aws_sdk_wafv2.types.username_field


class ManagedRuleGroupConfig(TypedDict):
    login_path: NotRequired["aws_sdk_wafv2.types.login_path_string.LoginPathString"]
    """<note> <p>Instead of this setting, provide your configuration under <code>AWSManagedRulesATPRuleSet</code>. </p> </note>"""
    payload_type: NotRequired["aws_sdk_wafv2.types.payload_type.PayloadType"]
    """<note> <p>Instead of this setting, provide your configuration under the request inspection configuration for <code>AWSManagedRulesATPRuleSet</code> or <code>AWSManagedRulesACFPRuleSet</code>. </p> </note>"""
    username_field: NotRequired["aws_sdk_wafv2.types.username_field.UsernameField"]
    """<note> <p>Instead of this setting, provide your configuration under the request inspection configuration for <code>AWSManagedRulesATPRuleSet</code> or <code>AWSManagedRulesACFPRuleSet</code>. </p> </note>"""
    password_field: NotRequired["aws_sdk_wafv2.types.password_field.PasswordField"]
    """<note> <p>Instead of this setting, provide your configuration under the request inspection configuration for <code>AWSManagedRulesATPRuleSet</code> or <code>AWSManagedRulesACFPRuleSet</code>. </p> </note>"""
    aws_managed_rules_bot_control_rule_set: NotRequired[
        "aws_sdk_wafv2.types.aws_managed_rules_bot_control_rule_set.AWSManagedRulesBotControlRuleSet"
    ]
    r"""<p>Additional configuration for using the Bot Control managed rule group. Use this to specify the inspection level that you want to use. For information about using the Bot Control managed rule group, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html\">WAF Bot Control rule group</a> and <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control.html\">WAF Bot Control</a> in the <i>WAF Developer Guide</i>.</p>"""
    aws_managed_rules_atp_rule_set: NotRequired[
        "aws_sdk_wafv2.types.aws_managed_rules_atp_rule_set.AWSManagedRulesATPRuleSet"
    ]
    r"""<p>Additional configuration for using the account takeover prevention (ATP) managed rule group, <code>AWSManagedRulesATPRuleSet</code>. Use this to provide login request information to the rule group. For web ACLs that protect CloudFront distributions, use this to also provide the information about how your distribution responds to login requests. </p> <p>This configuration replaces the individual configuration fields in <code>ManagedRuleGroupConfig</code> and provides additional feature configuration. </p> <p>For information about using the ATP managed rule group, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-atp.html\">WAF Fraud Control account takeover prevention (ATP) rule group</a> and <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp.html\">WAF Fraud Control account takeover prevention (ATP)</a> in the <i>WAF Developer Guide</i>.</p>"""
    aws_managed_rules_acfp_rule_set: NotRequired[
        "aws_sdk_wafv2.types.aws_managed_rules_acfp_rule_set.AWSManagedRulesACFPRuleSet"
    ]
    r"""<p>Additional configuration for using the account creation fraud prevention (ACFP) managed rule group, <code>AWSManagedRulesACFPRuleSet</code>. Use this to provide account creation request information to the rule group. For web ACLs that protect CloudFront distributions, use this to also provide the information about how your distribution responds to account creation requests. </p> <p>For information about using the ACFP managed rule group, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-acfp.html\">WAF Fraud Control account creation fraud prevention (ACFP) rule group</a> and <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/waf-acfp.html\">WAF Fraud Control account creation fraud prevention (ACFP)</a> in the <i>WAF Developer Guide</i>.</p>"""
    aws_managed_rules_anti_d_do_s_rule_set: NotRequired[
        "aws_sdk_wafv2.types.aws_managed_rules_anti_d_do_s_rule_set.AWSManagedRulesAntiDDoSRuleSet"
    ]
    r"""<p>Additional configuration for using the anti-DDoS managed rule group, <code>AWSManagedRulesAntiDDoSRuleSet</code>. Use this to configure anti-DDoS behavior for the rule group. </p> <p>For information about using the anti-DDoS managed rule group, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-anti-ddos.html\">WAF Anti-DDoS rule group</a> and <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/waf-anti-ddos.html\">Distributed Denial of Service (DDoS) prevention</a> in the <i>WAF Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleGroupConfig) -> dict:
    out: dict = {}
    if "login_path" in value:
        out["LoginPath"] = value["login_path"]
    if "payload_type" in value:
        import aws_sdk_wafv2.types.payload_type

        out["PayloadType"] = aws_sdk_wafv2.types.payload_type.serialize_aws_json_1_1(
            value["payload_type"]
        )
    if "username_field" in value:
        import aws_sdk_wafv2.types.username_field

        out["UsernameField"] = (
            aws_sdk_wafv2.types.username_field.serialize_aws_json_1_1(
                value["username_field"]
            )
        )
    if "password_field" in value:
        import aws_sdk_wafv2.types.password_field

        out["PasswordField"] = (
            aws_sdk_wafv2.types.password_field.serialize_aws_json_1_1(
                value["password_field"]
            )
        )
    if "aws_managed_rules_bot_control_rule_set" in value:
        import aws_sdk_wafv2.types.aws_managed_rules_bot_control_rule_set

        out["AWSManagedRulesBotControlRuleSet"] = (
            aws_sdk_wafv2.types.aws_managed_rules_bot_control_rule_set.serialize_aws_json_1_1(
                value["aws_managed_rules_bot_control_rule_set"]
            )
        )
    if "aws_managed_rules_atp_rule_set" in value:
        import aws_sdk_wafv2.types.aws_managed_rules_atp_rule_set

        out["AWSManagedRulesATPRuleSet"] = (
            aws_sdk_wafv2.types.aws_managed_rules_atp_rule_set.serialize_aws_json_1_1(
                value["aws_managed_rules_atp_rule_set"]
            )
        )
    if "aws_managed_rules_acfp_rule_set" in value:
        import aws_sdk_wafv2.types.aws_managed_rules_acfp_rule_set

        out["AWSManagedRulesACFPRuleSet"] = (
            aws_sdk_wafv2.types.aws_managed_rules_acfp_rule_set.serialize_aws_json_1_1(
                value["aws_managed_rules_acfp_rule_set"]
            )
        )
    if "aws_managed_rules_anti_d_do_s_rule_set" in value:
        import aws_sdk_wafv2.types.aws_managed_rules_anti_d_do_s_rule_set

        out["AWSManagedRulesAntiDDoSRuleSet"] = (
            aws_sdk_wafv2.types.aws_managed_rules_anti_d_do_s_rule_set.serialize_aws_json_1_1(
                value["aws_managed_rules_anti_d_do_s_rule_set"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedRuleGroupConfig:
    out: ManagedRuleGroupConfig = {}  # type: ignore[typeddict-item]
    if "LoginPath" in data:
        out["login_path"] = data["LoginPath"]
    if "PayloadType" in data:
        import aws_sdk_wafv2.types.payload_type

        out["payload_type"] = aws_sdk_wafv2.types.payload_type.deserialize_aws_json_1_1(
            data["PayloadType"]
        )
    if "UsernameField" in data:
        import aws_sdk_wafv2.types.username_field

        out["username_field"] = (
            aws_sdk_wafv2.types.username_field.deserialize_aws_json_1_1(
                data["UsernameField"]
            )
        )
    if "PasswordField" in data:
        import aws_sdk_wafv2.types.password_field

        out["password_field"] = (
            aws_sdk_wafv2.types.password_field.deserialize_aws_json_1_1(
                data["PasswordField"]
            )
        )
    if "AWSManagedRulesBotControlRuleSet" in data:
        import aws_sdk_wafv2.types.aws_managed_rules_bot_control_rule_set

        out["aws_managed_rules_bot_control_rule_set"] = (
            aws_sdk_wafv2.types.aws_managed_rules_bot_control_rule_set.deserialize_aws_json_1_1(
                data["AWSManagedRulesBotControlRuleSet"]
            )
        )
    if "AWSManagedRulesATPRuleSet" in data:
        import aws_sdk_wafv2.types.aws_managed_rules_atp_rule_set

        out["aws_managed_rules_atp_rule_set"] = (
            aws_sdk_wafv2.types.aws_managed_rules_atp_rule_set.deserialize_aws_json_1_1(
                data["AWSManagedRulesATPRuleSet"]
            )
        )
    if "AWSManagedRulesACFPRuleSet" in data:
        import aws_sdk_wafv2.types.aws_managed_rules_acfp_rule_set

        out["aws_managed_rules_acfp_rule_set"] = (
            aws_sdk_wafv2.types.aws_managed_rules_acfp_rule_set.deserialize_aws_json_1_1(
                data["AWSManagedRulesACFPRuleSet"]
            )
        )
    if "AWSManagedRulesAntiDDoSRuleSet" in data:
        import aws_sdk_wafv2.types.aws_managed_rules_anti_d_do_s_rule_set

        out["aws_managed_rules_anti_d_do_s_rule_set"] = (
            aws_sdk_wafv2.types.aws_managed_rules_anti_d_do_s_rule_set.deserialize_aws_json_1_1(
                data["AWSManagedRulesAntiDDoSRuleSet"]
            )
        )
    return out
