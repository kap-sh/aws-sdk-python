"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddMaintenance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.maintenance_day


class AddMaintenance(TypedDict, closed=True):
    maintenance_day: NotRequired[
        "aws_sdk_mediaconnect.types.maintenance_day.MaintenanceDay"
    ]
    """<p> A day of a week when the maintenance will happen. </p>"""
    maintenance_start_hour: NotRequired["str"]
    """<p> UTC time when the maintenance will happen. </p> <p>Use 24-hour HH:MM format. </p> <p>Minutes must be 00. </p> <p>Example: 13:00. </p> <p>The default value is 02:00.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddMaintenance) -> dict:
    out: dict = {}
    if "maintenance_day" in value:
        import aws_sdk_mediaconnect.types.maintenance_day

        out["maintenanceDay"] = (
            aws_sdk_mediaconnect.types.maintenance_day.serialize_json(
                value["maintenance_day"]
            )
        )
    if "maintenance_start_hour" in value:
        out["maintenanceStartHour"] = value["maintenance_start_hour"]
    return out


def deserialize_json(data: dict) -> AddMaintenance:
    out: AddMaintenance = {}  # type: ignore[typeddict-item]
    if "maintenanceDay" in data:
        import aws_sdk_mediaconnect.types.maintenance_day

        out["maintenance_day"] = (
            aws_sdk_mediaconnect.types.maintenance_day.deserialize_json(
                data["maintenanceDay"]
            )
        )
    if "maintenanceStartHour" in data:
        out["maintenance_start_hour"] = data["maintenanceStartHour"]
    return out
