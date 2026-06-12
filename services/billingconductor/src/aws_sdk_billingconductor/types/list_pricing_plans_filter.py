"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListPricingPlansFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.pricing_plan_arns


class ListPricingPlansFilter(TypedDict):
    arns: NotRequired[
        "aws_sdk_billingconductor.types.pricing_plan_arns.PricingPlanArns"
    ]
    """<p>A list of pricing plan Amazon Resource Names (ARNs) to retrieve information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPricingPlansFilter) -> dict:
    out: dict = {}
    if "arns" in value:
        import aws_sdk_billingconductor.types.pricing_plan_arns

        out["Arns"] = aws_sdk_billingconductor.types.pricing_plan_arns.serialize_json(
            value["arns"]
        )
    return out


def deserialize_json(data: dict) -> ListPricingPlansFilter:
    out: ListPricingPlansFilter = {}  # type: ignore[typeddict-item]
    if "Arns" in data:
        import aws_sdk_billingconductor.types.pricing_plan_arns

        out["arns"] = aws_sdk_billingconductor.types.pricing_plan_arns.deserialize_json(
            data["Arns"]
        )
    return out
