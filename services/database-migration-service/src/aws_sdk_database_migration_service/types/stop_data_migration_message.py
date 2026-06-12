"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StopDataMigrationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class StopDataMigrationMessage(TypedDict):
    data_migration_identifier: "aws_sdk_database_migration_service.types.string.String"
    """<p>The identifier (name or ARN) of the data migration to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopDataMigrationMessage) -> dict:
    out: dict = {}
    out["DataMigrationIdentifier"] = value["data_migration_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopDataMigrationMessage:
    out: StopDataMigrationMessage = {}  # type: ignore[typeddict-item]
    if "DataMigrationIdentifier" in data:
        out["data_migration_identifier"] = data["DataMigrationIdentifier"]
    else:
        raise DeserializationError(
            "StopDataMigrationMessage.data_migration_identifier required"
        )
    return out
