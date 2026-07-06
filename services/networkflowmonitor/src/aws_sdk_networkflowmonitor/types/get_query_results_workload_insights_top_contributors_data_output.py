"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetQueryResultsWorkloadInsightsTopContributorsDataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.metric_unit
    import aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_data_points


class GetQueryResultsWorkloadInsightsTopContributorsDataOutput(TypedDict, closed=True):
    unit: "aws_sdk_networkflowmonitor.types.metric_unit.MetricUnit"
    """<p>The units for a metric returned by the query.</p>"""
    datapoints: "aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_data_points.WorkloadInsightsTopContributorsDataPoints"
    """<p>The datapoints returned by the query.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: GetQueryResultsWorkloadInsightsTopContributorsDataOutput,
) -> dict:
    out: dict = {}
    import aws_sdk_networkflowmonitor.types.metric_unit

    out["unit"] = aws_sdk_networkflowmonitor.types.metric_unit.serialize_json(
        value["unit"]
    )
    import aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_data_points

    out["datapoints"] = (
        aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_data_points.serialize_json(
            value["datapoints"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(
    data: dict,
) -> GetQueryResultsWorkloadInsightsTopContributorsDataOutput:
    out: GetQueryResultsWorkloadInsightsTopContributorsDataOutput = {}  # type: ignore[typeddict-item]
    if "unit" in data:
        import aws_sdk_networkflowmonitor.types.metric_unit

        out["unit"] = aws_sdk_networkflowmonitor.types.metric_unit.deserialize_json(
            data["unit"]
        )
    else:
        raise DeserializationError(
            "GetQueryResultsWorkloadInsightsTopContributorsDataOutput.unit required"
        )
    if "datapoints" in data:
        import aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_data_points

        out["datapoints"] = (
            aws_sdk_networkflowmonitor.types.workload_insights_top_contributors_data_points.deserialize_json(
                data["datapoints"]
            )
        )
    else:
        raise DeserializationError(
            "GetQueryResultsWorkloadInsightsTopContributorsDataOutput.datapoints required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
