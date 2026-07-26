"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.event

EventList: TypeAlias = list["capo_database_migration_service.types.event.Event"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventList) -> list:
    import capo_database_migration_service.types.event

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.event.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventList:
    import capo_database_migration_service.types.event

    out: EventList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.event.deserialize_aws_json_1_1(item)
        )
    return out
