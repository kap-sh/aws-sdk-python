"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ScheduleMaintenanceWindowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.schedule_maintenance_window

ScheduleMaintenanceWindowList: TypeAlias = list[
    "capo_iot_managed_integrations.types.schedule_maintenance_window.ScheduleMaintenanceWindow"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleMaintenanceWindowList) -> list:
    import capo_iot_managed_integrations.types.schedule_maintenance_window

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.schedule_maintenance_window.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ScheduleMaintenanceWindowList:
    import capo_iot_managed_integrations.types.schedule_maintenance_window

    out: ScheduleMaintenanceWindowList = []
    for item in data:
        out.append(
            capo_iot_managed_integrations.types.schedule_maintenance_window.deserialize_json(
                item
            )
        )
    return out
