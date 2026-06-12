"""Generated from Smithy shape ``com.amazonaws.m2#PendingMaintenance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_m2.types.maintenance_schedule


class PendingMaintenance(TypedDict):
    schedule: NotRequired["aws_sdk_m2.types.maintenance_schedule.MaintenanceSchedule"]
    """<p>The maintenance schedule for the runtime engine version.</p>"""
    engine_version: NotRequired["str"]
    """<p>The specific runtime engine that the maintenance schedule applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PendingMaintenance) -> dict:
    out: dict = {}
    if "schedule" in value:
        import aws_sdk_m2.types.maintenance_schedule

        out["schedule"] = aws_sdk_m2.types.maintenance_schedule.serialize_json(
            value["schedule"]
        )
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    return out


def deserialize_json(data: dict) -> PendingMaintenance:
    out: PendingMaintenance = {}  # type: ignore[typeddict-item]
    if "schedule" in data:
        import aws_sdk_m2.types.maintenance_schedule

        out["schedule"] = aws_sdk_m2.types.maintenance_schedule.deserialize_json(
            data["schedule"]
        )
    if "engineVersion" in data:
        out["engine_version"] = data["engineVersion"]
    return out
