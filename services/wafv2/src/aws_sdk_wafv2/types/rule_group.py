"""Generated from Smithy shape ``com.amazonaws.wafv2#RuleGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.capacity_unit
    import aws_sdk_wafv2.types.custom_response_bodies
    import aws_sdk_wafv2.types.entity_description
    import aws_sdk_wafv2.types.entity_id
    import aws_sdk_wafv2.types.entity_name
    import aws_sdk_wafv2.types.label_name
    import aws_sdk_wafv2.types.label_summaries
    import aws_sdk_wafv2.types.resource_arn
    import aws_sdk_wafv2.types.rules
    import aws_sdk_wafv2.types.visibility_config


class RuleGroup(TypedDict):
    name: "aws_sdk_wafv2.types.entity_name.EntityName"
    """<p>The name of the rule group. You cannot change the name of a rule group after you create it.</p>"""
    id: "aws_sdk_wafv2.types.entity_id.EntityId"
    """<p>A unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    capacity: "aws_sdk_wafv2.types.capacity_unit.CapacityUnit"
    """<p>The web ACL capacity units (WCUs) required for this rule group.</p> <p>When you create your own rule group, you define this, and you cannot change it after creation. When you add or modify the rules in a rule group, WAF enforces this limit. You can check the capacity for a set of rules using <a>CheckCapacity</a>.</p> <p>WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html\">WAF web ACL capacity units (WCU)</a> in the <i>WAF Developer Guide</i>. </p>"""
    arn: "aws_sdk_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the entity.</p>"""
    description: NotRequired["aws_sdk_wafv2.types.entity_description.EntityDescription"]
    """<p>A description of the rule group that helps with identification. </p>"""
    rules: NotRequired["aws_sdk_wafv2.types.rules.Rules"]
    """<p>The <a>Rule</a> statements used to identify the web requests that you want to manage. Each rule includes one top-level statement that WAF uses to identify matching web requests, and parameters that govern how WAF handles them. </p>"""
    visibility_config: "aws_sdk_wafv2.types.visibility_config.VisibilityConfig"
    """<p>Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>"""
    label_namespace: NotRequired["aws_sdk_wafv2.types.label_name.LabelName"]
    """<p>The label namespace prefix for this rule group. All labels added by rules in this rule group have this prefix. </p> <ul> <li> <p>The syntax for the label namespace prefix for your rule groups is the following: </p> <p> <code>awswaf:<account ID>:rulegroup:<rule group name>:</code> </p> </li> <li> <p>When a rule with a label matches a web request, WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon: </p> <p> <code><label namespace>:<label from rule></code> </p> </li> </ul>"""
    custom_response_bodies: NotRequired[
        "aws_sdk_wafv2.types.custom_response_bodies.CustomResponseBodies"
    ]
    """<p>A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the rule group, and then use them in the rules that you define in the rule group. </p> <p>For information about customizing web requests and responses, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html\">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide</i>. </p> <p>For information about the limits on count and size for custom request and response settings, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/limits.html\">WAF quotas</a> in the <i>WAF Developer Guide</i>. </p>"""
    available_labels: NotRequired["aws_sdk_wafv2.types.label_summaries.LabelSummaries"]
    """<p>The labels that one or more rules in this rule group add to matching web requests. These labels are defined in the <code>RuleLabels</code> for a <a>Rule</a>.</p>"""
    consumed_labels: NotRequired["aws_sdk_wafv2.types.label_summaries.LabelSummaries"]
    """<p>The labels that one or more rules in this rule group match against in label match statements. These labels are defined in a <code>LabelMatchStatement</code> specification, in the <a>Statement</a> definition of a rule. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleGroup) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Id"] = value["id"]
    out["Capacity"] = value["capacity"]
    out["ARN"] = value["arn"]
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
    if "label_namespace" in value:
        out["LabelNamespace"] = value["label_namespace"]
    if "custom_response_bodies" in value:
        import aws_sdk_wafv2.types.custom_response_bodies

        out["CustomResponseBodies"] = (
            aws_sdk_wafv2.types.custom_response_bodies.serialize_aws_json_1_1(
                value["custom_response_bodies"]
            )
        )
    if "available_labels" in value:
        import aws_sdk_wafv2.types.label_summaries

        out["AvailableLabels"] = (
            aws_sdk_wafv2.types.label_summaries.serialize_aws_json_1_1(
                value["available_labels"]
            )
        )
    if "consumed_labels" in value:
        import aws_sdk_wafv2.types.label_summaries

        out["ConsumedLabels"] = (
            aws_sdk_wafv2.types.label_summaries.serialize_aws_json_1_1(
                value["consumed_labels"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleGroup:
    out: RuleGroup = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RuleGroup.name required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("RuleGroup.id required")
    if "Capacity" in data:
        out["capacity"] = data["Capacity"]
    else:
        raise DeserializationError("RuleGroup.capacity required")
    if "ARN" in data:
        out["arn"] = data["ARN"]
    else:
        raise DeserializationError("RuleGroup.arn required")
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
        raise DeserializationError("RuleGroup.visibility_config required")
    if "LabelNamespace" in data:
        out["label_namespace"] = data["LabelNamespace"]
    if "CustomResponseBodies" in data:
        import aws_sdk_wafv2.types.custom_response_bodies

        out["custom_response_bodies"] = (
            aws_sdk_wafv2.types.custom_response_bodies.deserialize_aws_json_1_1(
                data["CustomResponseBodies"]
            )
        )
    if "AvailableLabels" in data:
        import aws_sdk_wafv2.types.label_summaries

        out["available_labels"] = (
            aws_sdk_wafv2.types.label_summaries.deserialize_aws_json_1_1(
                data["AvailableLabels"]
            )
        )
    if "ConsumedLabels" in data:
        import aws_sdk_wafv2.types.label_summaries

        out["consumed_labels"] = (
            aws_sdk_wafv2.types.label_summaries.deserialize_aws_json_1_1(
                data["ConsumedLabels"]
            )
        )
    return out
