"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#DatabaseMigrationPreference``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_migrationhubstrategy.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.heterogeneous
    import aws_sdk_migrationhubstrategy.types.homogeneous
    import aws_sdk_migrationhubstrategy.types.no_database_migration_preference


class _DatabaseMigrationPreference_heterogeneous(TypedDict):
    heterogeneous: "aws_sdk_migrationhubstrategy.types.heterogeneous.Heterogeneous"


class _DatabaseMigrationPreference_homogeneous(TypedDict):
    homogeneous: "aws_sdk_migrationhubstrategy.types.homogeneous.Homogeneous"


class _DatabaseMigrationPreference_noPreference(TypedDict):
    noPreference: "aws_sdk_migrationhubstrategy.types.no_database_migration_preference.NoDatabaseMigrationPreference"


DatabaseMigrationPreference: TypeAlias = (
    _DatabaseMigrationPreference_heterogeneous
    | _DatabaseMigrationPreference_homogeneous
    | _DatabaseMigrationPreference_noPreference
)


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseMigrationPreference) -> dict:
    if "heterogeneous" in value:
        import aws_sdk_migrationhubstrategy.types.heterogeneous

        return {
            "heterogeneous": aws_sdk_migrationhubstrategy.types.heterogeneous.serialize_json(
                value["heterogeneous"]
            )
        }
    elif "homogeneous" in value:
        import aws_sdk_migrationhubstrategy.types.homogeneous

        return {
            "homogeneous": aws_sdk_migrationhubstrategy.types.homogeneous.serialize_json(
                value["homogeneous"]
            )
        }
    elif "noPreference" in value:
        import aws_sdk_migrationhubstrategy.types.no_database_migration_preference

        return {
            "noPreference": aws_sdk_migrationhubstrategy.types.no_database_migration_preference.serialize_json(
                value["noPreference"]
            )
        }
    else:
        raise SerializationError("DatabaseMigrationPreference: no variant present")


def deserialize_json(data: dict) -> DatabaseMigrationPreference:
    if "heterogeneous" in data:
        import aws_sdk_migrationhubstrategy.types.heterogeneous

        return {
            "heterogeneous": aws_sdk_migrationhubstrategy.types.heterogeneous.deserialize_json(
                data["heterogeneous"]
            )
        }
    elif "homogeneous" in data:
        import aws_sdk_migrationhubstrategy.types.homogeneous

        return {
            "homogeneous": aws_sdk_migrationhubstrategy.types.homogeneous.deserialize_json(
                data["homogeneous"]
            )
        }
    elif "noPreference" in data:
        import aws_sdk_migrationhubstrategy.types.no_database_migration_preference

        return {
            "noPreference": aws_sdk_migrationhubstrategy.types.no_database_migration_preference.deserialize_json(
                data["noPreference"]
            )
        }
    else:
        raise DeserializationError(
            "DatabaseMigrationPreference: no recognized variant key"
        )
