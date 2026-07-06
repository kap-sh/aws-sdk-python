"""Generated from Smithy shape ``com.amazonaws.quicksight#Computation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.forecast_computation
    import aws_sdk_quicksight.types.growth_rate_computation
    import aws_sdk_quicksight.types.maximum_minimum_computation
    import aws_sdk_quicksight.types.metric_comparison_computation
    import aws_sdk_quicksight.types.period_over_period_computation
    import aws_sdk_quicksight.types.period_to_date_computation
    import aws_sdk_quicksight.types.top_bottom_movers_computation
    import aws_sdk_quicksight.types.top_bottom_ranked_computation
    import aws_sdk_quicksight.types.total_aggregation_computation
    import aws_sdk_quicksight.types.unique_values_computation


class Computation(TypedDict, closed=True):
    top_bottom_ranked: NotRequired[
        "aws_sdk_quicksight.types.top_bottom_ranked_computation.TopBottomRankedComputation"
    ]
    """<p>The top ranked and bottom ranked computation configuration.</p>"""
    top_bottom_movers: NotRequired[
        "aws_sdk_quicksight.types.top_bottom_movers_computation.TopBottomMoversComputation"
    ]
    """<p>The top movers and bottom movers computation configuration.</p>"""
    total_aggregation: NotRequired[
        "aws_sdk_quicksight.types.total_aggregation_computation.TotalAggregationComputation"
    ]
    """<p>The total aggregation computation configuration.</p>"""
    maximum_minimum: NotRequired[
        "aws_sdk_quicksight.types.maximum_minimum_computation.MaximumMinimumComputation"
    ]
    """<p>The maximum and minimum computation configuration.</p>"""
    metric_comparison: NotRequired[
        "aws_sdk_quicksight.types.metric_comparison_computation.MetricComparisonComputation"
    ]
    """<p>The metric comparison computation configuration.</p>"""
    period_over_period: NotRequired[
        "aws_sdk_quicksight.types.period_over_period_computation.PeriodOverPeriodComputation"
    ]
    """<p>The period over period computation configuration.</p>"""
    period_to_date: NotRequired[
        "aws_sdk_quicksight.types.period_to_date_computation.PeriodToDateComputation"
    ]
    """<p>The period to <code>DataSetIdentifier</code> computation configuration.</p>"""
    growth_rate: NotRequired[
        "aws_sdk_quicksight.types.growth_rate_computation.GrowthRateComputation"
    ]
    """<p>The growth rate computation configuration.</p>"""
    unique_values: NotRequired[
        "aws_sdk_quicksight.types.unique_values_computation.UniqueValuesComputation"
    ]
    """<p>The unique values computation configuration.</p>"""
    forecast: NotRequired[
        "aws_sdk_quicksight.types.forecast_computation.ForecastComputation"
    ]
    """<p>The forecast computation configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Computation) -> dict:
    out: dict = {}
    if "top_bottom_ranked" in value:
        import aws_sdk_quicksight.types.top_bottom_ranked_computation

        out["TopBottomRanked"] = (
            aws_sdk_quicksight.types.top_bottom_ranked_computation.serialize_json(
                value["top_bottom_ranked"]
            )
        )
    if "top_bottom_movers" in value:
        import aws_sdk_quicksight.types.top_bottom_movers_computation

        out["TopBottomMovers"] = (
            aws_sdk_quicksight.types.top_bottom_movers_computation.serialize_json(
                value["top_bottom_movers"]
            )
        )
    if "total_aggregation" in value:
        import aws_sdk_quicksight.types.total_aggregation_computation

        out["TotalAggregation"] = (
            aws_sdk_quicksight.types.total_aggregation_computation.serialize_json(
                value["total_aggregation"]
            )
        )
    if "maximum_minimum" in value:
        import aws_sdk_quicksight.types.maximum_minimum_computation

        out["MaximumMinimum"] = (
            aws_sdk_quicksight.types.maximum_minimum_computation.serialize_json(
                value["maximum_minimum"]
            )
        )
    if "metric_comparison" in value:
        import aws_sdk_quicksight.types.metric_comparison_computation

        out["MetricComparison"] = (
            aws_sdk_quicksight.types.metric_comparison_computation.serialize_json(
                value["metric_comparison"]
            )
        )
    if "period_over_period" in value:
        import aws_sdk_quicksight.types.period_over_period_computation

        out["PeriodOverPeriod"] = (
            aws_sdk_quicksight.types.period_over_period_computation.serialize_json(
                value["period_over_period"]
            )
        )
    if "period_to_date" in value:
        import aws_sdk_quicksight.types.period_to_date_computation

        out["PeriodToDate"] = (
            aws_sdk_quicksight.types.period_to_date_computation.serialize_json(
                value["period_to_date"]
            )
        )
    if "growth_rate" in value:
        import aws_sdk_quicksight.types.growth_rate_computation

        out["GrowthRate"] = (
            aws_sdk_quicksight.types.growth_rate_computation.serialize_json(
                value["growth_rate"]
            )
        )
    if "unique_values" in value:
        import aws_sdk_quicksight.types.unique_values_computation

        out["UniqueValues"] = (
            aws_sdk_quicksight.types.unique_values_computation.serialize_json(
                value["unique_values"]
            )
        )
    if "forecast" in value:
        import aws_sdk_quicksight.types.forecast_computation

        out["Forecast"] = aws_sdk_quicksight.types.forecast_computation.serialize_json(
            value["forecast"]
        )
    return out


def deserialize_json(data: dict) -> Computation:
    out: Computation = {}  # type: ignore[typeddict-item]
    if "TopBottomRanked" in data:
        import aws_sdk_quicksight.types.top_bottom_ranked_computation

        out["top_bottom_ranked"] = (
            aws_sdk_quicksight.types.top_bottom_ranked_computation.deserialize_json(
                data["TopBottomRanked"]
            )
        )
    if "TopBottomMovers" in data:
        import aws_sdk_quicksight.types.top_bottom_movers_computation

        out["top_bottom_movers"] = (
            aws_sdk_quicksight.types.top_bottom_movers_computation.deserialize_json(
                data["TopBottomMovers"]
            )
        )
    if "TotalAggregation" in data:
        import aws_sdk_quicksight.types.total_aggregation_computation

        out["total_aggregation"] = (
            aws_sdk_quicksight.types.total_aggregation_computation.deserialize_json(
                data["TotalAggregation"]
            )
        )
    if "MaximumMinimum" in data:
        import aws_sdk_quicksight.types.maximum_minimum_computation

        out["maximum_minimum"] = (
            aws_sdk_quicksight.types.maximum_minimum_computation.deserialize_json(
                data["MaximumMinimum"]
            )
        )
    if "MetricComparison" in data:
        import aws_sdk_quicksight.types.metric_comparison_computation

        out["metric_comparison"] = (
            aws_sdk_quicksight.types.metric_comparison_computation.deserialize_json(
                data["MetricComparison"]
            )
        )
    if "PeriodOverPeriod" in data:
        import aws_sdk_quicksight.types.period_over_period_computation

        out["period_over_period"] = (
            aws_sdk_quicksight.types.period_over_period_computation.deserialize_json(
                data["PeriodOverPeriod"]
            )
        )
    if "PeriodToDate" in data:
        import aws_sdk_quicksight.types.period_to_date_computation

        out["period_to_date"] = (
            aws_sdk_quicksight.types.period_to_date_computation.deserialize_json(
                data["PeriodToDate"]
            )
        )
    if "GrowthRate" in data:
        import aws_sdk_quicksight.types.growth_rate_computation

        out["growth_rate"] = (
            aws_sdk_quicksight.types.growth_rate_computation.deserialize_json(
                data["GrowthRate"]
            )
        )
    if "UniqueValues" in data:
        import aws_sdk_quicksight.types.unique_values_computation

        out["unique_values"] = (
            aws_sdk_quicksight.types.unique_values_computation.deserialize_json(
                data["UniqueValues"]
            )
        )
    if "Forecast" in data:
        import aws_sdk_quicksight.types.forecast_computation

        out["forecast"] = (
            aws_sdk_quicksight.types.forecast_computation.deserialize_json(
                data["Forecast"]
            )
        )
    return out
