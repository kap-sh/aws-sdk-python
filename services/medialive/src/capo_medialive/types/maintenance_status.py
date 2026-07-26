"""Generated from Smithy shape ``com.amazonaws.medialive#MaintenanceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.maintenance_day


class MaintenanceStatus(TypedDict, closed=True):
    maintenance_day: NotRequired["capo_medialive.types.maintenance_day.MaintenanceDay"]
    """The currently selected maintenance day."""
    maintenance_deadline: NotRequired["capo_medialive.types.__string.__string"]
    """Maintenance is required by the displayed date and time. Date and time is in ISO."""
    maintenance_scheduled_date: NotRequired["capo_medialive.types.__string.__string"]
    """The currently scheduled maintenance date and time. Date and time is in ISO."""
    maintenance_start_time: NotRequired["capo_medialive.types.__string.__string"]
    """The currently selected maintenance start time. Time is in UTC."""


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceStatus) -> dict:
    out: dict = {}
    if "maintenance_day" in value:
        import capo_medialive.types.maintenance_day

        out["maintenanceDay"] = capo_medialive.types.maintenance_day.serialize_json(
            value["maintenance_day"]
        )
    if "maintenance_deadline" in value:
        out["maintenanceDeadline"] = value["maintenance_deadline"]
    if "maintenance_scheduled_date" in value:
        out["maintenanceScheduledDate"] = value["maintenance_scheduled_date"]
    if "maintenance_start_time" in value:
        out["maintenanceStartTime"] = value["maintenance_start_time"]
    return out


def deserialize_json(data: dict) -> MaintenanceStatus:
    out: MaintenanceStatus = {}  # type: ignore[typeddict-item]
    if "maintenanceDay" in data:
        import capo_medialive.types.maintenance_day

        out["maintenance_day"] = capo_medialive.types.maintenance_day.deserialize_json(
            data["maintenanceDay"]
        )
    if "maintenanceDeadline" in data:
        out["maintenance_deadline"] = data["maintenanceDeadline"]
    if "maintenanceScheduledDate" in data:
        out["maintenance_scheduled_date"] = data["maintenanceScheduledDate"]
    if "maintenanceStartTime" in data:
        out["maintenance_start_time"] = data["maintenanceStartTime"]
    return out
