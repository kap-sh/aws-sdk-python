"""Generated from Smithy shape ``com.amazonaws.medialive#MaintenanceCreateSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string_pattern010920300
    import capo_medialive.types.maintenance_day


class MaintenanceCreateSettings(TypedDict, closed=True):
    maintenance_day: NotRequired["capo_medialive.types.maintenance_day.MaintenanceDay"]
    """Choose one day of the week for maintenance. The chosen day is used for all future maintenance windows."""
    maintenance_start_time: NotRequired[
        "capo_medialive.types.__string_pattern010920300.__stringPattern010920300"
    ]
    """Choose the hour that maintenance will start. The chosen time is used for all future maintenance windows."""


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceCreateSettings) -> dict:
    out: dict = {}
    if "maintenance_day" in value:
        import capo_medialive.types.maintenance_day

        out["maintenanceDay"] = capo_medialive.types.maintenance_day.serialize_json(
            value["maintenance_day"]
        )
    if "maintenance_start_time" in value:
        out["maintenanceStartTime"] = value["maintenance_start_time"]
    return out


def deserialize_json(data: dict) -> MaintenanceCreateSettings:
    out: MaintenanceCreateSettings = {}  # type: ignore[typeddict-item]
    if "maintenanceDay" in data:
        import capo_medialive.types.maintenance_day

        out["maintenance_day"] = capo_medialive.types.maintenance_day.deserialize_json(
            data["maintenanceDay"]
        )
    if "maintenanceStartTime" in data:
        out["maintenance_start_time"] = data["maintenanceStartTime"]
    return out
