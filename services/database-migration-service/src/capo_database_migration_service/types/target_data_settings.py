"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TargetDataSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.target_data_setting

TargetDataSettings: TypeAlias = list[
    "capo_database_migration_service.types.target_data_setting.TargetDataSetting"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetDataSettings) -> list:
    import capo_database_migration_service.types.target_data_setting

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.target_data_setting.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TargetDataSettings:
    import capo_database_migration_service.types.target_data_setting

    out: TargetDataSettings = []
    for item in data:
        out.append(
            capo_database_migration_service.types.target_data_setting.deserialize_aws_json_1_1(
                item
            )
        )
    return out
