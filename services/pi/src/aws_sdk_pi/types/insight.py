"""Generated from Smithy shape ``com.amazonaws.pi#Insight``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pi.types.context_type
    import aws_sdk_pi.types.data_list
    import aws_sdk_pi.types.insight_list
    import aws_sdk_pi.types.iso_timestamp
    import aws_sdk_pi.types.markdown_string
    import aws_sdk_pi.types.recommendation_list
    import aws_sdk_pi.types.severity
    import aws_sdk_pi.types.string


class Insight(TypedDict):
    insight_id: "aws_sdk_pi.types.string.String"
    """<p>The unique identifier for the insight. For example, <code>insight-12345678901234567</code>.</p>"""
    insight_type: NotRequired["aws_sdk_pi.types.string.String"]
    """<p>The type of insight. For example, <code>HighDBLoad</code>, <code>HighCPU</code>, or <code>DominatingSQLs</code>.</p>"""
    context: NotRequired["aws_sdk_pi.types.context_type.ContextType"]
    """<p>Indicates if the insight is causal or correlated insight.</p>"""
    start_time: NotRequired["aws_sdk_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The start time of the insight. For example, <code>2018-10-30T00:00:00Z</code>.</p>"""
    end_time: NotRequired["aws_sdk_pi.types.iso_timestamp.ISOTimestamp"]
    """<p>The end time of the insight. For example, <code>2018-10-30T00:00:00Z</code>.</p>"""
    severity: NotRequired["aws_sdk_pi.types.severity.Severity"]
    """<p>The severity of the insight. The values are: <code>Low</code>, <code>Medium</code>, or <code>High</code>.</p>"""
    supporting_insights: NotRequired["aws_sdk_pi.types.insight_list.InsightList"]
    """<p>List of supporting insights that provide additional factors for the insight.</p>"""
    description: NotRequired["aws_sdk_pi.types.markdown_string.MarkdownString"]
    """<p>Description of the insight. For example: <code>A high severity Insight found between 02:00 to 02:30, where there was an unusually high DB load 600x above baseline. Likely performance impact</code>.</p>"""
    recommendations: NotRequired[
        "aws_sdk_pi.types.recommendation_list.RecommendationList"
    ]
    """<p>List of recommendations for the insight. For example, <code>Investigate the following SQLs that contributed to 100% of the total DBLoad during that time period: sql-id</code>.</p>"""
    insight_data: NotRequired["aws_sdk_pi.types.data_list.DataList"]
    """<p>List of data objects containing metrics and references from the time range while generating the insight.</p>"""
    baseline_data: NotRequired["aws_sdk_pi.types.data_list.DataList"]
    """<p> Metric names and values from the timeframe used as baseline to generate the insight.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Insight) -> dict:
    out: dict = {}
    out["InsightId"] = value["insight_id"]
    if "insight_type" in value:
        out["InsightType"] = value["insight_type"]
    if "context" in value:
        import aws_sdk_pi.types.context_type

        out["Context"] = aws_sdk_pi.types.context_type.serialize_aws_json_1_1(
            value["context"]
        )
    if "start_time" in value:
        import aws_sdk_pi.types.iso_timestamp

        out["StartTime"] = aws_sdk_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_pi.types.iso_timestamp

        out["EndTime"] = aws_sdk_pi.types.iso_timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "severity" in value:
        import aws_sdk_pi.types.severity

        out["Severity"] = aws_sdk_pi.types.severity.serialize_aws_json_1_1(
            value["severity"]
        )
    if "supporting_insights" in value:
        import aws_sdk_pi.types.insight_list

        out["SupportingInsights"] = (
            aws_sdk_pi.types.insight_list.serialize_aws_json_1_1(
                value["supporting_insights"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "recommendations" in value:
        import aws_sdk_pi.types.recommendation_list

        out["Recommendations"] = (
            aws_sdk_pi.types.recommendation_list.serialize_aws_json_1_1(
                value["recommendations"]
            )
        )
    if "insight_data" in value:
        import aws_sdk_pi.types.data_list

        out["InsightData"] = aws_sdk_pi.types.data_list.serialize_aws_json_1_1(
            value["insight_data"]
        )
    if "baseline_data" in value:
        import aws_sdk_pi.types.data_list

        out["BaselineData"] = aws_sdk_pi.types.data_list.serialize_aws_json_1_1(
            value["baseline_data"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Insight:
    out: Insight = {}  # type: ignore[typeddict-item]
    if "InsightId" in data:
        out["insight_id"] = data["InsightId"]
    else:
        raise DeserializationError("Insight.insight_id required")
    if "InsightType" in data:
        out["insight_type"] = data["InsightType"]
    if "Context" in data:
        import aws_sdk_pi.types.context_type

        out["context"] = aws_sdk_pi.types.context_type.deserialize_aws_json_1_1(
            data["Context"]
        )
    if "StartTime" in data:
        import aws_sdk_pi.types.iso_timestamp

        out["start_time"] = aws_sdk_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_pi.types.iso_timestamp

        out["end_time"] = aws_sdk_pi.types.iso_timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "Severity" in data:
        import aws_sdk_pi.types.severity

        out["severity"] = aws_sdk_pi.types.severity.deserialize_aws_json_1_1(
            data["Severity"]
        )
    if "SupportingInsights" in data:
        import aws_sdk_pi.types.insight_list

        out["supporting_insights"] = (
            aws_sdk_pi.types.insight_list.deserialize_aws_json_1_1(
                data["SupportingInsights"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Recommendations" in data:
        import aws_sdk_pi.types.recommendation_list

        out["recommendations"] = (
            aws_sdk_pi.types.recommendation_list.deserialize_aws_json_1_1(
                data["Recommendations"]
            )
        )
    if "InsightData" in data:
        import aws_sdk_pi.types.data_list

        out["insight_data"] = aws_sdk_pi.types.data_list.deserialize_aws_json_1_1(
            data["InsightData"]
        )
    if "BaselineData" in data:
        import aws_sdk_pi.types.data_list

        out["baseline_data"] = aws_sdk_pi.types.data_list.deserialize_aws_json_1_1(
            data["BaselineData"]
        )
    return out
