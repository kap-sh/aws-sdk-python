"""Generated from Smithy shape ``com.amazonaws.invoicing#AmountBreakdown``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string
    import capo_invoicing.types.discounts_breakdown
    import capo_invoicing.types.fees_breakdown
    import capo_invoicing.types.taxes_breakdown


class AmountBreakdown(TypedDict, closed=True):
    sub_total_amount: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p> The total of a set of the breakdown. </p>"""
    discounts: NotRequired[
        "capo_invoicing.types.discounts_breakdown.DiscountsBreakdown"
    ]
    """<p> The discounted amount. </p>"""
    taxes: NotRequired["capo_invoicing.types.taxes_breakdown.TaxesBreakdown"]
    """<p> The tax amount. </p>"""
    fees: NotRequired["capo_invoicing.types.fees_breakdown.FeesBreakdown"]
    """<p> The fee amount. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AmountBreakdown) -> dict:
    out: dict = {}
    if "sub_total_amount" in value:
        out["SubTotalAmount"] = value["sub_total_amount"]
    if "discounts" in value:
        import capo_invoicing.types.discounts_breakdown

        out["Discounts"] = (
            capo_invoicing.types.discounts_breakdown.serialize_aws_json_1_0(
                value["discounts"]
            )
        )
    if "taxes" in value:
        import capo_invoicing.types.taxes_breakdown

        out["Taxes"] = capo_invoicing.types.taxes_breakdown.serialize_aws_json_1_0(
            value["taxes"]
        )
    if "fees" in value:
        import capo_invoicing.types.fees_breakdown

        out["Fees"] = capo_invoicing.types.fees_breakdown.serialize_aws_json_1_0(
            value["fees"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AmountBreakdown:
    out: AmountBreakdown = {}  # type: ignore[typeddict-item]
    if "SubTotalAmount" in data:
        out["sub_total_amount"] = data["SubTotalAmount"]
    if "Discounts" in data:
        import capo_invoicing.types.discounts_breakdown

        out["discounts"] = (
            capo_invoicing.types.discounts_breakdown.deserialize_aws_json_1_0(
                data["Discounts"]
            )
        )
    if "Taxes" in data:
        import capo_invoicing.types.taxes_breakdown

        out["taxes"] = capo_invoicing.types.taxes_breakdown.deserialize_aws_json_1_0(
            data["Taxes"]
        )
    if "Fees" in data:
        import capo_invoicing.types.fees_breakdown

        out["fees"] = capo_invoicing.types.fees_breakdown.deserialize_aws_json_1_0(
            data["Fees"]
        )
    return out
