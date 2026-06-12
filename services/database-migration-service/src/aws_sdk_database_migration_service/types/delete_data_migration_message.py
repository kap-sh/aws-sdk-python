"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteDataMigrationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class DeleteDataMigrationMessage(TypedDict):
    data_migration_identifier: "aws_sdk_database_migration_service.types.string.String"
    """<p>The identifier (name or ARN) of the data migration to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDataMigrationMessage) -> dict:
    out: dict = {}
    out["DataMigrationIdentifier"] = value["data_migration_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDataMigrationMessage:
    out: DeleteDataMigrationMessage = {}  # type: ignore[typeddict-item]
    if "DataMigrationIdentifier" in data:
        out["data_migration_identifier"] = data["DataMigrationIdentifier"]
    else:
        raise DeserializationError(
            "DeleteDataMigrationMessage.data_migration_identifier required"
        )
    return out
