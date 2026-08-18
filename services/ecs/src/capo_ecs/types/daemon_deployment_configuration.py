"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.daemon_alarm_configuration
    import capo_ecs.types.daemon_drain_percent
    import capo_ecs.types.integer


class DaemonDeploymentConfiguration(TypedDict, closed=True):
    drain_percent: NotRequired["capo_ecs.types.daemon_drain_percent.DaemonDrainPercent"]
    """<p>The percentage of container instances to drain simultaneously during a daemon deployment. Valid values are between 0.0 and 100.0.</p>"""
    alarms: NotRequired[
        "capo_ecs.types.daemon_alarm_configuration.DaemonAlarmConfiguration"
    ]
    """<p>The CloudWatch alarm configuration for the daemon deployment. When alarms are triggered during a deployment, the deployment can be automatically rolled back.</p>"""
    bake_time_in_minutes: "capo_ecs.types.integer.Integer"
    """<p>The amount of time (in minutes) to wait after a successful deployment step before proceeding. This allows time to monitor for issues before continuing. The default value is 0.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeploymentConfiguration) -> dict:
    out: dict = {}
    if "drain_percent" in value:
        out["drainPercent"] = (
            "NaN"
            if value["drain_percent"] != value["drain_percent"]
            else "Infinity"
            if value["drain_percent"] == float("inf")
            else "-Infinity"
            if value["drain_percent"] == float("-inf")
            else value["drain_percent"]
        )
    if "alarms" in value:
        import capo_ecs.types.daemon_alarm_configuration

        out["alarms"] = (
            capo_ecs.types.daemon_alarm_configuration.serialize_aws_json_1_1(
                value["alarms"]
            )
        )
    out["bakeTimeInMinutes"] = value.get("bake_time_in_minutes", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonDeploymentConfiguration:
    out: DaemonDeploymentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("drainPercent") is not None:
        out["drain_percent"] = float(data["drainPercent"])
    if data.get("alarms") is not None:
        import capo_ecs.types.daemon_alarm_configuration

        out["alarms"] = (
            capo_ecs.types.daemon_alarm_configuration.deserialize_aws_json_1_1(
                data["alarms"]
            )
        )
    if data.get("bakeTimeInMinutes") is not None:
        out["bake_time_in_minutes"] = data["bakeTimeInMinutes"]
    else:
        out["bake_time_in_minutes"] = 0
    return out
