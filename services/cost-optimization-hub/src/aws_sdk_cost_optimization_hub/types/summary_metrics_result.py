"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#SummaryMetricsResult``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SummaryMetricsResult(TypedDict):
    savings_percentage: NotRequired["str"]
    """<p>The savings percentage based on your Amazon Web Services spend over the past 30 days.</p> <note> <p>Savings percentage is only supported when filtering by Region, account ID, or tags.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SummaryMetricsResult) -> dict:
    out: dict = {}
    if "savings_percentage" in value:
        out["savingsPercentage"] = value["savings_percentage"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SummaryMetricsResult:
    out: SummaryMetricsResult = {}  # type: ignore[typeddict-item]
    if "savingsPercentage" in data:
        out["savings_percentage"] = data["savingsPercentage"]
    return out
