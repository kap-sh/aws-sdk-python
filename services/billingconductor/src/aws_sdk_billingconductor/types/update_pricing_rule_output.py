"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdatePricingRuleOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_entity
    import aws_sdk_billingconductor.types.instant
    import aws_sdk_billingconductor.types.modifier_percentage
    import aws_sdk_billingconductor.types.number_of_pricing_plans_associated_with
    import aws_sdk_billingconductor.types.operation
    import aws_sdk_billingconductor.types.pricing_rule_arn
    import aws_sdk_billingconductor.types.pricing_rule_description
    import aws_sdk_billingconductor.types.pricing_rule_name
    import aws_sdk_billingconductor.types.pricing_rule_scope
    import aws_sdk_billingconductor.types.pricing_rule_type
    import aws_sdk_billingconductor.types.service
    import aws_sdk_billingconductor.types.update_tiering_input
    import aws_sdk_billingconductor.types.usage_type


class UpdatePricingRuleOutput(TypedDict):
    arn: NotRequired["aws_sdk_billingconductor.types.pricing_rule_arn.PricingRuleArn"]
    """<p> The Amazon Resource Name (ARN) of the successfully updated pricing rule. </p>"""
    name: NotRequired[
        "aws_sdk_billingconductor.types.pricing_rule_name.PricingRuleName"
    ]
    """<p> The new name of the pricing rule. The name must be unique to each pricing rule. </p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.pricing_rule_description.PricingRuleDescription"
    ]
    """<p> The new description for the pricing rule. </p>"""
    scope: NotRequired[
        "aws_sdk_billingconductor.types.pricing_rule_scope.PricingRuleScope"
    ]
    """<p> The scope of pricing rule that indicates if it's globally applicable, or it's service-specific. </p>"""
    type: NotRequired[
        "aws_sdk_billingconductor.types.pricing_rule_type.PricingRuleType"
    ]
    """<p> The new pricing rule type. </p>"""
    modifier_percentage: NotRequired[
        "aws_sdk_billingconductor.types.modifier_percentage.ModifierPercentage"
    ]
    """<p> The new modifier to show pricing plan rates as a percentage. </p>"""
    service: NotRequired["aws_sdk_billingconductor.types.service.Service"]
    """<p> If the <code>Scope</code> attribute is set to <code>SERVICE</code>, the attribute indicates which service the <code>PricingRule</code> is applicable for. </p>"""
    associated_pricing_plan_count: "aws_sdk_billingconductor.types.number_of_pricing_plans_associated_with.NumberOfPricingPlansAssociatedWith"
    """<p> The pricing plans count that this pricing rule is associated with. </p>"""
    last_modified_time: "aws_sdk_billingconductor.types.instant.Instant"
    """<p> The most recent time the pricing rule was modified. </p>"""
    billing_entity: NotRequired[
        "aws_sdk_billingconductor.types.billing_entity.BillingEntity"
    ]
    """<p> The seller of services provided by Amazon Web Services, their affiliates, or third-party providers selling services via Amazon Web Services Marketplace. </p>"""
    tiering: NotRequired[
        "aws_sdk_billingconductor.types.update_tiering_input.UpdateTieringInput"
    ]
    """<p> The set of tiering configurations for the pricing rule. </p>"""
    usage_type: NotRequired["aws_sdk_billingconductor.types.usage_type.UsageType"]
    """<p>Usage type is the unit that each service uses to measure the usage of a specific type of resource.</p> <p>If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which usage type the <code>PricingRule</code> is modifying. For example, <code>USW2-BoxUsage:m2.2xlarge</code> describes an <code>M2 High Memory Double Extra Large</code> instance in the US West (Oregon) Region. </p>"""
    operation: NotRequired["aws_sdk_billingconductor.types.operation.Operation"]
    """<p>Operation refers to the specific Amazon Web Services covered by this line item. This describes the specific usage of the line item.</p> <p> If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which operation the <code>PricingRule</code> is modifying. For example, a value of <code>RunInstances:0202</code> indicates the operation of running an Amazon EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePricingRuleOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "scope" in value:
        import aws_sdk_billingconductor.types.pricing_rule_scope

        out["Scope"] = aws_sdk_billingconductor.types.pricing_rule_scope.serialize_json(
            value["scope"]
        )
    if "type" in value:
        import aws_sdk_billingconductor.types.pricing_rule_type

        out["Type"] = aws_sdk_billingconductor.types.pricing_rule_type.serialize_json(
            value["type"]
        )
    if "modifier_percentage" in value:
        out["ModifierPercentage"] = value["modifier_percentage"]
    if "service" in value:
        out["Service"] = value["service"]
    out["AssociatedPricingPlanCount"] = value.get("associated_pricing_plan_count", 0)
    out["LastModifiedTime"] = value.get("last_modified_time", 0)
    if "billing_entity" in value:
        out["BillingEntity"] = value["billing_entity"]
    if "tiering" in value:
        import aws_sdk_billingconductor.types.update_tiering_input

        out["Tiering"] = (
            aws_sdk_billingconductor.types.update_tiering_input.serialize_json(
                value["tiering"]
            )
        )
    if "usage_type" in value:
        out["UsageType"] = value["usage_type"]
    if "operation" in value:
        out["Operation"] = value["operation"]
    return out


def deserialize_json(data: dict) -> UpdatePricingRuleOutput:
    out: UpdatePricingRuleOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Scope" in data:
        import aws_sdk_billingconductor.types.pricing_rule_scope

        out["scope"] = (
            aws_sdk_billingconductor.types.pricing_rule_scope.deserialize_json(
                data["Scope"]
            )
        )
    if "Type" in data:
        import aws_sdk_billingconductor.types.pricing_rule_type

        out["type"] = aws_sdk_billingconductor.types.pricing_rule_type.deserialize_json(
            data["Type"]
        )
    if "ModifierPercentage" in data:
        out["modifier_percentage"] = data["ModifierPercentage"]
    if "Service" in data:
        out["service"] = data["Service"]
    if "AssociatedPricingPlanCount" in data:
        out["associated_pricing_plan_count"] = data["AssociatedPricingPlanCount"]
    else:
        out["associated_pricing_plan_count"] = 0
    if "LastModifiedTime" in data:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if "BillingEntity" in data:
        out["billing_entity"] = data["BillingEntity"]
    if "Tiering" in data:
        import aws_sdk_billingconductor.types.update_tiering_input

        out["tiering"] = (
            aws_sdk_billingconductor.types.update_tiering_input.deserialize_json(
                data["Tiering"]
            )
        )
    if "UsageType" in data:
        out["usage_type"] = data["UsageType"]
    if "Operation" in data:
        out["operation"] = data["Operation"]
    return out
