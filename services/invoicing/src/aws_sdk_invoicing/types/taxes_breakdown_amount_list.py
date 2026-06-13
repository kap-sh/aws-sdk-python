"""Generated from Smithy shape ``com.amazonaws.invoicing#TaxesBreakdownAmountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.taxes_breakdown_amount

TaxesBreakdownAmountList: TypeAlias = list[
    "aws_sdk_invoicing.types.taxes_breakdown_amount.TaxesBreakdownAmount"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaxesBreakdownAmountList) -> list:
    import aws_sdk_invoicing.types.taxes_breakdown_amount

    out: list = []
    for item in value:
        out.append(
            aws_sdk_invoicing.types.taxes_breakdown_amount.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TaxesBreakdownAmountList:
    import aws_sdk_invoicing.types.taxes_breakdown_amount

    out: TaxesBreakdownAmountList = []
    for item in data:
        out.append(
            aws_sdk_invoicing.types.taxes_breakdown_amount.deserialize_aws_json_1_0(
                item
            )
        )
    return out
