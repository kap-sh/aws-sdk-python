"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TargetDataSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.table_preparation_mode


class TargetDataSetting(TypedDict, closed=True):
    table_preparation_mode: NotRequired[
        "capo_database_migration_service.types.table_preparation_mode.TablePreparationMode"
    ]
    """<p>This setting determines how DMS handles the target tables before starting a data migration, either by leaving them untouched, dropping and recreating them, or truncating the existing data in the target tables.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetDataSetting) -> dict:
    out: dict = {}
    if "table_preparation_mode" in value:
        import capo_database_migration_service.types.table_preparation_mode

        out["TablePreparationMode"] = (
            capo_database_migration_service.types.table_preparation_mode.serialize_aws_json_1_1(
                value["table_preparation_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetDataSetting:
    out: TargetDataSetting = {}  # type: ignore[typeddict-item]
    if "TablePreparationMode" in data:
        import capo_database_migration_service.types.table_preparation_mode

        out["table_preparation_mode"] = (
            capo_database_migration_service.types.table_preparation_mode.deserialize_aws_json_1_1(
                data["TablePreparationMode"]
            )
        )
    return out
