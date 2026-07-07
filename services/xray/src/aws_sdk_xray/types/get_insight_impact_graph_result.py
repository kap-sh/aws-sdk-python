"""Generated from Smithy shape ``com.amazonaws.xray#GetInsightImpactGraphResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.insight_id
    import aws_sdk_xray.types.insight_impact_graph_service_list
    import aws_sdk_xray.types.timestamp
    import aws_sdk_xray.types.token


class GetInsightImpactGraphResult(TypedDict, closed=True):
    insight_id: NotRequired["aws_sdk_xray.types.insight_id.InsightId"]
    """<p>The insight's unique identifier.</p>"""
    start_time: NotRequired["aws_sdk_xray.types.timestamp.Timestamp"]
    """<p>The provided start time.</p>"""
    end_time: NotRequired["aws_sdk_xray.types.timestamp.Timestamp"]
    """<p>The provided end time. </p>"""
    service_graph_start_time: NotRequired["aws_sdk_xray.types.timestamp.Timestamp"]
    """<p>The time, in Unix seconds, at which the service graph started.</p>"""
    service_graph_end_time: NotRequired["aws_sdk_xray.types.timestamp.Timestamp"]
    """<p>The time, in Unix seconds, at which the service graph ended.</p>"""
    services: NotRequired[
        "aws_sdk_xray.types.insight_impact_graph_service_list.InsightImpactGraphServiceList"
    ]
    """<p>The Amazon Web Services instrumented services related to the insight.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.token.Token"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightImpactGraphResult) -> dict:
    out: dict = {}
    if "insight_id" in value:
        out["InsightId"] = value["insight_id"]
    if "start_time" in value:
        import aws_sdk_xray.types.timestamp

        out["StartTime"] = aws_sdk_xray.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_xray.types.timestamp

        out["EndTime"] = aws_sdk_xray.types.timestamp.serialize_json(value["end_time"])
    if "service_graph_start_time" in value:
        import aws_sdk_xray.types.timestamp

        out["ServiceGraphStartTime"] = aws_sdk_xray.types.timestamp.serialize_json(
            value["service_graph_start_time"]
        )
    if "service_graph_end_time" in value:
        import aws_sdk_xray.types.timestamp

        out["ServiceGraphEndTime"] = aws_sdk_xray.types.timestamp.serialize_json(
            value["service_graph_end_time"]
        )
    if "services" in value:
        import aws_sdk_xray.types.insight_impact_graph_service_list

        out["Services"] = (
            aws_sdk_xray.types.insight_impact_graph_service_list.serialize_json(
                value["services"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetInsightImpactGraphResult:
    out: GetInsightImpactGraphResult = {}  # type: ignore[typeddict-item]
    if "InsightId" in data:
        out["insight_id"] = data["InsightId"]
    if "StartTime" in data:
        import aws_sdk_xray.types.timestamp

        out["start_time"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_xray.types.timestamp

        out["end_time"] = aws_sdk_xray.types.timestamp.deserialize_json(data["EndTime"])
    if "ServiceGraphStartTime" in data:
        import aws_sdk_xray.types.timestamp

        out["service_graph_start_time"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["ServiceGraphStartTime"]
        )
    if "ServiceGraphEndTime" in data:
        import aws_sdk_xray.types.timestamp

        out["service_graph_end_time"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["ServiceGraphEndTime"]
        )
    if "Services" in data:
        import aws_sdk_xray.types.insight_impact_graph_service_list

        out["services"] = (
            aws_sdk_xray.types.insight_impact_graph_service_list.deserialize_json(
                data["Services"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
