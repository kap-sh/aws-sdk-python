"""Generated from Smithy shape ``com.amazonaws.costexplorer#ComparisonMetricValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class ComparisonMetricValue(TypedDict, closed=True):
    baseline_time_period_amount: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The numeric value for the baseline time period measurement.</p>"""
    comparison_time_period_amount: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The numeric value for the comparison time period measurement.</p>"""
    difference: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The calculated difference between <code>ComparisonTimePeriodAmount</code> and <code>BaselineTimePeriodAmount</code>.</p>"""
    unit: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The unit of measurement applicable to all numeric values in this comparison.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComparisonMetricValue) -> dict:
    out: dict = {}
    if "baseline_time_period_amount" in value:
        out["BaselineTimePeriodAmount"] = value["baseline_time_period_amount"]
    if "comparison_time_period_amount" in value:
        out["ComparisonTimePeriodAmount"] = value["comparison_time_period_amount"]
    if "difference" in value:
        out["Difference"] = value["difference"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ComparisonMetricValue:
    out: ComparisonMetricValue = {}  # type: ignore[typeddict-item]
    if "BaselineTimePeriodAmount" in data:
        out["baseline_time_period_amount"] = data["BaselineTimePeriodAmount"]
    if "ComparisonTimePeriodAmount" in data:
        out["comparison_time_period_amount"] = data["ComparisonTimePeriodAmount"]
    if "Difference" in data:
        out["difference"] = data["Difference"]
    if "Unit" in data:
        out["unit"] = data["Unit"]
    return out
