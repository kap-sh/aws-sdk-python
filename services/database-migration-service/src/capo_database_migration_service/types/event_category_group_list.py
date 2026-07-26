"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EventCategoryGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.event_category_group

EventCategoryGroupList: TypeAlias = list[
    "capo_database_migration_service.types.event_category_group.EventCategoryGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventCategoryGroupList) -> list:
    import capo_database_migration_service.types.event_category_group

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.event_category_group.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventCategoryGroupList:
    import capo_database_migration_service.types.event_category_group

    out: EventCategoryGroupList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.event_category_group.deserialize_aws_json_1_1(
                item
            )
        )
    return out
