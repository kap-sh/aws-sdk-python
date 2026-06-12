"""Generated from Smithy shape ``com.amazonaws.billingconductor#CreatePricingRuleInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_entity
    import aws_sdk_billingconductor.types.client_token
    import aws_sdk_billingconductor.types.create_tiering_input
    import aws_sdk_billingconductor.types.modifier_percentage
    import aws_sdk_billingconductor.types.operation
    import aws_sdk_billingconductor.types.pricing_rule_description
    import aws_sdk_billingconductor.types.pricing_rule_name
    import aws_sdk_billingconductor.types.pricing_rule_scope
    import aws_sdk_billingconductor.types.pricing_rule_type
    import aws_sdk_billingconductor.types.service
    import aws_sdk_billingconductor.types.tag_map
    import aws_sdk_billingconductor.types.usage_type


class CreatePricingRuleInput(TypedDict):
    client_token: NotRequired["aws_sdk_billingconductor.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>"""
    name: "aws_sdk_billingconductor.types.pricing_rule_name.PricingRuleName"
    """<p> The pricing rule name. The names must be unique to each pricing rule. </p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.pricing_rule_description.PricingRuleDescription"
    ]
    """<p> The pricing rule description. </p>"""
    scope: "aws_sdk_billingconductor.types.pricing_rule_scope.PricingRuleScope"
    """<p> The scope of pricing rule that indicates if it's globally applicable, or it's service-specific. </p>"""
    type: "aws_sdk_billingconductor.types.pricing_rule_type.PricingRuleType"
    """<p> The type of pricing rule. </p>"""
    modifier_percentage: NotRequired[
        "aws_sdk_billingconductor.types.modifier_percentage.ModifierPercentage"
    ]
    """<p>A percentage modifier that's applied on the public pricing rates. Your entry will be rounded to the nearest 2 decimal places.</p>"""
    service: NotRequired["aws_sdk_billingconductor.types.service.Service"]
    """<p> If the <code>Scope</code> attribute is set to <code>SERVICE</code> or <code>SKU</code>, the attribute indicates which service the <code>PricingRule</code> is applicable for. </p>"""
    tags: NotRequired["aws_sdk_billingconductor.types.tag_map.TagMap"]
    """<p> A map that contains tag keys and tag values that are attached to a pricing rule. </p>"""
    billing_entity: NotRequired[
        "aws_sdk_billingconductor.types.billing_entity.BillingEntity"
    ]
    """<p> The seller of services provided by Amazon Web Services, their affiliates, or third-party providers selling services via Amazon Web Services Marketplace. </p>"""
    tiering: NotRequired[
        "aws_sdk_billingconductor.types.create_tiering_input.CreateTieringInput"
    ]
    """<p> The set of tiering configurations for the pricing rule. </p>"""
    usage_type: NotRequired["aws_sdk_billingconductor.types.usage_type.UsageType"]
    """<p> Usage type is the unit that each service uses to measure the usage of a specific type of resource.</p> <p>If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which usage type the <code>PricingRule</code> is modifying. For example, <code>USW2-BoxUsage:m2.2xlarge</code> describes an<code> M2 High Memory Double Extra Large</code> instance in the US West (Oregon) Region. </p>"""
    operation: NotRequired["aws_sdk_billingconductor.types.operation.Operation"]
    """<p> Operation is the specific Amazon Web Services action covered by this line item. This describes the specific usage of the line item.</p> <p> If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which operation the <code>PricingRule</code> is modifying. For example, a value of <code>RunInstances:0202</code> indicates the operation of running an Amazon EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePricingRuleInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_billingconductor.types.pricing_rule_scope

    out["Scope"] = aws_sdk_billingconductor.types.pricing_rule_scope.serialize_json(
        value["scope"]
    )
    import aws_sdk_billingconductor.types.pricing_rule_type

    out["Type"] = aws_sdk_billingconductor.types.pricing_rule_type.serialize_json(
        value["type"]
    )
    if "modifier_percentage" in value:
        out["ModifierPercentage"] = value["modifier_percentage"]
    if "service" in value:
        out["Service"] = value["service"]
    if "tags" in value:
        import aws_sdk_billingconductor.types.tag_map

        out["Tags"] = aws_sdk_billingconductor.types.tag_map.serialize_json(
            value["tags"]
        )
    if "billing_entity" in value:
        out["BillingEntity"] = value["billing_entity"]
    if "tiering" in value:
        import aws_sdk_billingconductor.types.create_tiering_input

        out["Tiering"] = (
            aws_sdk_billingconductor.types.create_tiering_input.serialize_json(
                value["tiering"]
            )
        )
    if "usage_type" in value:
        out["UsageType"] = value["usage_type"]
    if "operation" in value:
        out["Operation"] = value["operation"]
    return out


def deserialize_json(data: dict) -> CreatePricingRuleInput:
    out: CreatePricingRuleInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreatePricingRuleInput.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Scope" in data:
        import aws_sdk_billingconductor.types.pricing_rule_scope

        out["scope"] = (
            aws_sdk_billingconductor.types.pricing_rule_scope.deserialize_json(
                data["Scope"]
            )
        )
    else:
        raise DeserializationError("CreatePricingRuleInput.scope required")
    if "Type" in data:
        import aws_sdk_billingconductor.types.pricing_rule_type

        out["type"] = aws_sdk_billingconductor.types.pricing_rule_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("CreatePricingRuleInput.type required")
    if "ModifierPercentage" in data:
        out["modifier_percentage"] = data["ModifierPercentage"]
    if "Service" in data:
        out["service"] = data["Service"]
    if "Tags" in data:
        import aws_sdk_billingconductor.types.tag_map

        out["tags"] = aws_sdk_billingconductor.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if "BillingEntity" in data:
        out["billing_entity"] = data["BillingEntity"]
    if "Tiering" in data:
        import aws_sdk_billingconductor.types.create_tiering_input

        out["tiering"] = (
            aws_sdk_billingconductor.types.create_tiering_input.deserialize_json(
                data["Tiering"]
            )
        )
    if "UsageType" in data:
        out["usage_type"] = data["UsageType"]
    if "Operation" in data:
        out["operation"] = data["Operation"]
    return out
