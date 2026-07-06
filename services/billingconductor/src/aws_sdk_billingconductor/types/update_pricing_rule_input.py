"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdatePricingRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.modifier_percentage
    import aws_sdk_billingconductor.types.pricing_rule_arn
    import aws_sdk_billingconductor.types.pricing_rule_description
    import aws_sdk_billingconductor.types.pricing_rule_name
    import aws_sdk_billingconductor.types.pricing_rule_type
    import aws_sdk_billingconductor.types.update_tiering_input


class UpdatePricingRuleInput(TypedDict, closed=True):
    arn: "aws_sdk_billingconductor.types.pricing_rule_arn.PricingRuleArn"
    """<p> The Amazon Resource Name (ARN) of the pricing rule to update. </p>"""
    name: NotRequired[
        "aws_sdk_billingconductor.types.pricing_rule_name.PricingRuleName"
    ]
    """<p> The new name of the pricing rule. The name must be unique to each pricing rule. </p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.pricing_rule_description.PricingRuleDescription"
    ]
    """<p> The new description for the pricing rule. </p>"""
    type: NotRequired[
        "aws_sdk_billingconductor.types.pricing_rule_type.PricingRuleType"
    ]
    """<p> The new pricing rule type. </p>"""
    modifier_percentage: NotRequired[
        "aws_sdk_billingconductor.types.modifier_percentage.ModifierPercentage"
    ]
    """<p> The new modifier to show pricing plan rates as a percentage. Your entry will be rounded to the nearest 2 decimal places. </p>"""
    tiering: NotRequired[
        "aws_sdk_billingconductor.types.update_tiering_input.UpdateTieringInput"
    ]
    """<p> The set of tiering configurations for the pricing rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePricingRuleInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import aws_sdk_billingconductor.types.pricing_rule_type

        out["Type"] = aws_sdk_billingconductor.types.pricing_rule_type.serialize_json(
            value["type"]
        )
    if "modifier_percentage" in value:
        out["ModifierPercentage"] = value["modifier_percentage"]
    if "tiering" in value:
        import aws_sdk_billingconductor.types.update_tiering_input

        out["Tiering"] = (
            aws_sdk_billingconductor.types.update_tiering_input.serialize_json(
                value["tiering"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePricingRuleInput:
    out: UpdatePricingRuleInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdatePricingRuleInput.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        import aws_sdk_billingconductor.types.pricing_rule_type

        out["type"] = aws_sdk_billingconductor.types.pricing_rule_type.deserialize_json(
            data["Type"]
        )
    if "ModifierPercentage" in data:
        out["modifier_percentage"] = data["ModifierPercentage"]
    if "Tiering" in data:
        import aws_sdk_billingconductor.types.update_tiering_input

        out["tiering"] = (
            aws_sdk_billingconductor.types.update_tiering_input.deserialize_json(
                data["Tiering"]
            )
        )
    return out
