"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DatabaseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.database_response

DatabaseList: TypeAlias = list[
    "capo_database_migration_service.types.database_response.DatabaseResponse"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseList) -> list:
    import capo_database_migration_service.types.database_response

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.database_response.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DatabaseList:
    import capo_database_migration_service.types.database_response

    out: DatabaseList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.database_response.deserialize_aws_json_1_1(
                item
            )
        )
    return out
