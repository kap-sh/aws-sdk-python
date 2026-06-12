"""Generated from Smithy shape ``com.amazonaws.budgets#CalculatedSpend``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.spend


class CalculatedSpend(TypedDict):
    actual_spend: "aws_sdk_budgets.types.spend.Spend"
    """<p>The amount of cost, usage, RI units, or Savings Plans units that you used.</p>"""
    forecasted_spend: NotRequired["aws_sdk_budgets.types.spend.Spend"]
    """<p>The amount of cost, usage, RI units, or Savings Plans units that you're forecasted to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CalculatedSpend) -> dict:
    out: dict = {}
    import aws_sdk_budgets.types.spend

    out["ActualSpend"] = aws_sdk_budgets.types.spend.serialize_aws_json_1_1(
        value["actual_spend"]
    )
    if "forecasted_spend" in value:
        import aws_sdk_budgets.types.spend

        out["ForecastedSpend"] = aws_sdk_budgets.types.spend.serialize_aws_json_1_1(
            value["forecasted_spend"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CalculatedSpend:
    out: CalculatedSpend = {}  # type: ignore[typeddict-item]
    if "ActualSpend" in data:
        import aws_sdk_budgets.types.spend

        out["actual_spend"] = aws_sdk_budgets.types.spend.deserialize_aws_json_1_1(
            data["ActualSpend"]
        )
    else:
        raise DeserializationError("CalculatedSpend.actual_spend required")
    if "ForecastedSpend" in data:
        import aws_sdk_budgets.types.spend

        out["forecasted_spend"] = aws_sdk_budgets.types.spend.deserialize_aws_json_1_1(
            data["ForecastedSpend"]
        )
    return out
