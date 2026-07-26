"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#DatabasePreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.database_management_preference
    import capo_migrationhubstrategy.types.database_migration_preference


class DatabasePreferences(TypedDict, closed=True):
    database_management_preference: NotRequired[
        "capo_migrationhubstrategy.types.database_management_preference.DatabaseManagementPreference"
    ]
    """<p> Specifies whether you're interested in self-managed databases or databases managed by AWS. </p>"""
    database_migration_preference: NotRequired[
        "capo_migrationhubstrategy.types.database_migration_preference.DatabaseMigrationPreference"
    ]
    """<p> Specifies your preferred migration path. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabasePreferences) -> dict:
    out: dict = {}
    if "database_management_preference" in value:
        out["databaseManagementPreference"] = value["database_management_preference"]
    if "database_migration_preference" in value:
        import capo_migrationhubstrategy.types.database_migration_preference

        out["databaseMigrationPreference"] = (
            capo_migrationhubstrategy.types.database_migration_preference.serialize_json(
                value["database_migration_preference"]
            )
        )
    return out


def deserialize_json(data: dict) -> DatabasePreferences:
    out: DatabasePreferences = {}  # type: ignore[typeddict-item]
    if "databaseManagementPreference" in data:
        out["database_management_preference"] = data["databaseManagementPreference"]
    if "databaseMigrationPreference" in data:
        import capo_migrationhubstrategy.types.database_migration_preference

        out["database_migration_preference"] = (
            capo_migrationhubstrategy.types.database_migration_preference.deserialize_json(
                data["databaseMigrationPreference"]
            )
        )
    return out
