"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InsightSelector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.insight_type
    import aws_sdk_cloudtrail.types.source_event_categories


class InsightSelector(TypedDict):
    insight_type: NotRequired["aws_sdk_cloudtrail.types.insight_type.InsightType"]
    """<p>The type of Insights events to log on a trail or event data store. <code>ApiCallRateInsight</code> and <code>ApiErrorRateInsight</code> are valid Insight types.</p> <p>The <code>ApiCallRateInsight</code> Insights type analyzes write-only management API calls or read and write data API calls that are aggregated per minute against a baseline API call volume.</p> <p>The <code>ApiErrorRateInsight</code> Insights type analyzes management and data API calls that result in error codes. The error is shown if the API call is unsuccessful.</p>"""
    event_categories: NotRequired[
        "aws_sdk_cloudtrail.types.source_event_categories.SourceEventCategories"
    ]
    """<p>Select the event category on which Insights should be enabled. </p> <ul> <li> <p>If EventCategories is not provided, the specified Insights types are enabled on management API calls by default.</p> </li> <li> <p>If EventCategories is provided, the given event categories will overwrite the existing ones. For example, if a trail already has Insights enabled on management events, and then a PutInsightSelectors request is made with only data events specified in EventCategories, Insights on management events will be disabled. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsightSelector) -> dict:
    out: dict = {}
    if "insight_type" in value:
        import aws_sdk_cloudtrail.types.insight_type

        out["InsightType"] = (
            aws_sdk_cloudtrail.types.insight_type.serialize_aws_json_1_1(
                value["insight_type"]
            )
        )
    if "event_categories" in value:
        import aws_sdk_cloudtrail.types.source_event_categories

        out["EventCategories"] = (
            aws_sdk_cloudtrail.types.source_event_categories.serialize_aws_json_1_1(
                value["event_categories"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InsightSelector:
    out: InsightSelector = {}  # type: ignore[typeddict-item]
    if "InsightType" in data:
        import aws_sdk_cloudtrail.types.insight_type

        out["insight_type"] = (
            aws_sdk_cloudtrail.types.insight_type.deserialize_aws_json_1_1(
                data["InsightType"]
            )
        )
    if "EventCategories" in data:
        import aws_sdk_cloudtrail.types.source_event_categories

        out["event_categories"] = (
            aws_sdk_cloudtrail.types.source_event_categories.deserialize_aws_json_1_1(
                data["EventCategories"]
            )
        )
    return out
