"""Generated from Smithy shape ``com.amazonaws.internetmonitor#HealthEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_internetmonitor.types.arn
    import aws_sdk_internetmonitor.types.health_event_impact_type
    import aws_sdk_internetmonitor.types.health_event_name
    import aws_sdk_internetmonitor.types.health_event_status
    import aws_sdk_internetmonitor.types.impacted_locations_list
    import aws_sdk_internetmonitor.types.percentage


class HealthEvent(TypedDict):
    event_arn: "aws_sdk_internetmonitor.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the event.</p>"""
    event_id: "aws_sdk_internetmonitor.types.health_event_name.HealthEventName"
    """<p>The internally-generated identifier of a specific network traffic impairment health event.</p>"""
    started_at: "datetime.datetime"
    """<p>When a health event started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time when a health event ended. If the health event is still active, then the end time is not set.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>When the health event was created.</p>"""
    last_updated_at: "datetime.datetime"
    """<p>When the health event was last updated.</p>"""
    impacted_locations: (
        "aws_sdk_internetmonitor.types.impacted_locations_list.ImpactedLocationsList"
    )
    """<p>The locations impacted by the health event.</p>"""
    status: "aws_sdk_internetmonitor.types.health_event_status.HealthEventStatus"
    """<p>The status of a health event.</p>"""
    percent_of_total_traffic_impacted: NotRequired["float"]
    """<p>The impact on total traffic that a health event has, in increased latency or reduced availability. This is the percentage of how much latency has increased or availability has decreased during the event, compared to what is typical for traffic from this client location to the Amazon Web Services location using this client network.</p>"""
    impact_type: (
        "aws_sdk_internetmonitor.types.health_event_impact_type.HealthEventImpactType"
    )
    """<p>The type of impairment for a health event.</p>"""
    health_score_threshold: "aws_sdk_internetmonitor.types.percentage.Percentage"
    """<p>The value of the threshold percentage for performance or availability that was configured when Amazon CloudWatch Internet Monitor created the health event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HealthEvent) -> dict:
    out: dict = {}
    out["EventArn"] = value["event_arn"]
    out["EventId"] = value["event_id"]
    import aws_sdk_internetmonitor.types._prelude.timestamp

    out["StartedAt"] = aws_sdk_internetmonitor.types._prelude.timestamp.serialize_json(
        value["started_at"]
    )
    if "ended_at" in value:
        import aws_sdk_internetmonitor.types._prelude.timestamp

        out["EndedAt"] = (
            aws_sdk_internetmonitor.types._prelude.timestamp.serialize_json(
                value["ended_at"]
            )
        )
    if "created_at" in value:
        import aws_sdk_internetmonitor.types._prelude.timestamp

        out["CreatedAt"] = (
            aws_sdk_internetmonitor.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    import aws_sdk_internetmonitor.types._prelude.timestamp

    out["LastUpdatedAt"] = (
        aws_sdk_internetmonitor.types._prelude.timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    import aws_sdk_internetmonitor.types.impacted_locations_list

    out["ImpactedLocations"] = (
        aws_sdk_internetmonitor.types.impacted_locations_list.serialize_json(
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


def deserialize_json(data: dict) -> HealthEvent:
    out: HealthEvent = {}  # type: ignore[typeddict-item]
    if "EventArn" in data:
        out["event_arn"] = data["EventArn"]
    else:
        raise DeserializationError("HealthEvent.event_arn required")
    if "EventId" in data:
        out["event_id"] = data["EventId"]
    else:
        raise DeserializationError("HealthEvent.event_id required")
    if "StartedAt" in data:
        import aws_sdk_internetmonitor.types._prelude.timestamp

        out["started_at"] = (
            aws_sdk_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["StartedAt"]
            )
        )
    else:
        raise DeserializationError("HealthEvent.started_at required")
    if "EndedAt" in data:
        import aws_sdk_internetmonitor.types._prelude.timestamp

        out["ended_at"] = (
            aws_sdk_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["EndedAt"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_internetmonitor.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_internetmonitor.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("HealthEvent.last_updated_at required")
    if "ImpactedLocations" in data:
        import aws_sdk_internetmonitor.types.impacted_locations_list

        out["impacted_locations"] = (
            aws_sdk_internetmonitor.types.impacted_locations_list.deserialize_json(
                data["ImpactedLocations"]
            )
        )
    else:
        raise DeserializationError("HealthEvent.impacted_locations required")
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("HealthEvent.status required")
    if "PercentOfTotalTrafficImpacted" in data:
        out["percent_of_total_traffic_impacted"] = data["PercentOfTotalTrafficImpacted"]
    if "ImpactType" in data:
        out["impact_type"] = data["ImpactType"]
    else:
        raise DeserializationError("HealthEvent.impact_type required")
    if "HealthScoreThreshold" in data:
        out["health_score_threshold"] = data["HealthScoreThreshold"]
    else:
        out["health_score_threshold"] = 0
    return out
