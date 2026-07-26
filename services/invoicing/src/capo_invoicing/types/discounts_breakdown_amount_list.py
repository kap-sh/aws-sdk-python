"""Generated from Smithy shape ``com.amazonaws.invoicing#DiscountsBreakdownAmountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.discounts_breakdown_amount

DiscountsBreakdownAmountList: TypeAlias = list[
    "capo_invoicing.types.discounts_breakdown_amount.DiscountsBreakdownAmount"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DiscountsBreakdownAmountList) -> list:
    import capo_invoicing.types.discounts_breakdown_amount

    out: list = []
    for item in value:
        out.append(
            capo_invoicing.types.discounts_breakdown_amount.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DiscountsBreakdownAmountList:
    import capo_invoicing.types.discounts_breakdown_amount

    out: DiscountsBreakdownAmountList = []
    for item in data:
        out.append(
            capo_invoicing.types.discounts_breakdown_amount.deserialize_aws_json_1_0(
                item
            )
        )
    return out
