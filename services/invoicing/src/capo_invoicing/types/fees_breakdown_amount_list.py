"""Generated from Smithy shape ``com.amazonaws.invoicing#FeesBreakdownAmountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.fees_breakdown_amount

FeesBreakdownAmountList: TypeAlias = list[
    "capo_invoicing.types.fees_breakdown_amount.FeesBreakdownAmount"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FeesBreakdownAmountList) -> list:
    import capo_invoicing.types.fees_breakdown_amount

    out: list = []
    for item in value:
        out.append(
            capo_invoicing.types.fees_breakdown_amount.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FeesBreakdownAmountList:
    import capo_invoicing.types.fees_breakdown_amount

    out: FeesBreakdownAmountList = []
    for item in data:
        out.append(
            capo_invoicing.types.fees_breakdown_amount.deserialize_aws_json_1_0(item)
        )
    return out
