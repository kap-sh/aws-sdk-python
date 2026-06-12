"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartDataMigrationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.data_migration


class StartDataMigrationResponse(TypedDict):
    data_migration: NotRequired[
        "aws_sdk_database_migration_service.types.data_migration.DataMigration"
    ]
    """<p>The data migration that DMS started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDataMigrationResponse) -> dict:
    out: dict = {}
    if "data_migration" in value:
        import aws_sdk_database_migration_service.types.data_migration

        out["DataMigration"] = (
            aws_sdk_database_migration_service.types.data_migration.serialize_aws_json_1_1(
                value["data_migration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDataMigrationResponse:
    out: StartDataMigrationResponse = {}  # type: ignore[typeddict-item]
    if "DataMigration" in data:
        import aws_sdk_database_migration_service.types.data_migration

        out["data_migration"] = (
            aws_sdk_database_migration_service.types.data_migration.deserialize_aws_json_1_1(
                data["DataMigration"]
            )
        )
    return out
