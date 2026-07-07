"""Generated from Smithy shape ``com.amazonaws.invoicing#TaxesBreakdown``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.basic_string
    import aws_sdk_invoicing.types.taxes_breakdown_amount_list


class TaxesBreakdown(TypedDict, closed=True):
    breakdown: NotRequired[
        "aws_sdk_invoicing.types.taxes_breakdown_amount_list.TaxesBreakdownAmountList"
    ]
    """<p> A list of tax information. </p>"""
    total_amount: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The total amount for your taxes. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaxesBreakdown) -> dict:
    out: dict = {}
    if "breakdown" in value:
        import aws_sdk_invoicing.types.taxes_breakdown_amount_list

        out["Breakdown"] = (
            aws_sdk_invoicing.types.taxes_breakdown_amount_list.serialize_aws_json_1_0(
                value["breakdown"]
            )
        )
    if "total_amount" in value:
        out["TotalAmount"] = value["total_amount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TaxesBreakdown:
    out: TaxesBreakdown = {}  # type: ignore[typeddict-item]
    if "Breakdown" in data:
        import aws_sdk_invoicing.types.taxes_breakdown_amount_list

        out["breakdown"] = (
            aws_sdk_invoicing.types.taxes_breakdown_amount_list.deserialize_aws_json_1_0(
                data["Breakdown"]
            )
        )
    if "TotalAmount" in data:
        out["total_amount"] = data["TotalAmount"]
    return out
