"""Generated from Smithy shape ``com.amazonaws.xray#GetTimeSeriesServiceStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_xray.errors import DeserializationError

if TYPE_CHECKING:
    import capo_xray.types.entity_selector_expression
    import capo_xray.types.group_arn
    import capo_xray.types.group_name
    import capo_xray.types.nullable_boolean
    import capo_xray.types.nullable_integer
    import capo_xray.types.string
    import capo_xray.types.timestamp


class GetTimeSeriesServiceStatisticsRequest(TypedDict, closed=True):
    start_time: "capo_xray.types.timestamp.Timestamp"
    """<p>The start of the time frame for which to aggregate statistics.</p>"""
    end_time: "capo_xray.types.timestamp.Timestamp"
    """<p>The end of the time frame for which to aggregate statistics.</p>"""
    group_name: NotRequired["capo_xray.types.group_name.GroupName"]
    """<p>The case-sensitive name of the group for which to pull statistics from.</p>"""
    group_arn: NotRequired["capo_xray.types.group_arn.GroupARN"]
    """<p>The Amazon Resource Name (ARN) of the group for which to pull statistics from.</p>"""
    entity_selector_expression: NotRequired[
        "capo_xray.types.entity_selector_expression.EntitySelectorExpression"
    ]
    """<p>A filter expression defining entities that will be aggregated for statistics. Supports ID, service, and edge functions. If no selector expression is specified, edge statistics are returned. </p>"""
    period: NotRequired["capo_xray.types.nullable_integer.NullableInteger"]
    """<p>Aggregation period in seconds.</p>"""
    forecast_statistics: NotRequired["capo_xray.types.nullable_boolean.NullableBoolean"]
    """<p>The forecasted high and low fault count values. Forecast enabled requests require the EntitySelectorExpression ID be provided.</p>"""
    next_token: NotRequired["capo_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTimeSeriesServiceStatisticsRequest) -> dict:
    out: dict = {}
    import capo_xray.types.timestamp

    out["StartTime"] = capo_xray.types.timestamp.serialize_json(value["start_time"])
    import capo_xray.types.timestamp

    out["EndTime"] = capo_xray.types.timestamp.serialize_json(value["end_time"])
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "group_arn" in value:
        out["GroupARN"] = value["group_arn"]
    if "entity_selector_expression" in value:
        out["EntitySelectorExpression"] = value["entity_selector_expression"]
    if "period" in value:
        out["Period"] = value["period"]
    if "forecast_statistics" in value:
        out["ForecastStatistics"] = value["forecast_statistics"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetTimeSeriesServiceStatisticsRequest:
    out: GetTimeSeriesServiceStatisticsRequest = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import capo_xray.types.timestamp

        out["start_time"] = capo_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        raise DeserializationError(
            "GetTimeSeriesServiceStatisticsRequest.start_time required"
        )
    if "EndTime" in data:
        import capo_xray.types.timestamp

        out["end_time"] = capo_xray.types.timestamp.deserialize_json(data["EndTime"])
    else:
        raise DeserializationError(
            "GetTimeSeriesServiceStatisticsRequest.end_time required"
        )
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "GroupARN" in data:
        out["group_arn"] = data["GroupARN"]
    if "EntitySelectorExpression" in data:
        out["entity_selector_expression"] = data["EntitySelectorExpression"]
    if "Period" in data:
        out["period"] = data["Period"]
    if "ForecastStatistics" in data:
        out["forecast_statistics"] = data["ForecastStatistics"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
