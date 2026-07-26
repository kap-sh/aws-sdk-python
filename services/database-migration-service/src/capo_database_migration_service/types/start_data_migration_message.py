"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartDataMigrationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.start_replication_migration_type_value
    import capo_database_migration_service.types.string


class StartDataMigrationMessage(TypedDict, closed=True):
    data_migration_identifier: "capo_database_migration_service.types.string.String"
    """<p>The identifier (name or ARN) of the data migration to start.</p>"""
    start_type: "capo_database_migration_service.types.start_replication_migration_type_value.StartReplicationMigrationTypeValue"
    """<p>Specifies the start type for the data migration. Valid values include <code>start-replication</code>, <code>reload-target</code>, and <code>resume-processing</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDataMigrationMessage) -> dict:
    out: dict = {}
    out["DataMigrationIdentifier"] = value["data_migration_identifier"]
    import capo_database_migration_service.types.start_replication_migration_type_value

    out["StartType"] = (
        capo_database_migration_service.types.start_replication_migration_type_value.serialize_aws_json_1_1(
            value["start_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartDataMigrationMessage:
    out: StartDataMigrationMessage = {}  # type: ignore[typeddict-item]
    if "DataMigrationIdentifier" in data:
        out["data_migration_identifier"] = data["DataMigrationIdentifier"]
    else:
        raise DeserializationError(
            "StartDataMigrationMessage.data_migration_identifier required"
        )
    if "StartType" in data:
        import capo_database_migration_service.types.start_replication_migration_type_value

        out["start_type"] = (
            capo_database_migration_service.types.start_replication_migration_type_value.deserialize_aws_json_1_1(
                data["StartType"]
            )
        )
    else:
        raise DeserializationError("StartDataMigrationMessage.start_type required")
    return out
