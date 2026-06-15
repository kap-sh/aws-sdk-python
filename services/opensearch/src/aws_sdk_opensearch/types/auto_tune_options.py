"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.auto_tune_desired_state
    import aws_sdk_opensearch.types.auto_tune_maintenance_schedule_list
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.rollback_on_disable


class AutoTuneOptions(TypedDict):
    desired_state: NotRequired[
        "aws_sdk_opensearch.types.auto_tune_desired_state.AutoTuneDesiredState"
    ]
    """<p>Whether Auto-Tune is enabled or disabled.</p>"""
    rollback_on_disable: NotRequired[
        "aws_sdk_opensearch.types.rollback_on_disable.RollbackOnDisable"
    ]
    """<p>When disabling Auto-Tune, specify <code>NO_ROLLBACK</code> to retain all prior Auto-Tune settings or <code>DEFAULT_ROLLBACK</code> to revert to the OpenSearch Service defaults. If you specify <code>DEFAULT_ROLLBACK</code>, you must include a <code>MaintenanceSchedule</code> in the request. Otherwise, OpenSearch Service is unable to perform the rollback.</p>"""
    maintenance_schedules: NotRequired[
        "aws_sdk_opensearch.types.auto_tune_maintenance_schedule_list.AutoTuneMaintenanceScheduleList"
    ]
    r"""<p>DEPRECATED. Use <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html\">off-peak window</a> instead.</p> <p>A list of maintenance schedules during which Auto-Tune can deploy changes.</p>"""
    use_off_peak_window: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    r"""<p>Whether to use the domain's <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_OffPeakWindow.html\">off-peak window</a> to deploy configuration changes on the domain rather than a maintenance schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneOptions) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import aws_sdk_opensearch.types.auto_tune_desired_state

        out["DesiredState"] = (
            aws_sdk_opensearch.types.auto_tune_desired_state.serialize_json(
                value["desired_state"]
            )
        )
    if "rollback_on_disable" in value:
        import aws_sdk_opensearch.types.rollback_on_disable

        out["RollbackOnDisable"] = (
            aws_sdk_opensearch.types.rollback_on_disable.serialize_json(
                value["rollback_on_disable"]
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


def deserialize_json(data: dict) -> AutoTuneOptions:
    out: AutoTuneOptions = {}  # type: ignore[typeddict-item]
    if "DesiredState" in data:
        import aws_sdk_opensearch.types.auto_tune_desired_state

        out["desired_state"] = (
            aws_sdk_opensearch.types.auto_tune_desired_state.deserialize_json(
                data["DesiredState"]
            )
        )
    if "RollbackOnDisable" in data:
        import aws_sdk_opensearch.types.rollback_on_disable

        out["rollback_on_disable"] = (
            aws_sdk_opensearch.types.rollback_on_disable.deserialize_json(
                data["RollbackOnDisable"]
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
