"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#EstimatedTaxes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.bounded_string
    import aws_sdk_marketplace_agreement.types.tax_breakdown


class EstimatedTaxes(TypedDict, closed=True):
    breakdown: NotRequired[
        "aws_sdk_marketplace_agreement.types.tax_breakdown.TaxBreakdown"
    ]
    """<p>A list of tax breakdown information.</p>"""
    total_amount: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The total amount of tax aggregated from the tax breakdown.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EstimatedTaxes) -> dict:
    out: dict = {}
    if "breakdown" in value:
        import aws_sdk_marketplace_agreement.types.tax_breakdown

        out["breakdown"] = (
            aws_sdk_marketplace_agreement.types.tax_breakdown.serialize_aws_json_1_0(
                value["breakdown"]
            )
        )
    if "total_amount" in value:
        out["totalAmount"] = value["total_amount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EstimatedTaxes:
    out: EstimatedTaxes = {}  # type: ignore[typeddict-item]
    if "breakdown" in data:
        import aws_sdk_marketplace_agreement.types.tax_breakdown

        out["breakdown"] = (
            aws_sdk_marketplace_agreement.types.tax_breakdown.deserialize_aws_json_1_0(
                data["breakdown"]
            )
        )
    if "totalAmount" in data:
        out["total_amount"] = data["totalAmount"]
    return out
