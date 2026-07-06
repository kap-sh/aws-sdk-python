"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteDataMigrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.data_migration


class DeleteDataMigrationResponse(TypedDict, closed=True):
    data_migration: NotRequired[
        "aws_sdk_database_migration_service.types.data_migration.DataMigration"
    ]
    """<p>The deleted data migration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDataMigrationResponse) -> dict:
    out: dict = {}
    if "data_migration" in value:
        import aws_sdk_database_migration_service.types.data_migration

        out["DataMigration"] = (
            aws_sdk_database_migration_service.types.data_migration.serialize_aws_json_1_1(
                value["data_migration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDataMigrationResponse:
    out: DeleteDataMigrationResponse = {}  # type: ignore[typeddict-item]
    if "DataMigration" in data:
        import aws_sdk_database_migration_service.types.data_migration

        out["data_migration"] = (
            aws_sdk_database_migration_service.types.data_migration.deserialize_aws_json_1_1(
                data["DataMigration"]
            )
        )
    return out
