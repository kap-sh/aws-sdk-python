"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetInsightSelectorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.event_data_store_arn
    import aws_sdk_cloudtrail.types.insight_selectors
    import aws_sdk_cloudtrail.types.string


class GetInsightSelectorsResponse(TypedDict):
    trail_arn: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of a trail for which you want to get Insights selectors.</p>"""
    insight_selectors: NotRequired[
        "aws_sdk_cloudtrail.types.insight_selectors.InsightSelectors"
    ]
    """<p>Contains the Insights types that are enabled on a trail or event data store. It also specifies the event categories on which a particular Insight type is enabled. <code>ApiCallRateInsight</code> and <code>ApiErrorRateInsight</code> are valid Insight types.The EventCategory field can specify <code>Management</code> or <code>Data</code> events or both. For event data store, you can log Insights for management events only.</p>"""
    event_data_store_arn: NotRequired[
        "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p> The ARN of the source event data store that enabled Insights events. </p>"""
    insights_destination: NotRequired[
        "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p> The ARN of the destination event data store that logs Insights events. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInsightSelectorsResponse) -> dict:
    out: dict = {}
    if "trail_arn" in value:
        out["TrailARN"] = value["trail_arn"]
    if "insight_selectors" in value:
        import aws_sdk_cloudtrail.types.insight_selectors

        out["InsightSelectors"] = (
            aws_sdk_cloudtrail.types.insight_selectors.serialize_aws_json_1_1(
                value["insight_selectors"]
            )
        )
    if "event_data_store_arn" in value:
        out["EventDataStoreArn"] = value["event_data_store_arn"]
    if "insights_destination" in value:
        out["InsightsDestination"] = value["insights_destination"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInsightSelectorsResponse:
    out: GetInsightSelectorsResponse = {}  # type: ignore[typeddict-item]
    if "TrailARN" in data:
        out["trail_arn"] = data["TrailARN"]
    if "InsightSelectors" in data:
        import aws_sdk_cloudtrail.types.insight_selectors

        out["insight_selectors"] = (
            aws_sdk_cloudtrail.types.insight_selectors.deserialize_aws_json_1_1(
                data["InsightSelectors"]
            )
        )
    if "EventDataStoreArn" in data:
        out["event_data_store_arn"] = data["EventDataStoreArn"]
    if "InsightsDestination" in data:
        out["insights_destination"] = data["InsightsDestination"]
    return out
