"""Generated from Smithy shape ``com.amazonaws.kendra#GetSnapshotsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.integer
    import aws_sdk_kendra.types.interval
    import aws_sdk_kendra.types.metric_type
    import aws_sdk_kendra.types.next_token


class GetSnapshotsRequest(TypedDict):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index to get search metrics data.</p>"""
    interval: "aws_sdk_kendra.types.interval.Interval"
    """<p>The time interval or time window to get search metrics data. The time interval uses the time zone of your index. You can view data in the following time windows:</p> <ul> <li> <p> <code>THIS_WEEK</code>: The current week, starting on the Sunday and ending on the day before the current date.</p> </li> <li> <p> <code>ONE_WEEK_AGO</code>: The previous week, starting on the Sunday and ending on the following Saturday.</p> </li> <li> <p> <code>TWO_WEEKS_AGO</code>: The week before the previous week, starting on the Sunday and ending on the following Saturday.</p> </li> <li> <p> <code>THIS_MONTH</code>: The current month, starting on the first day of the month and ending on the day before the current date.</p> </li> <li> <p> <code>ONE_MONTH_AGO</code>: The previous month, starting on the first day of the month and ending on the last day of the month.</p> </li> <li> <p> <code>TWO_MONTHS_AGO</code>: The month before the previous month, starting on the first day of the month and ending on last day of the month.</p> </li> </ul>"""
    metric_type: "aws_sdk_kendra.types.metric_type.MetricType"
    r"""<p>The metric you want to retrieve. You can specify only one metric per call.</p> <p>For more information about the metrics you can view, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/search-analytics.html\">Gaining insights with search analytics</a>.</p>"""
    next_token: NotRequired["aws_sdk_kendra.types.next_token.NextToken"]
    """<p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of search metrics data.</p>"""
    max_results: NotRequired["aws_sdk_kendra.types.integer.Integer"]
    """<p>The maximum number of returned data for the metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSnapshotsRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    import aws_sdk_kendra.types.interval

    out["Interval"] = aws_sdk_kendra.types.interval.serialize_aws_json_1_1(
        value["interval"]
    )
    import aws_sdk_kendra.types.metric_type

    out["MetricType"] = aws_sdk_kendra.types.metric_type.serialize_aws_json_1_1(
        value["metric_type"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSnapshotsRequest:
    out: GetSnapshotsRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("GetSnapshotsRequest.index_id required")
    if "Interval" in data:
        import aws_sdk_kendra.types.interval

        out["interval"] = aws_sdk_kendra.types.interval.deserialize_aws_json_1_1(
            data["Interval"]
        )
    else:
        raise DeserializationError("GetSnapshotsRequest.interval required")
    if "MetricType" in data:
        import aws_sdk_kendra.types.metric_type

        out["metric_type"] = aws_sdk_kendra.types.metric_type.deserialize_aws_json_1_1(
            data["MetricType"]
        )
    else:
        raise DeserializationError("GetSnapshotsRequest.metric_type required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
