"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskSchedulingConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.end_time
    import aws_sdk_iot_managed_integrations.types.schedule_maintenance_window_list
    import aws_sdk_iot_managed_integrations.types.schedule_start_time
    import aws_sdk_iot_managed_integrations.types.scheduling_config_end_behavior


class OtaTaskSchedulingConfig(TypedDict):
    end_behavior: NotRequired[
        "aws_sdk_iot_managed_integrations.types.scheduling_config_end_behavior.SchedulingConfigEndBehavior"
    ]
    """<p>Specifies the end behavior for all task executions after a task reaches the selected <code>endTime</code>. If <code>endTime</code> is not selected when creating the task, then <code>endBehavior</code> does not apply.</p>"""
    end_time: NotRequired["aws_sdk_iot_managed_integrations.types.end_time.EndTime"]
    """<p>The time an over-the-air (OTA) task will stop.</p>"""
    maintenance_windows: NotRequired[
        "aws_sdk_iot_managed_integrations.types.schedule_maintenance_window_list.ScheduleMaintenanceWindowList"
    ]
    """<p>Maintenance window list for over-the-air (OTA) task scheduling config.</p>"""
    start_time: NotRequired[
        "aws_sdk_iot_managed_integrations.types.schedule_start_time.ScheduleStartTime"
    ]
    """<p>The time an over-the-air (OTA) task will start.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskSchedulingConfig) -> dict:
    out: dict = {}
    if "end_behavior" in value:
        import aws_sdk_iot_managed_integrations.types.scheduling_config_end_behavior

        out["EndBehavior"] = (
            aws_sdk_iot_managed_integrations.types.scheduling_config_end_behavior.serialize_json(
                value["end_behavior"]
            )
        )
    if "end_time" in value:
        out["EndTime"] = value["end_time"]
    if "maintenance_windows" in value:
        import aws_sdk_iot_managed_integrations.types.schedule_maintenance_window_list

        out["MaintenanceWindows"] = (
            aws_sdk_iot_managed_integrations.types.schedule_maintenance_window_list.serialize_json(
                value["maintenance_windows"]
            )
        )
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    return out


def deserialize_json(data: dict) -> OtaTaskSchedulingConfig:
    out: OtaTaskSchedulingConfig = {}  # type: ignore[typeddict-item]
    if "EndBehavior" in data:
        import aws_sdk_iot_managed_integrations.types.scheduling_config_end_behavior

        out["end_behavior"] = (
            aws_sdk_iot_managed_integrations.types.scheduling_config_end_behavior.deserialize_json(
                data["EndBehavior"]
            )
        )
    if "EndTime" in data:
        out["end_time"] = data["EndTime"]
    if "MaintenanceWindows" in data:
        import aws_sdk_iot_managed_integrations.types.schedule_maintenance_window_list

        out["maintenance_windows"] = (
            aws_sdk_iot_managed_integrations.types.schedule_maintenance_window_list.deserialize_json(
                data["MaintenanceWindows"]
            )
        )
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    return out
