"""Generated from Smithy shape ``com.amazonaws.internetmonitor#HealthEventsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.local_health_events_config
    import aws_sdk_internetmonitor.types.percentage


class HealthEventsConfig(TypedDict, closed=True):
    availability_score_threshold: "aws_sdk_internetmonitor.types.percentage.Percentage"
    """<p>The health event threshold percentage set for availability scores.</p>"""
    performance_score_threshold: "aws_sdk_internetmonitor.types.percentage.Percentage"
    """<p>The health event threshold percentage set for performance scores.</p>"""
    availability_local_health_events_config: NotRequired[
        "aws_sdk_internetmonitor.types.local_health_events_config.LocalHealthEventsConfig"
    ]
    """<p>The configuration that determines the threshold and other conditions for when Internet Monitor creates a health event for a local availability issue.</p>"""
    performance_local_health_events_config: NotRequired[
        "aws_sdk_internetmonitor.types.local_health_events_config.LocalHealthEventsConfig"
    ]
    """<p>The configuration that determines the threshold and other conditions for when Internet Monitor creates a health event for a local performance issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HealthEventsConfig) -> dict:
    out: dict = {}
    out["AvailabilityScoreThreshold"] = value.get("availability_score_threshold", 0)
    out["PerformanceScoreThreshold"] = value.get("performance_score_threshold", 0)
    if "availability_local_health_events_config" in value:
        import aws_sdk_internetmonitor.types.local_health_events_config

        out["AvailabilityLocalHealthEventsConfig"] = (
            aws_sdk_internetmonitor.types.local_health_events_config.serialize_json(
                value["availability_local_health_events_config"]
            )
        )
    if "performance_local_health_events_config" in value:
        import aws_sdk_internetmonitor.types.local_health_events_config

        out["PerformanceLocalHealthEventsConfig"] = (
            aws_sdk_internetmonitor.types.local_health_events_config.serialize_json(
                value["performance_local_health_events_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> HealthEventsConfig:
    out: HealthEventsConfig = {}  # type: ignore[typeddict-item]
    if "AvailabilityScoreThreshold" in data:
        out["availability_score_threshold"] = data["AvailabilityScoreThreshold"]
    else:
        out["availability_score_threshold"] = 0
    if "PerformanceScoreThreshold" in data:
        out["performance_score_threshold"] = data["PerformanceScoreThreshold"]
    else:
        out["performance_score_threshold"] = 0
    if "AvailabilityLocalHealthEventsConfig" in data:
        import aws_sdk_internetmonitor.types.local_health_events_config

        out["availability_local_health_events_config"] = (
            aws_sdk_internetmonitor.types.local_health_events_config.deserialize_json(
                data["AvailabilityLocalHealthEventsConfig"]
            )
        )
    if "PerformanceLocalHealthEventsConfig" in data:
        import aws_sdk_internetmonitor.types.local_health_events_config

        out["performance_local_health_events_config"] = (
            aws_sdk_internetmonitor.types.local_health_events_config.deserialize_json(
                data["PerformanceLocalHealthEventsConfig"]
            )
        )
    return out
