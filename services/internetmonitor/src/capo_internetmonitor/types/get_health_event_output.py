"""Generated from Smithy shape ``com.amazonaws.internetmonitor#GetHealthEventOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_internetmonitor.types.arn
    import capo_internetmonitor.types.health_event_impact_type
    import capo_internetmonitor.types.health_event_name
    import capo_internetmonitor.types.health_event_status
    import capo_internetmonitor.types.impacted_locations_list
    import capo_internetmonitor.types.percentage


class GetHealthEventOutput(TypedDict, closed=True):
    event_arn: "capo_internetmonitor.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the event.</p>"""
    event_id: "capo_internetmonitor.types.health_event_name.HealthEventName"
    """<p>The internally-generated identifier of a health event.</p>"""
    started_at: "datetime.datetime"
    """<p>The time when a health event started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time when a health event was resolved. If the health event is still active, the end time is not set.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time when a health event was created.</p>"""
    last_updated_at: "datetime.datetime"
    """<p>The time when a health event was last updated or recalculated.</p>"""
    impacted_locations: (
        "capo_internetmonitor.types.impacted_locations_list.ImpactedLocationsList"
    )
    """<p>The locations affected by a health event.</p>"""
    status: "capo_internetmonitor.types.health_event_status.HealthEventStatus"
    """<p>The status of a health event.</p>"""
    percent_of_total_traffic_impacted: NotRequired["float"]
    """<p>The impact on total traffic that a health event has, in increased latency or reduced availability. This is the percentage of how much latency has increased or availability has decreased during the event, compared to what is typical for traffic from this client location to the Amazon Web Services location using this client network.</p>"""
    impact_type: (
        "capo_internetmonitor.types.health_event_impact_type.HealthEventImpactType"
    )
    """<p>The type of impairment of a specific health event.</p>"""
    health_score_threshold: "capo_internetmonitor.types.percentage.Percentage"
    """<p>The threshold percentage for a health score that determines, along with other configuration information, when Internet Monitor creates a health event when there's an internet issue that affects your application end users.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHealthEventOutput) -> dict:
    out: dict = {}
    out["EventArn"] = value["event_arn"]
    out["EventId"] = value["event_id"]
    import capo_internetmonitor.types._prelude.timestamp

    out["StartedAt"] = capo_internetmonitor.types._prelude.timestamp.serialize_json(
        value["started_at"]
    )
    if "ended_at" in value:
        import capo_internetmonitor.types._prelude.timestamp

        out["EndedAt"] = capo_internetmonitor.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    if "created_at" in value:
        import capo_internetmonitor.types._prelude.timestamp

        out["CreatedAt"] = capo_internetmonitor.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    import capo_internetmonitor.types._prelude.timestamp

    out["LastUpdatedAt"] = capo_internetmonitor.types._prelude.timestamp.serialize_json(
        value["last_updated_at"]
    )
    import capo_internetmonitor.types.impacted_locations_list

    out["ImpactedLocations"] = (
        capo_internetmonitor.types.impacted_locations_list.serialize_json(
            value["impacted_locations"]
        )
    )
    out["Status"] = value["status"]
    if "percent_of_total_traffic_impacted" in value:
        out["PercentOfTotalTrafficImpacted"] = value[
            "percent_of_total_traffic_impacted"
        ]
    out["ImpactType"] = value["impact_type"]
    out["HealthScoreThreshold"] = value.get("health_score_threshold", 0)
    return out


def deserialize_json(data: dict) -> GetHealthEventOutput:
    out: GetHealthEventOutput = {}  # type: ignore[typeddict-item]
    if "EventArn" in data:
        out["event_arn"] = data["EventArn"]
    else:
        raise DeserializationError("GetHealthEventOutput.event_arn required")
    if "EventId" in data:
        out["event_id"] = data["EventId"]
    else:
        raise DeserializationError("GetHealthEventOutput.event_id required")
    if "StartedAt" in data:
        import capo_internetmonitor.types._prelude.timestamp

        out["started_at"] = (
            capo_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["StartedAt"]
            )
        )
    else:
        raise DeserializationError("GetHealthEventOutput.started_at required")
    if "EndedAt" in data:
        import capo_internetmonitor.types._prelude.timestamp

        out["ended_at"] = (
            capo_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["EndedAt"]
            )
        )
    if "CreatedAt" in data:
        import capo_internetmonitor.types._prelude.timestamp

        out["created_at"] = (
            capo_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "LastUpdatedAt" in data:
        import capo_internetmonitor.types._prelude.timestamp

        out["last_updated_at"] = (
            capo_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("GetHealthEventOutput.last_updated_at required")
    if "ImpactedLocations" in data:
        import capo_internetmonitor.types.impacted_locations_list

        out["impacted_locations"] = (
            capo_internetmonitor.types.impacted_locations_list.deserialize_json(
                data["ImpactedLocations"]
            )
        )
    else:
        raise DeserializationError("GetHealthEventOutput.impacted_locations required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("GetHealthEventOutput.status required")
    if "PercentOfTotalTrafficImpacted" in data:
        out["percent_of_total_traffic_impacted"] = data["PercentOfTotalTrafficImpacted"]
    if "ImpactType" in data:
        out["impact_type"] = data["ImpactType"]
    else:
        raise DeserializationError("GetHealthEventOutput.impact_type required")
    if "HealthScoreThreshold" in data:
        out["health_score_threshold"] = data["HealthScoreThreshold"]
    else:
        out["health_score_threshold"] = 0
    return out
