"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneMaintenanceScheduleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.auto_tune_maintenance_schedule

AutoTuneMaintenanceScheduleList: TypeAlias = list[
    "aws_sdk_elasticsearch_service.types.auto_tune_maintenance_schedule.AutoTuneMaintenanceSchedule"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneMaintenanceScheduleList) -> list:
    import aws_sdk_elasticsearch_service.types.auto_tune_maintenance_schedule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_elasticsearch_service.types.auto_tune_maintenance_schedule.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutoTuneMaintenanceScheduleList:
    import aws_sdk_elasticsearch_service.types.auto_tune_maintenance_schedule

    out: AutoTuneMaintenanceScheduleList = []
    for item in data:
        out.append(
            aws_sdk_elasticsearch_service.types.auto_tune_maintenance_schedule.deserialize_json(
                item
            )
        )
    return out
