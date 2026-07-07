"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ListInsightsMetricDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.error_code
    import aws_sdk_cloudtrail.types.event_name
    import aws_sdk_cloudtrail.types.event_source
    import aws_sdk_cloudtrail.types.insight_type
    import aws_sdk_cloudtrail.types.insights_metric_next_token
    import aws_sdk_cloudtrail.types.insights_metric_values
    import aws_sdk_cloudtrail.types.string
    import aws_sdk_cloudtrail.types.timestamps


class ListInsightsMetricDataResponse(TypedDict, closed=True):
    trail_arn: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Specifies the ARN of the trail. This is only returned when Insights is enabled on a trail logging data events. </p>"""
    event_source: NotRequired["aws_sdk_cloudtrail.types.event_source.EventSource"]
    """<p>The Amazon Web Services service to which the request was made, such as <code>iam.amazonaws.com</code> or <code>s3.amazonaws.com</code>.</p>"""
    event_name: NotRequired["aws_sdk_cloudtrail.types.event_name.EventName"]
    """<p>The name of the event, typically the Amazon Web Services API on which unusual levels of activity were recorded.</p>"""
    insight_type: NotRequired["aws_sdk_cloudtrail.types.insight_type.InsightType"]
    """<p>The type of CloudTrail Insights event, which is either <code>ApiCallRateInsight</code> or <code>ApiErrorRateInsight</code>. The <code>ApiCallRateInsight</code> Insights type analyzes write-only management API calls that are aggregated per minute against a baseline API call volume. The <code>ApiErrorRateInsight</code> Insights type analyzes management API calls that result in error codes.</p>"""
    error_code: NotRequired["aws_sdk_cloudtrail.types.error_code.ErrorCode"]
    """<p>Only returned if <code>InsightType</code> parameter was set to <code>ApiErrorRateInsight</code>.</p> <p>If returning metrics for the <code>ApiErrorRateInsight</code> Insights type, this is the error to retrieve data for. For example, <code>AccessDenied</code>.</p>"""
    timestamps: NotRequired["aws_sdk_cloudtrail.types.timestamps.Timestamps"]
    """<p>List of timestamps at intervals corresponding to the specified time period.</p>"""
    values: NotRequired[
        "aws_sdk_cloudtrail.types.insights_metric_values.InsightsMetricValues"
    ]
    """<p>List of values representing the API call rate or error rate at each timestamp. The number of values is equal to the number of timestamps.</p>"""
    next_token: NotRequired[
        "aws_sdk_cloudtrail.types.insights_metric_next_token.InsightsMetricNextToken"
    ]
    """<p>Only returned if the full results could not be returned in a single query. You can set the <code>NextToken</code> parameter in the next request to this value to continue retrieval.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInsightsMetricDataResponse) -> dict:
    out: dict = {}
    if "trail_arn" in value:
        out["TrailARN"] = value["trail_arn"]
    if "event_source" in value:
        out["EventSource"] = value["event_source"]
    if "event_name" in value:
        out["EventName"] = value["event_name"]
    if "insight_type" in value:
        import aws_sdk_cloudtrail.types.insight_type

        out["InsightType"] = (
            aws_sdk_cloudtrail.types.insight_type.serialize_aws_json_1_1(
                value["insight_type"]
            )
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "timestamps" in value:
        import aws_sdk_cloudtrail.types.timestamps

        out["Timestamps"] = aws_sdk_cloudtrail.types.timestamps.serialize_aws_json_1_1(
            value["timestamps"]
        )
    if "values" in value:
        import aws_sdk_cloudtrail.types.insights_metric_values

        out["Values"] = (
            aws_sdk_cloudtrail.types.insights_metric_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInsightsMetricDataResponse:
    out: ListInsightsMetricDataResponse = {}  # type: ignore[typeddict-item]
    if "TrailARN" in data:
        out["trail_arn"] = data["TrailARN"]
    if "EventSource" in data:
        out["event_source"] = data["EventSource"]
    if "EventName" in data:
        out["event_name"] = data["EventName"]
    if "InsightType" in data:
        import aws_sdk_cloudtrail.types.insight_type

        out["insight_type"] = (
            aws_sdk_cloudtrail.types.insight_type.deserialize_aws_json_1_1(
                data["InsightType"]
            )
        )
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Timestamps" in data:
        import aws_sdk_cloudtrail.types.timestamps

        out["timestamps"] = (
            aws_sdk_cloudtrail.types.timestamps.deserialize_aws_json_1_1(
                data["Timestamps"]
            )
        )
    if "Values" in data:
        import aws_sdk_cloudtrail.types.insights_metric_values

        out["values"] = (
            aws_sdk_cloudtrail.types.insights_metric_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
