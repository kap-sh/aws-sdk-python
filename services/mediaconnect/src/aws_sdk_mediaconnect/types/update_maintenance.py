"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateMaintenance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.maintenance_day


class UpdateMaintenance(TypedDict):
    maintenance_day: NotRequired[
        "aws_sdk_mediaconnect.types.maintenance_day.MaintenanceDay"
    ]
    """<p> A day of a week when the maintenance will happen.</p>"""
    maintenance_scheduled_date: NotRequired["str"]
    """<p> A scheduled date in ISO UTC format when the maintenance will happen. Use YYYY-MM-DD format. Example: 2021-01-30.</p>"""
    maintenance_start_hour: NotRequired["str"]
    """<p> UTC time when the maintenance will happen. Use 24-hour HH:MM format. Minutes must be 00. Example: 13:00. The default value is 02:00.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMaintenance) -> dict:
    out: dict = {}
    if "maintenance_day" in value:
        import aws_sdk_mediaconnect.types.maintenance_day

        out["maintenanceDay"] = (
            aws_sdk_mediaconnect.types.maintenance_day.serialize_json(
                value["maintenance_day"]
            )
        )
    if "maintenance_scheduled_date" in value:
        out["maintenanceScheduledDate"] = value["maintenance_scheduled_date"]
    if "maintenance_start_hour" in value:
        out["maintenanceStartHour"] = value["maintenance_start_hour"]
    return out


def deserialize_json(data: dict) -> UpdateMaintenance:
    out: UpdateMaintenance = {}  # type: ignore[typeddict-item]
    if "maintenanceDay" in data:
        import aws_sdk_mediaconnect.types.maintenance_day

        out["maintenance_day"] = (
            aws_sdk_mediaconnect.types.maintenance_day.deserialize_json(
                data["maintenanceDay"]
            )
        )
    if "maintenanceScheduledDate" in data:
        out["maintenance_scheduled_date"] = data["maintenanceScheduledDate"]
    if "maintenanceStartHour" in data:
        out["maintenance_start_hour"] = data["maintenanceStartHour"]
    return out
