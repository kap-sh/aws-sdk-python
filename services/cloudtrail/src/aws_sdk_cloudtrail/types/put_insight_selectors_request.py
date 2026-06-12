"""Generated from Smithy shape ``com.amazonaws.cloudtrail#PutInsightSelectorsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.event_data_store_arn
    import aws_sdk_cloudtrail.types.insight_selectors
    import aws_sdk_cloudtrail.types.string


class PutInsightSelectorsRequest(TypedDict):
    trail_name: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The name of the CloudTrail trail for which you want to change or add Insights selectors.</p> <p>You cannot use this parameter with the <code>EventDataStore</code> and <code>InsightsDestination</code> parameters.</p>"""
    insight_selectors: "aws_sdk_cloudtrail.types.insight_selectors.InsightSelectors"
    """<p>Contains the Insights types you want to log on a specific category of events on a trail or event data store. <code>ApiCallRateInsight</code> and <code>ApiErrorRateInsight</code> are valid Insight types.The EventCategory field can specify <code>Management</code> or <code>Data</code> events or both. For event data store, you can log Insights for management events only.</p> <p>The <code>ApiCallRateInsight</code> Insights type analyzes write-only management API calls or read and write data API calls that are aggregated per minute against a baseline API call volume.</p> <p>The <code>ApiErrorRateInsight</code> Insights type analyzes management and data API calls that result in error codes. The error is shown if the API call is unsuccessful.</p>"""
    event_data_store: NotRequired[
        "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p>The ARN (or ID suffix of the ARN) of the source event data store for which you want to change or add Insights selectors. To enable Insights on an event data store, you must provide both the <code>EventDataStore</code> and <code>InsightsDestination</code> parameters.</p> <p>You cannot use this parameter with the <code>TrailName</code> parameter.</p>"""
    insights_destination: NotRequired[
        "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p> The ARN (or ID suffix of the ARN) of the destination event data store that logs Insights events. To enable Insights on an event data store, you must provide both the <code>EventDataStore</code> and <code>InsightsDestination</code> parameters. </p> <p>You cannot use this parameter with the <code>TrailName</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutInsightSelectorsRequest) -> dict:
    out: dict = {}
    if "trail_name" in value:
        out["TrailName"] = value["trail_name"]
    import aws_sdk_cloudtrail.types.insight_selectors

    out["InsightSelectors"] = (
        aws_sdk_cloudtrail.types.insight_selectors.serialize_aws_json_1_1(
            value["insight_selectors"]
        )
    )
    if "event_data_store" in value:
        out["EventDataStore"] = value["event_data_store"]
    if "insights_destination" in value:
        out["InsightsDestination"] = value["insights_destination"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutInsightSelectorsRequest:
    out: PutInsightSelectorsRequest = {}  # type: ignore[typeddict-item]
    if "TrailName" in data:
        out["trail_name"] = data["TrailName"]
    if "InsightSelectors" in data:
        import aws_sdk_cloudtrail.types.insight_selectors

        out["insight_selectors"] = (
            aws_sdk_cloudtrail.types.insight_selectors.deserialize_aws_json_1_1(
                data["InsightSelectors"]
            )
        )
    else:
        raise DeserializationError(
            "PutInsightSelectorsRequest.insight_selectors required"
        )
    if "EventDataStore" in data:
        out["event_data_store"] = data["EventDataStore"]
    if "InsightsDestination" in data:
        out["insights_destination"] = data["InsightsDestination"]
    return out
