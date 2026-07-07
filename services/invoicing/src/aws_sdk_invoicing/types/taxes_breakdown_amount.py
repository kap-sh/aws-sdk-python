"""Generated from Smithy shape ``com.amazonaws.invoicing#TaxesBreakdownAmount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.basic_string


class TaxesBreakdownAmount(TypedDict, closed=True):
    description: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The details of the taxes. </p>"""
    amount: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The tax amount. </p>"""
    rate: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The details of the tax rate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaxesBreakdownAmount) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "amount" in value:
        out["Amount"] = value["amount"]
    if "rate" in value:
        out["Rate"] = value["rate"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TaxesBreakdownAmount:
    out: TaxesBreakdownAmount = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Amount" in data:
        out["amount"] = data["Amount"]
    if "Rate" in data:
        out["rate"] = data["Rate"]
    return out
