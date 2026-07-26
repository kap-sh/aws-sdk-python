"""Generated from Smithy shape ``com.amazonaws.xray#GetInsightImpactGraphResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.insight_id
    import capo_xray.types.insight_impact_graph_service_list
    import capo_xray.types.timestamp
    import capo_xray.types.token


class GetInsightImpactGraphResult(TypedDict, closed=True):
    insight_id: NotRequired["capo_xray.types.insight_id.InsightId"]
    """<p>The insight's unique identifier.</p>"""
    start_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The provided start time.</p>"""
    end_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The provided end time. </p>"""
    service_graph_start_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The time, in Unix seconds, at which the service graph started.</p>"""
    service_graph_end_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The time, in Unix seconds, at which the service graph ended.</p>"""
    services: NotRequired[
        "capo_xray.types.insight_impact_graph_service_list.InsightImpactGraphServiceList"
    ]
    """<p>The Amazon Web Services instrumented services related to the insight.</p>"""
    next_token: NotRequired["capo_xray.types.token.Token"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightImpactGraphResult) -> dict:
    out: dict = {}
    if "insight_id" in value:
        out["InsightId"] = value["insight_id"]
    if "start_time" in value:
        import capo_xray.types.timestamp

        out["StartTime"] = capo_xray.types.timestamp.serialize_json(value["start_time"])
    if "end_time" in value:
        import capo_xray.types.timestamp

        out["EndTime"] = capo_xray.types.timestamp.serialize_json(value["end_time"])
    if "service_graph_start_time" in value:
        import capo_xray.types.timestamp

        out["ServiceGraphStartTime"] = capo_xray.types.timestamp.serialize_json(
            value["service_graph_start_time"]
        )
    if "service_graph_end_time" in value:
        import capo_xray.types.timestamp

        out["ServiceGraphEndTime"] = capo_xray.types.timestamp.serialize_json(
            value["service_graph_end_time"]
        )
    if "services" in value:
        import capo_xray.types.insight_impact_graph_service_list

        out["Services"] = (
            capo_xray.types.insight_impact_graph_service_list.serialize_json(
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
        import capo_xray.types.timestamp

        out["start_time"] = capo_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_xray.types.timestamp

        out["end_time"] = capo_xray.types.timestamp.deserialize_json(data["EndTime"])
    if "ServiceGraphStartTime" in data:
        import capo_xray.types.timestamp

        out["service_graph_start_time"] = capo_xray.types.timestamp.deserialize_json(
            data["ServiceGraphStartTime"]
        )
    if "ServiceGraphEndTime" in data:
        import capo_xray.types.timestamp

        out["service_graph_end_time"] = capo_xray.types.timestamp.deserialize_json(
            data["ServiceGraphEndTime"]
        )
    if "Services" in data:
        import capo_xray.types.insight_impact_graph_service_list

        out["services"] = (
            capo_xray.types.insight_impact_graph_service_list.deserialize_json(
                data["Services"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
