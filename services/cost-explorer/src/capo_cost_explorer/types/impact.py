"""Generated from Smithy shape ``com.amazonaws.costexplorer#Impact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_double
    import capo_cost_explorer.types.nullable_non_negative_double


class Impact(TypedDict, closed=True):
    max_impact: "capo_cost_explorer.types.generic_double.GenericDouble"
    """<p>The maximum dollar value that's observed for an anomaly.</p>"""
    total_impact: "capo_cost_explorer.types.generic_double.GenericDouble"
    """<p>The cumulative dollar difference between the total actual spend and total expected spend. It is calculated as <code>TotalActualSpend - TotalExpectedSpend</code>.</p>"""
    total_actual_spend: NotRequired[
        "capo_cost_explorer.types.nullable_non_negative_double.NullableNonNegativeDouble"
    ]
    """<p>The cumulative dollar amount that was actually spent during the anomaly.</p>"""
    total_expected_spend: NotRequired[
        "capo_cost_explorer.types.nullable_non_negative_double.NullableNonNegativeDouble"
    ]
    """<p>The cumulative dollar amount that was expected to be spent during the anomaly. It is calculated using advanced machine learning models to determine the typical spending pattern based on historical data for a customer.</p>"""
    total_impact_percentage: NotRequired[
        "capo_cost_explorer.types.nullable_non_negative_double.NullableNonNegativeDouble"
    ]
    """<p>The cumulative percentage difference between the total actual spend and total expected spend. It is calculated as <code>(TotalImpact / TotalExpectedSpend) * 100</code>. When <code>TotalExpectedSpend</code> is zero, this field is omitted. Expected spend can be zero in situations such as when you start to use a service for the first time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Impact) -> dict:
    out: dict = {}
    out["MaxImpact"] = value.get("max_impact", 0)
    out["TotalImpact"] = value.get("total_impact", 0)
    if "total_actual_spend" in value:
        out["TotalActualSpend"] = value["total_actual_spend"]
    if "total_expected_spend" in value:
        out["TotalExpectedSpend"] = value["total_expected_spend"]
    if "total_impact_percentage" in value:
        out["TotalImpactPercentage"] = value["total_impact_percentage"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Impact:
    out: Impact = {}  # type: ignore[typeddict-item]
    if "MaxImpact" in data:
        out["max_impact"] = data["MaxImpact"]
    else:
        out["max_impact"] = 0
    if "TotalImpact" in data:
        out["total_impact"] = data["TotalImpact"]
    else:
        out["total_impact"] = 0
    if "TotalActualSpend" in data:
        out["total_actual_spend"] = data["TotalActualSpend"]
    if "TotalExpectedSpend" in data:
        out["total_expected_spend"] = data["TotalExpectedSpend"]
    if "TotalImpactPercentage" in data:
        out["total_impact_percentage"] = data["TotalImpactPercentage"]
    return out
