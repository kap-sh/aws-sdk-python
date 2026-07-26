"""Generated from Smithy shape ``com.amazonaws.xray#Insight``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.anomalous_service_list
    import capo_xray.types.group_arn
    import capo_xray.types.group_name
    import capo_xray.types.insight_category_list
    import capo_xray.types.insight_id
    import capo_xray.types.insight_state
    import capo_xray.types.insight_summary_text
    import capo_xray.types.request_impact_statistics
    import capo_xray.types.service_id
    import capo_xray.types.timestamp


class Insight(TypedDict, closed=True):
    insight_id: NotRequired["capo_xray.types.insight_id.InsightId"]
    """<p>The insights unique identifier. </p>"""
    group_arn: NotRequired["capo_xray.types.group_arn.GroupARN"]
    """<p>The Amazon Resource Name (ARN) of the group that the insight belongs to.</p>"""
    group_name: NotRequired["capo_xray.types.group_name.GroupName"]
    """<p>The name of the group that the insight belongs to.</p>"""
    root_cause_service_id: NotRequired["capo_xray.types.service_id.ServiceId"]
    categories: NotRequired["capo_xray.types.insight_category_list.InsightCategoryList"]
    """<p>The categories that label and describe the type of insight.</p>"""
    state: NotRequired["capo_xray.types.insight_state.InsightState"]
    """<p>The current state of the insight.</p>"""
    start_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The time, in Unix seconds, at which the insight began.</p>"""
    end_time: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The time, in Unix seconds, at which the insight ended.</p>"""
    summary: NotRequired["capo_xray.types.insight_summary_text.InsightSummaryText"]
    """<p>A brief description of the insight.</p>"""
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
    """<p>The service within the insight that is most impacted by the incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Insight) -> dict:
    out: dict = {}
    if "insight_id" in value:
        out["InsightId"] = value["insight_id"]
    if "group_arn" in value:
        out["GroupARN"] = value["group_arn"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "root_cause_service_id" in value:
        import capo_xray.types.service_id

        out["RootCauseServiceId"] = capo_xray.types.service_id.serialize_json(
            value["root_cause_service_id"]
        )
    if "categories" in value:
        import capo_xray.types.insight_category_list

        out["Categories"] = capo_xray.types.insight_category_list.serialize_json(
            value["categories"]
        )
    if "state" in value:
        import capo_xray.types.insight_state

        out["State"] = capo_xray.types.insight_state.serialize_json(value["state"])
    if "start_time" in value:
        import capo_xray.types.timestamp

        out["StartTime"] = capo_xray.types.timestamp.serialize_json(value["start_time"])
    if "end_time" in value:
        import capo_xray.types.timestamp

        out["EndTime"] = capo_xray.types.timestamp.serialize_json(value["end_time"])
    if "summary" in value:
        out["Summary"] = value["summary"]
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


def deserialize_json(data: dict) -> Insight:
    out: Insight = {}  # type: ignore[typeddict-item]
    if "InsightId" in data:
        out["insight_id"] = data["InsightId"]
    if "GroupARN" in data:
        out["group_arn"] = data["GroupARN"]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "RootCauseServiceId" in data:
        import capo_xray.types.service_id

        out["root_cause_service_id"] = capo_xray.types.service_id.deserialize_json(
            data["RootCauseServiceId"]
        )
    if "Categories" in data:
        import capo_xray.types.insight_category_list

        out["categories"] = capo_xray.types.insight_category_list.deserialize_json(
            data["Categories"]
        )
    if "State" in data:
        import capo_xray.types.insight_state

        out["state"] = capo_xray.types.insight_state.deserialize_json(data["State"])
    if "StartTime" in data:
        import capo_xray.types.timestamp

        out["start_time"] = capo_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_xray.types.timestamp

        out["end_time"] = capo_xray.types.timestamp.deserialize_json(data["EndTime"])
    if "Summary" in data:
        out["summary"] = data["Summary"]
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
