"""Generated from Smithy shape ``com.amazonaws.budgets#CalculatedSpend``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.spend


class CalculatedSpend(TypedDict, closed=True):
    actual_spend: "capo_budgets.types.spend.Spend"
    """<p>The amount of cost, usage, RI units, or Savings Plans units that you used.</p>"""
    forecasted_spend: NotRequired["capo_budgets.types.spend.Spend"]
    """<p>The amount of cost, usage, RI units, or Savings Plans units that you're forecasted to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CalculatedSpend) -> dict:
    out: dict = {}
    import capo_budgets.types.spend

    out["ActualSpend"] = capo_budgets.types.spend.serialize_aws_json_1_1(
        value["actual_spend"]
    )
    if "forecasted_spend" in value:
        import capo_budgets.types.spend

        out["ForecastedSpend"] = capo_budgets.types.spend.serialize_aws_json_1_1(
            value["forecasted_spend"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CalculatedSpend:
    out: CalculatedSpend = {}  # type: ignore[typeddict-item]
    if "ActualSpend" in data:
        import capo_budgets.types.spend

        out["actual_spend"] = capo_budgets.types.spend.deserialize_aws_json_1_1(
            data["ActualSpend"]
        )
    else:
        raise DeserializationError("CalculatedSpend.actual_spend required")
    if "ForecastedSpend" in data:
        import capo_budgets.types.spend

        out["forecasted_spend"] = capo_budgets.types.spend.deserialize_aws_json_1_1(
            data["ForecastedSpend"]
        )
    return out
