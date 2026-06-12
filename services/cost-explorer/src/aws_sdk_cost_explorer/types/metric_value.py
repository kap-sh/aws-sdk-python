"""Generated from Smithy shape ``com.amazonaws.costexplorer#MetricValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.metric_amount
    import aws_sdk_cost_explorer.types.metric_unit


class MetricValue(TypedDict):
    amount: NotRequired["aws_sdk_cost_explorer.types.metric_amount.MetricAmount"]
    """<p>The actual number that represents the metric.</p>"""
    unit: NotRequired["aws_sdk_cost_explorer.types.metric_unit.MetricUnit"]
    """<p>The unit that the metric is given in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricValue) -> dict:
    out: dict = {}
    if "amount" in value:
        out["Amount"] = value["amount"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricValue:
    out: MetricValue = {}  # type: ignore[typeddict-item]
    if "Amount" in data:
        out["amount"] = data["Amount"]
    if "Unit" in data:
        out["unit"] = data["Unit"]
    return out
