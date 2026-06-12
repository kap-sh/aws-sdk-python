"""Generated from Smithy shape ``com.amazonaws.billingconductor#CreatePricingPlanInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.client_token
    import aws_sdk_billingconductor.types.pricing_plan_description
    import aws_sdk_billingconductor.types.pricing_plan_name
    import aws_sdk_billingconductor.types.pricing_rule_arns_input
    import aws_sdk_billingconductor.types.tag_map


class CreatePricingPlanInput(TypedDict):
    client_token: NotRequired["aws_sdk_billingconductor.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>"""
    name: "aws_sdk_billingconductor.types.pricing_plan_name.PricingPlanName"
    """<p>The name of the pricing plan. The names must be unique to each pricing plan. </p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.pricing_plan_description.PricingPlanDescription"
    ]
    """<p>The description of the pricing plan. </p>"""
    pricing_rule_arns: NotRequired[
        "aws_sdk_billingconductor.types.pricing_rule_arns_input.PricingRuleArnsInput"
    ]
    """<p> A list of Amazon Resource Names (ARNs) that define the pricing plan parameters. </p>"""
    tags: NotRequired["aws_sdk_billingconductor.types.tag_map.TagMap"]
    """<p> A map that contains tag keys and tag values that are attached to a pricing plan. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePricingPlanInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "pricing_rule_arns" in value:
        import aws_sdk_billingconductor.types.pricing_rule_arns_input

        out["PricingRuleArns"] = (
            aws_sdk_billingconductor.types.pricing_rule_arns_input.serialize_json(
                value["pricing_rule_arns"]
            )
        )
    if "tags" in value:
        import aws_sdk_billingconductor.types.tag_map

        out["Tags"] = aws_sdk_billingconductor.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreatePricingPlanInput:
    out: CreatePricingPlanInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreatePricingPlanInput.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "PricingRuleArns" in data:
        import aws_sdk_billingconductor.types.pricing_rule_arns_input

        out["pricing_rule_arns"] = (
            aws_sdk_billingconductor.types.pricing_rule_arns_input.deserialize_json(
                data["PricingRuleArns"]
            )
        )
    if "Tags" in data:
        import aws_sdk_billingconductor.types.tag_map

        out["tags"] = aws_sdk_billingconductor.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
