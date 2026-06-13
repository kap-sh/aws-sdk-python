"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssessmentCost``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.cost_currency


class AssessmentCost(TypedDict):
    amount: NotRequired["float"]
    """<p>The cost amount for the assessment.</p>"""
    currency: NotRequired["aws_sdk_resiliencehubv2.types.cost_currency.CostCurrency"]
    """<p>The currency of the assessment cost.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentCost) -> dict:
    out: dict = {}
    if "amount" in value:
        out["amount"] = value["amount"]
    if "currency" in value:
        import aws_sdk_resiliencehubv2.types.cost_currency

        out["currency"] = aws_sdk_resiliencehubv2.types.cost_currency.serialize_json(
            value["currency"]
        )
    return out


def deserialize_json(data: dict) -> AssessmentCost:
    out: AssessmentCost = {}  # type: ignore[typeddict-item]
    if "amount" in data:
        out["amount"] = data["amount"]
    if "currency" in data:
        import aws_sdk_resiliencehubv2.types.cost_currency

        out["currency"] = aws_sdk_resiliencehubv2.types.cost_currency.deserialize_json(
            data["currency"]
        )
    return out
