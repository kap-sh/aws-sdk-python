"""Generated from Smithy shape ``com.amazonaws.wafv2#CreateRuleGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.capacity_unit
    import aws_sdk_wafv2.types.custom_response_bodies
    import aws_sdk_wafv2.types.entity_description
    import aws_sdk_wafv2.types.entity_name
    import aws_sdk_wafv2.types.rules
    import aws_sdk_wafv2.types.scope
    import aws_sdk_wafv2.types.tag_list
    import aws_sdk_wafv2.types.visibility_config


class CreateRuleGroupRequest(TypedDict):
    name: "aws_sdk_wafv2.types.entity_name.EntityName"
    """<p>The name of the rule group. You cannot change the name of a rule group after you create it.</p>"""
    scope: "aws_sdk_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    capacity: "aws_sdk_wafv2.types.capacity_unit.CapacityUnit"
    """<p>The web ACL capacity units (WCUs) required for this rule group.</p> <p>When you create your own rule group, you define this, and you cannot change it after creation. When you add or modify the rules in a rule group, WAF enforces this limit. You can check the capacity for a set of rules using <a>CheckCapacity</a>.</p> <p>WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html\">WAF web ACL capacity units (WCU)</a> in the <i>WAF Developer Guide</i>. </p>"""
    description: NotRequired["aws_sdk_wafv2.types.entity_description.EntityDescription"]
    """<p>A description of the rule group that helps with identification. </p>"""
    rules: NotRequired["aws_sdk_wafv2.types.rules.Rules"]
    """<p>The <a>Rule</a> statements used to identify the web requests that you want to manage. Each rule includes one top-level statement that WAF uses to identify matching web requests, and parameters that govern how WAF handles them. </p>"""
    visibility_config: "aws_sdk_wafv2.types.visibility_config.VisibilityConfig"
    """<p>Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>"""
    tags: NotRequired["aws_sdk_wafv2.types.tag_list.TagList"]
    """<p>An array of key:value pairs to associate with the resource.</p>"""
    custom_response_bodies: NotRequired[
        "aws_sdk_wafv2.types.custom_response_bodies.CustomResponseBodies"
    ]
    """<p>A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the rule group, and then use them in the rules that you define in the rule group. </p> <p>For information about customizing web requests and responses, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html\">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide</i>. </p> <p>For information about the limits on count and size for custom request and response settings, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/limits.html\">WAF quotas</a> in the <i>WAF Developer Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRuleGroupRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_wafv2.types.scope

    out["Scope"] = aws_sdk_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    out["Capacity"] = value["capacity"]
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
    if "tags" in value:
        import aws_sdk_wafv2.types.tag_list

        out["Tags"] = aws_sdk_wafv2.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "custom_response_bodies" in value:
        import aws_sdk_wafv2.types.custom_response_bodies

        out["CustomResponseBodies"] = (
            aws_sdk_wafv2.types.custom_response_bodies.serialize_aws_json_1_1(
                value["custom_response_bodies"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRuleGroupRequest:
    out: CreateRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRuleGroupRequest.name required")
    if "Scope" in data:
        import aws_sdk_wafv2.types.scope

        out["scope"] = aws_sdk_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError("CreateRuleGroupRequest.scope required")
    if "Capacity" in data:
        out["capacity"] = data["Capacity"]
    else:
        raise DeserializationError("CreateRuleGroupRequest.capacity required")
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
        raise DeserializationError("CreateRuleGroupRequest.visibility_config required")
    if "Tags" in data:
        import aws_sdk_wafv2.types.tag_list

        out["tags"] = aws_sdk_wafv2.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "CustomResponseBodies" in data:
        import aws_sdk_wafv2.types.custom_response_bodies

        out["custom_response_bodies"] = (
            aws_sdk_wafv2.types.custom_response_bodies.deserialize_aws_json_1_1(
                data["CustomResponseBodies"]
            )
        )
    return out
