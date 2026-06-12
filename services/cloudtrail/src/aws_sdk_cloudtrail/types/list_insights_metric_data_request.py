"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListInsightsMetricDataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.date
    import aws_sdk_cloudtrail.types.error_code
    import aws_sdk_cloudtrail.types.event_name
    import aws_sdk_cloudtrail.types.event_source
    import aws_sdk_cloudtrail.types.insight_type
    import aws_sdk_cloudtrail.types.insights_metric_data_type
    import aws_sdk_cloudtrail.types.insights_metric_max_results
    import aws_sdk_cloudtrail.types.insights_metric_next_token
    import aws_sdk_cloudtrail.types.insights_metric_period
    import aws_sdk_cloudtrail.types.string


class ListInsightsMetricDataRequest(TypedDict):
    trail_name: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The Amazon Resource Name(ARN) or name of the trail for which you want to retrieve Insights metrics data. This parameter should only be provided to fetch Insights metrics data generated on trails logging data events. This parameter is not required for Insights metric data generated on trails logging management events.</p>"""
    event_source: "aws_sdk_cloudtrail.types.event_source.EventSource"
    """<p>The Amazon Web Services service to which the request was made, such as <code>iam.amazonaws.com</code> or <code>s3.amazonaws.com</code>.</p>"""
    event_name: "aws_sdk_cloudtrail.types.event_name.EventName"
    """<p>The name of the event, typically the Amazon Web Services API on which unusual levels of activity were recorded.</p>"""
    insight_type: "aws_sdk_cloudtrail.types.insight_type.InsightType"
    """<p>The type of CloudTrail Insights event, which is either <code>ApiCallRateInsight</code> or <code>ApiErrorRateInsight</code>. The <code>ApiCallRateInsight</code> Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume. The <code>ApiErrorRateInsight</code> Insights type analyzes management API calls that result in error codes.</p>"""
    error_code: NotRequired["aws_sdk_cloudtrail.types.error_code.ErrorCode"]
    """<p>Conditionally required if the <code>InsightType</code> parameter is set to <code>ApiErrorRateInsight</code>.</p> <p>If returning metrics for the <code>ApiErrorRateInsight</code> Insights type, this is the error to retrieve data for. For example, <code>AccessDenied</code>.</p>"""
    start_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p>Specifies, in UTC, the start time for time-series data. The value specified is inclusive; results include data points with the specified time stamp.</p> <p>The default is 90 days before the time of request.</p>"""
    end_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p>Specifies, in UTC, the end time for time-series data. The value specified is exclusive; results include data points up to the specified time stamp.</p> <p>The default is the time of request.</p>"""
    period: NotRequired[
        "aws_sdk_cloudtrail.types.insights_metric_period.InsightsMetricPeriod"
    ]
    """<p>Granularity of data to retrieve, in seconds. Valid values are <code>60</code>, <code>300</code>, and <code>3600</code>. If you specify any other value, you will get an error. The default is 3600 seconds.</p>"""
    data_type: NotRequired[
        "aws_sdk_cloudtrail.types.insights_metric_data_type.InsightsMetricDataType"
    ]
    """<p>Type of data points to return. Valid values are <code>NonZeroData</code> and <code>FillWithZeros</code>. The default is <code>NonZeroData</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_cloudtrail.types.insights_metric_max_results.InsightsMetricMaxResults"
    ]
    """<p>The maximum number of data points to return. Valid values are integers from 1 to 21600. The default value is 21600.</p>"""
    next_token: NotRequired[
        "aws_sdk_cloudtrail.types.insights_metric_next_token.InsightsMetricNextToken"
    ]
    """<p>Returned if all datapoints can't be returned in a single call. For example, due to reaching <code>MaxResults</code>.</p> <p>Add this parameter to the request to continue retrieving results starting from the last evaluated point.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInsightsMetricDataRequest) -> dict:
    out: dict = {}
    if "trail_name" in value:
        out["TrailName"] = value["trail_name"]
    out["EventSource"] = value["event_source"]
    out["EventName"] = value["event_name"]
    import aws_sdk_cloudtrail.types.insight_type

    out["InsightType"] = aws_sdk_cloudtrail.types.insight_type.serialize_aws_json_1_1(
        value["insight_type"]
    )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "start_time" in value:
        import aws_sdk_cloudtrail.types.date

        out["StartTime"] = aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_cloudtrail.types.date

        out["EndTime"] = aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "period" in value:
        out["Period"] = value["period"]
    if "data_type" in value:
        import aws_sdk_cloudtrail.types.insights_metric_data_type

        out["DataType"] = (
            aws_sdk_cloudtrail.types.insights_metric_data_type.serialize_aws_json_1_1(
                value["data_type"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInsightsMetricDataRequest:
    out: ListInsightsMetricDataRequest = {}  # type: ignore[typeddict-item]
    if "TrailName" in data:
        out["trail_name"] = data["TrailName"]
    if "EventSource" in data:
        out["event_source"] = data["EventSource"]
    else:
        raise DeserializationError(
            "ListInsightsMetricDataRequest.event_source required"
        )
    if "EventName" in data:
        out["event_name"] = data["EventName"]
    else:
        raise DeserializationError("ListInsightsMetricDataRequest.event_name required")
    if "InsightType" in data:
        import aws_sdk_cloudtrail.types.insight_type

        out["insight_type"] = (
            aws_sdk_cloudtrail.types.insight_type.deserialize_aws_json_1_1(
                data["InsightType"]
            )
        )
    else:
        raise DeserializationError(
            "ListInsightsMetricDataRequest.insight_type required"
        )
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "StartTime" in data:
        import aws_sdk_cloudtrail.types.date

        out["start_time"] = aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_cloudtrail.types.date

        out["end_time"] = aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "Period" in data:
        out["period"] = data["Period"]
    if "DataType" in data:
        import aws_sdk_cloudtrail.types.insights_metric_data_type

        out["data_type"] = (
            aws_sdk_cloudtrail.types.insights_metric_data_type.deserialize_aws_json_1_1(
                data["DataType"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
