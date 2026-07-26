"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneMaintenanceScheduleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.auto_tune_maintenance_schedule

AutoTuneMaintenanceScheduleList: TypeAlias = list[
    "capo_opensearch.types.auto_tune_maintenance_schedule.AutoTuneMaintenanceSchedule"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneMaintenanceScheduleList) -> list:
    import capo_opensearch.types.auto_tune_maintenance_schedule

    out: list = []
    for item in value:
        out.append(
            capo_opensearch.types.auto_tune_maintenance_schedule.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutoTuneMaintenanceScheduleList:
    import capo_opensearch.types.auto_tune_maintenance_schedule

    out: AutoTuneMaintenanceScheduleList = []
    for item in data:
        out.append(
            capo_opensearch.types.auto_tune_maintenance_schedule.deserialize_json(item)
        )
    return out
