"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListPricingRulesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.pricing_rule_arns


class ListPricingRulesFilter(TypedDict, closed=True):
    arns: NotRequired[
        "aws_sdk_billingconductor.types.pricing_rule_arns.PricingRuleArns"
    ]
    """<p>A list containing the pricing rule Amazon Resource Names (ARNs) to include in the API response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPricingRulesFilter) -> dict:
    out: dict = {}
    if "arns" in value:
        import aws_sdk_billingconductor.types.pricing_rule_arns

        out["Arns"] = aws_sdk_billingconductor.types.pricing_rule_arns.serialize_json(
            value["arns"]
        )
    return out


def deserialize_json(data: dict) -> ListPricingRulesFilter:
    out: ListPricingRulesFilter = {}  # type: ignore[typeddict-item]
    if "Arns" in data:
        import aws_sdk_billingconductor.types.pricing_rule_arns

        out["arns"] = aws_sdk_billingconductor.types.pricing_rule_arns.deserialize_json(
            data["Arns"]
        )
    return out
