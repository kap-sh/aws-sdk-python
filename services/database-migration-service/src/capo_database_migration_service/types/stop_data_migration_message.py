"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StopDataMigrationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class StopDataMigrationMessage(TypedDict, closed=True):
    data_migration_identifier: "capo_database_migration_service.types.string.String"
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
