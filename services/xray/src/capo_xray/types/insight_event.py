"""Generated from Smithy shape ``com.amazonaws.xray#InsightEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.anomalous_service_list
    import capo_xray.types.event_summary_text
    import capo_xray.types.request_impact_statistics
    import capo_xray.types.timestamp


class InsightEvent(TypedDict, closed=True):
    summary: NotRequired["capo_xray.types.event_summary_text.EventSummaryText"]
    """<p>A brief description of the event.</p>"""
    event_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The time, in Unix seconds, at which the event was recorded.</p>"""
    client_request_impact_statistics: NotRequired[
        "capo_xray.types.request_impact_statistics.RequestImpactStatistics"
    ]
    """<p>The impact statistics of the client side service. This includes the number of requests to the client service and whether the requests were faults or okay.</p>"""
    root_cause_service_request_impact_statistics: NotRequired[
        "capo_xray.types.request_impact_statistics.RequestImpactStatistics"
    ]
    """<p>The impact statistics of the root cause service. This includes the number of requests to the client service and whether the requests were faults or okay.</p>"""
    top_anomalous_services: NotRequired[
        "capo_xray.types.anomalous_service_list.AnomalousServiceList"
    ]
    """<p>The service during the event that is most impacted by the incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightEvent) -> dict:
    out: dict = {}
    if "summary" in value:
        out["Summary"] = value["summary"]
    if "event_time" in value:
        import capo_xray.types.timestamp

        out["EventTime"] = capo_xray.types.timestamp.serialize_json(value["event_time"])
    if "client_request_impact_statistics" in value:
        import capo_xray.types.request_impact_statistics

        out["ClientRequestImpactStatistics"] = (
            capo_xray.types.request_impact_statistics.serialize_json(
                value["client_request_impact_statistics"]
            )
        )
    if "root_cause_service_request_impact_statistics" in value:
        import capo_xray.types.request_impact_statistics

        out["RootCauseServiceRequestImpactStatistics"] = (
            capo_xray.types.request_impact_statistics.serialize_json(
                value["root_cause_service_request_impact_statistics"]
            )
        )
    if "top_anomalous_services" in value:
        import capo_xray.types.anomalous_service_list

        out["TopAnomalousServices"] = (
            capo_xray.types.anomalous_service_list.serialize_json(
                value["top_anomalous_services"]
            )
        )
    return out


def deserialize_json(data: dict) -> InsightEvent:
    out: InsightEvent = {}  # type: ignore[typeddict-item]
    if "Summary" in data:
        out["summary"] = data["Summary"]
    if "EventTime" in data:
        import capo_xray.types.timestamp

        out["event_time"] = capo_xray.types.timestamp.deserialize_json(
            data["EventTime"]
        )
    if "ClientRequestImpactStatistics" in data:
        import capo_xray.types.request_impact_statistics

        out["client_request_impact_statistics"] = (
            capo_xray.types.request_impact_statistics.deserialize_json(
                data["ClientRequestImpactStatistics"]
            )
        )
    if "RootCauseServiceRequestImpactStatistics" in data:
        import capo_xray.types.request_impact_statistics

        out["root_cause_service_request_impact_statistics"] = (
            capo_xray.types.request_impact_statistics.deserialize_json(
                data["RootCauseServiceRequestImpactStatistics"]
            )
        )
    if "TopAnomalousServices" in data:
        import capo_xray.types.anomalous_service_list

        out["top_anomalous_services"] = (
            capo_xray.types.anomalous_service_list.deserialize_json(
                data["TopAnomalousServices"]
            )
        )
    return out
