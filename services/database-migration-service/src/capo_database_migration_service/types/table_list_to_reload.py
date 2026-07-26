"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TableListToReload``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.table_to_reload

TableListToReload: TypeAlias = list[
    "capo_database_migration_service.types.table_to_reload.TableToReload"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableListToReload) -> list:
    import capo_database_migration_service.types.table_to_reload

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.table_to_reload.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TableListToReload:
    import capo_database_migration_service.types.table_to_reload

    out: TableListToReload = []
    for item in data:
        out.append(
            capo_database_migration_service.types.table_to_reload.deserialize_aws_json_1_1(
                item
            )
        )
    return out
