"""Generated from Smithy shape ``com.amazonaws.invoicing#FeesBreakdownAmount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string


class FeesBreakdownAmount(TypedDict, closed=True):
    description: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p> The list of fees information. </p>"""
    amount: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p> The fee amount. </p>"""
    rate: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p> Details about the rate amount. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FeesBreakdownAmount) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "amount" in value:
        out["Amount"] = value["amount"]
    if "rate" in value:
        out["Rate"] = value["rate"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FeesBreakdownAmount:
    out: FeesBreakdownAmount = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Amount" in data:
        out["amount"] = data["Amount"]
    if "Rate" in data:
        out["rate"] = data["Rate"]
    return out
