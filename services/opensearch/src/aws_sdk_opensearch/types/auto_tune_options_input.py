"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneOptionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.auto_tune_desired_state
    import aws_sdk_opensearch.types.auto_tune_maintenance_schedule_list
    import aws_sdk_opensearch.types.boolean


class AutoTuneOptionsInput(TypedDict):
    desired_state: NotRequired[
        "aws_sdk_opensearch.types.auto_tune_desired_state.AutoTuneDesiredState"
    ]
    """<p>Whether Auto-Tune is enabled or disabled.</p>"""
    maintenance_schedules: NotRequired[
        "aws_sdk_opensearch.types.auto_tune_maintenance_schedule_list.AutoTuneMaintenanceScheduleList"
    ]
    """<p>A list of maintenance schedules during which Auto-Tune can deploy changes. Maintenance windows are deprecated and have been replaced with <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html\">off-peak windows</a>.</p>"""
    use_off_peak_window: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether to schedule Auto-Tune optimizations that require blue/green deployments during the domain's configured daily off-peak window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneOptionsInput) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import aws_sdk_opensearch.types.auto_tune_desired_state

        out["DesiredState"] = (
            aws_sdk_opensearch.types.auto_tune_desired_state.serialize_json(
                value["desired_state"]
            )
        )
    if "maintenance_schedules" in value:
        import aws_sdk_opensearch.types.auto_tune_maintenance_schedule_list

        out["MaintenanceSchedules"] = (
            aws_sdk_opensearch.types.auto_tune_maintenance_schedule_list.serialize_json(
                value["maintenance_schedules"]
            )
        )
    if "use_off_peak_window" in value:
        out["UseOffPeakWindow"] = value["use_off_peak_window"]
    return out


def deserialize_json(data: dict) -> AutoTuneOptionsInput:
    out: AutoTuneOptionsInput = {}  # type: ignore[typeddict-item]
    if "DesiredState" in data:
        import aws_sdk_opensearch.types.auto_tune_desired_state

        out["desired_state"] = (
            aws_sdk_opensearch.types.auto_tune_desired_state.deserialize_json(
                data["DesiredState"]
            )
        )
    if "MaintenanceSchedules" in data:
        import aws_sdk_opensearch.types.auto_tune_maintenance_schedule_list

        out["maintenance_schedules"] = (
            aws_sdk_opensearch.types.auto_tune_maintenance_schedule_list.deserialize_json(
                data["MaintenanceSchedules"]
            )
        )
    if "UseOffPeakWindow" in data:
        out["use_off_peak_window"] = data["UseOffPeakWindow"]
    return out
