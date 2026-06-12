"""Generated from Smithy shape ``com.amazonaws.medialive#MaintenanceUpdateSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.__string_pattern010920300
    import aws_sdk_medialive.types.maintenance_day


class MaintenanceUpdateSettings(TypedDict):
    maintenance_day: NotRequired[
        "aws_sdk_medialive.types.maintenance_day.MaintenanceDay"
    ]
    """Choose one day of the week for maintenance. The chosen day is used for all future maintenance windows."""
    maintenance_scheduled_date: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Choose a specific date for maintenance to occur. The chosen date is used for the next maintenance window only."""
    maintenance_start_time: NotRequired[
        "aws_sdk_medialive.types.__string_pattern010920300.__stringPattern010920300"
    ]
    """Choose the hour that maintenance will start. The chosen time is used for all future maintenance windows."""


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceUpdateSettings) -> dict:
    out: dict = {}
    if "maintenance_day" in value:
        import aws_sdk_medialive.types.maintenance_day

        out["maintenanceDay"] = aws_sdk_medialive.types.maintenance_day.serialize_json(
            value["maintenance_day"]
        )
    if "maintenance_scheduled_date" in value:
        out["maintenanceScheduledDate"] = value["maintenance_scheduled_date"]
    if "maintenance_start_time" in value:
        out["maintenanceStartTime"] = value["maintenance_start_time"]
    return out


def deserialize_json(data: dict) -> MaintenanceUpdateSettings:
    out: MaintenanceUpdateSettings = {}  # type: ignore[typeddict-item]
    if "maintenanceDay" in data:
        import aws_sdk_medialive.types.maintenance_day

        out["maintenance_day"] = (
            aws_sdk_medialive.types.maintenance_day.deserialize_json(
                data["maintenanceDay"]
            )
        )
    if "maintenanceScheduledDate" in data:
        out["maintenance_scheduled_date"] = data["maintenanceScheduledDate"]
    if "maintenanceStartTime" in data:
        out["maintenance_start_time"] = data["maintenanceStartTime"]
    return out
